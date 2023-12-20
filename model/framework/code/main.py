# imports
import os
import csv
import sys
import joblib
import numpy as np
import pandas as pd
from rdkit import Chem
from rdkit.Chem.Descriptors import MolWt
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import MolFromSmiles
from rdkit.Chem.AllChem import GetMorganFingerprintAsBitVect

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))

# load pre-trained model
model_path= os.path.abspath(os.path.join(root,"..", "..","checkpoints", "XGBoost_Morgan2.m"))
model_pre = joblib.load(model_path)

# Functions
def Fingerprint_compute(Smi):
    try:
        mol = Chem.MolFromSmiles(Smi)
        fp_hash = AllChem.GetMorganFingerprintAsBitVect(mol,2,nBits=1024)
        fp = fp_hash.ToBitString()
        return fp
    except:
        return 'error'

def Compute(smiles_list): #pass smiles list
    List_fp = []
    for i in range(0,len(smiles_list)):
        smi = smiles_list[i] 
        fp = Fingerprint_compute(smi)
        fp_split = list(str(fp))
        List_fp.append(fp_split)
    df_fp = pd.DataFrame(List_fp)
    return df_fp

def my_model(smiles_list):
    df_pre = Compute(smiles_list) #compute expects a list
    X = np.array(df_pre)
    proba_pre = model_pre.predict_proba(X)
    list_active = [x[1] for x in proba_pre]

    return list_active # return the list of predicted probabilities(Outputs)


# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]

# run model (# predict bioactivity probability score)
outputs = my_model(smiles_list)

#check input and output have the same length
input_len = len(smiles_list)
output_len = len(outputs)
assert input_len == output_len

# write output in a .csv file (save result)
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["value"])  # header
    for o in outputs:
        writer.writerow([o])

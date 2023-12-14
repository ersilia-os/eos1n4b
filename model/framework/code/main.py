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

# Functions
def Fingerprint_compute(Smi):
    try:
        mol = Chem.MolFromSmiles(Smi)
        fp_hash = AllChem.GetMorganFingerprintAsBitVect(mol,2,nBits=1024)
        fp = fp_hash.ToBitString()
        return fp
    except:
        return 'error'

def Compute(df):
    length = len(df)
    List_smiles = df.iloc[:, 0]

    List_fp = []
    for i in range(0,length):
        smi = List_smiles[i]
        if smi == 'error':
            continue
        else:
            fp = Fingerprint_compute(smi)
            fp_split = list(str(fp))
            List_fp.append(fp_split)
    df_fp = pd.DataFrame(List_fp)
    return df_fp

def class_type2(class_pre):
    flag = 'Inactive'
    if class_pre == 1:
        flag = 'Active'
    return flag

def predict_class(input_file, model_pre, output_file):
    df_input = pd.read_csv(input_file)
    df_pre = Compute(df_input)
    X = np.array(df_pre)
    class_pre = model_pre.predict(X)
    proba_pre = model_pre.predict_proba(X)
    list_active   = [x[1] for x in proba_pre]
    list_inactive = [x[0] for x in proba_pre]
    df_pre.insert(0,'SMILES',df_input.iloc[:, 0])
    df_pre.insert(1,'class_pre',class_pre)
    df_pre.insert(2,'Probability_active',list_active)
    df_pre.insert(3,'Probability_inactive',list_inactive)

    df_pre['Bioactivity_pre'] = df_pre['class_pre'].apply(class_type2)

    df_pre = df_pre[['SMILES','Bioactivity_pre','Probability_active']]
    df_pre_final = df_pre.sort_values(by="Probability_active",ascending= False)  
    df_pre_final.to_csv(output_file,index=None)

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))
# load pre-trained model
model_path= os.path.abspath(os.path.join(root,"..", "..","checkpoints", "XGBoost_Morgan2.m"))
model_pre = joblib.load(model_path)

# predict bioactivity and save results
predict_class(input_file, model_pre, output_file)

FROM bentoml/model-server:0.11.0-py38
MAINTAINER ersilia

RUN pip install rdkit==2022.9.5
RUN pip install pandas==1.3.5
RUN pip install numpy==1.24
RUN pip install scikit-learn==0.23.2
RUN pip install joblib==0.13.2
RUN conda install -c conda-forge xgboost=1.0.2

WORKDIR /repo
COPY . /repo

FROM bentoml/model-server:0.11.0-py38
MAINTAINER ersilia

RUN conda install -c conda-forge cmake==4.0.3
RUN conda install -c conda-forge numpy==1.24
RUN pip install rdkit==2022.9.5
RUN pip install pandas==1.3.5
RUN conda install -c conda-forge scikit-learn==0.23.2
RUN pip install joblib==0.13.2
RUN pip install xgboost==1.0.2

WORKDIR /repo
COPY . /repo

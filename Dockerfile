FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN pip install rdkit-pypi==2022.9.5
RUN conda install pandas==0.25.1
RUN conda install numpy==1.16.5
RUN conda nstall joblib==0.13.2
RUN conda install scikit-learn==0.21.3
RUN pip install xgboost==1.0.2

WORKDIR /repo
COPY . /repo

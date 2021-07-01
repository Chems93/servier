# syntax=docker/dockerfile:1
FROM python:3.6
ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"
WORKDIR /project
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
RUN mkdir /root/.conda
RUN bash Miniconda3-latest-Linux-x86_64.sh -b
    #&& export PATH=~/miniconda/bin:$PATH
RUN conda update -n base conda \
    && conda install -c conda-forge rdkit
COPY . .
RUN python setup.py install
CMD ["python", "main/main.py"]
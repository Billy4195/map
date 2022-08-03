FROM python:3.7
MAINTAINER Billy Su "billy.su@sifive.com"

# system packages for general use
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get -yq install \
    sudo \
    tcsh \
    bash

# Software for Dash deployment
RUN apt-get -y install \
    vim \
    nginx

# install python package dependencies of the app
RUN pip install --upgrade pip
RUN pip install django==2.2.14 && \
    pip install django-cors-headers && \
    pip install channels && \
    pip install uvloop websockets && \
    pip install dask==2 numba==0.48.0 numpy==1.19 && \
    pip install uvicorn beaker pandas colorama==0.4.1 hdf5plugin toolz fsspec cloudpickle gitpython click pylibmc

EXPOSE 8002
EXPOSE 8080

# Add an agent user for NFS access
RUN groupadd -g 9002 compute
RUN groupadd -g 1885 bsu
RUN groupadd -g 10005 teamperf
RUN useradd -m -d /home/bsu/ -s /bin/bash -r -u 1885 -g 1885 bsu
RUN usermod -aG compute bsu
RUN usermod -aG teamperf bsu


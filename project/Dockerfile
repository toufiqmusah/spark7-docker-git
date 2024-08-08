FROM python:3.9.16-slim
# FROM pytorch/pytorch:1.12.0-cuda11.3-cudnn8-runtime


COPY ./requirements.txt /spark/requirements.txt 

# Set environment variable to prevent interactive prompts
# ENV DEBIAN_FRONTEND=noninteractive

# Update the package list and install git
# RUN apt-get update && \
#     apt-get install -y git && \
#     apt-get clean && \
#     rm -rf /var/lib/apt/lists/*

RUN pip3 install -r /spark/requirements.txt


ENV LANG=C.UTF-8

COPY . /spark

ENTRYPOINT ["python3", "/spark/mlcube.py"]
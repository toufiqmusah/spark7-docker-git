FROM python:3.9.16-slim

COPY ./requirements.txt /spark/requirements.txt 

# Set environment variable to prevent interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Update the package list and install git
RUN apt-get update && \
    apt-get install -y git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install -r /spark/requirements.txt

# RUN pip install git+https://github.com/MIC-DKFZ/MedNeXt.git@c5ed3f38b56d58c80581c75fea856865f42ddb75#egg=mednextv1
# RUN pip install https://github.com/mlcommons/medperf/archive/d072303e0bd457030da03ea9d1ab94920e0fd8af.zip#egg=medperf&subdirectory=cli

# RUN pip install https://github.com/hasan7n/mlcube/archive/7fbb1828c9c79ab52023d2919e157468deecb95a.zip#subdirectory=mlcube
# RUN pip install https://github.com/hasan7n/mlcube/archive/7fbb1828c9c79ab52023d2919e157468deecb95a.zip#subdirectory=runners/mlcube_docker
# RUN pip install https://github.com/hasan7n/mlcube/archive/7fbb1828c9c79ab52023d2919e157468deecb95a.zip#subdirectory=runners/mlcube_singularity


ENV LANG C.UTF-8

COPY . /spark

ENTRYPOINT ["python3", "/spark/mlcube.py"]
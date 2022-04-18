FROM nvidia/cuda:11.6.0-devel-ubuntu20.04

ARG DEBIAN_FRONTEND=noninteractive

ENV CONDA_DIR /opt/conda

RUN apt-get update && apt-get install -y \
    tar \
    wget \
    vim \
    curl \
    bash \
    rsync \
    gcc \
    libfreetype6-dev \
    libhdf5-serial-dev \
    libpng-dev \
    libzmq3-dev \
    unzip \
    pkg-config \
    software-properties-common \
    graphviz

# Install Conda
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-py38_4.11.0-Linux-x86_64.sh -O /tmp/Miniconda3-py38_4.11.0-Linux-x86_64.sh && \
    bash /tmp/Miniconda3-py38_4.11.0-Linux-x86_64.sh -b -p /opt/conda && \
    rm /tmp/Miniconda3-py38_4.11.0-Linux-x86_64.sh

ENV PATH $CONDA_DIR/bin:$PATH

ENV PYSPARK_PYTHON=python
ENV PYSPARK_DRIVER_PYTHON=python

# Install OpenJDK-11
RUN apt-get update && \
    apt-get install -y openjdk-11-jdk && \
    apt-get install -y ant && \
    apt-get clean;

# Fix certificate issues
RUN apt-get update && \
    apt-get install ca-certificates-java && \
    apt-get clean && \
    update-ca-certificates -f;

# Setup JAVA_HOME -- useful for docker commandline
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64/
RUN export JAVA_HOME

RUN echo "export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64/" >> ~/.bashrc

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /workspace

ADD  . .

RUN pip install -r requirements.txt

CMD python consumer.py -t ${KAFKA_TOPIC}

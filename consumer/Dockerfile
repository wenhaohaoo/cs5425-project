FROM python:3.8.13-slim-bullseye

USER 0

ENV PYSPARK_PYTHON=python
ENV PYSPARK_DRIVER_PYTHON=python

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

# Install OpenJDK-8
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

RUN pip install pyspark spark-nlp==3.1.2 sklearn pandas

WORKDIR /workspace

ADD  . .

# RUN apt-get update && apt-get install -y vim curl

# RUN pip install -r requirements.txt

# # CMD [ "python", "consumer.py", "-t", "$TOPIC" ]
CMD [ "sleep", "infinity" ]
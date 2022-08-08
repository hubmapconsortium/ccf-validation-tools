FROM ubuntu:20.04
LABEL maintainer="anitac@ebi.ac.uk" 

WORKDIR /tools

ENV ROBOT v1.9.0
ARG ROBOT_JAR=https://github.com/ontodev/robot/releases/download/$ROBOT/robot.jar
ENV ROBOT_JAR ${ROBOT_JAR}

RUN apt-get update && \
    DEBIAN_FRONTEND="noninteractive" apt-get install -y --no-install-recommends \
        git \
        openjdk-11-jre-headless \
        python3-pip \
        python-is-python3 \
        make \
        unzip \
        curl \
        jq \
        graphviz \
        npm

###### robot ######
RUN curl -L $ROBOT_JAR -o /tools/robot.jar &&\
    curl -L https://raw.githubusercontent.com/ontodev/robot/$ROBOT/bin/robot -o /tools/robot && \
    chmod +x /tools/robot && \
    chmod +x /tools/robot.jar
  
ENV PATH "/tools/:$PATH"

###### obographviz #####
RUN npm install obographviz && \
    ln -s /tools/node_modules/obographviz/bin/og2dot.js /tools/og2dot.js

##### ontobio ######
RUN cd /tools \
&& git clone 'https://github.com/biolink/ontobio.git' \
&& cd ontobio \
&& pip install -e .[dev,test]
ENV PATH "/tools/ontobio/bin:$PATH"

#### install python dependencies ####
COPY requirements.txt /tools/requirements.txt
RUN python -m pip install --upgrade pip &&\
    pip install -r requirements.txt
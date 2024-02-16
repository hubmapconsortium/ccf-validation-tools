FROM ubuntu:22.04
LABEL maintainer="anitac@ebi.ac.uk" 

WORKDIR /tools

ENV ROBOT v1.9.5
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
        nodejs \
        npm \
        graphviz

###### robot ######
RUN curl -L $ROBOT_JAR -o /tools/robot.jar &&\
    curl -L https://raw.githubusercontent.com/ontodev/robot/$ROBOT/bin/robot -o /tools/robot && \
    chmod +x /tools/robot && \
    chmod +x /tools/robot.jar
  
ENV PATH "/tools/:$PATH"

###### Update Node version #####
# nvm environment variables
ENV NODE_VERSION 20.9.0
ENV NVM_VERSION 0.39.7

ENV NVM_DIR /usr/local/nvm
RUN mkdir $NVM_DIR

RUN curl --silent -o- https://raw.githubusercontent.com/creationix/nvm/v$NVM_VERSION/install.sh | bash && \
    . $NVM_DIR/nvm.sh && \
    nvm install $NODE_VERSION && \
    nvm alias default $NODE_VERSION && \
    nvm use default

ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH

###### obographviz #####
RUN npm install -g obographviz

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
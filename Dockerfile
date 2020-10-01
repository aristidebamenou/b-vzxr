FROM    debian:buster-slim

WORKDIR ./workshop

RUN     apt-get update && \
        apt-get upgrade -y && \
        apt-get install -y git && \
        apt-get install -y python && \
        git clone https://github.com/aristidebamenou/b-vzxr.git

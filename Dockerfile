FROM    alpine:3.12.0

WORKDIR ./workshop

RUN     apt-get update && \
        apt-get upgrade && \
        apt-get install git && \
        apt-get install python && \
        apt-get clone git@github.com:aristidebamenou/b-vzxr.git

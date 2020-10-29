FROM ubuntu

ENV pythonbuffer=1

RUN apt update && \
    apt upgrade -y && \
    apt install python3 python3-pip curl -y && \
    pip3 install pandas numpy && \
    pip3 install -i https://test.pypi.org/simple/ dfunc==0.0.2

FROM ubuntu:14.04

RUN apt-get update
RUN apt-get install -y -qq curl git python-pip wget
WORKDIR /opt
RUN git clone https://github.com/ianmiell/shutit-distro.git
WORKDIR shutit
RUN pip install -r requirements.txt

WORKDIR /space/git/shutitdist/tls
RUN /opt/shutit/shutit build --shutit_module_path .. --delivery bash

CMD ["/bin/bash"] 

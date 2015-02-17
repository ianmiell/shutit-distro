FROM ubuntu:14.04

RUN apt-get update
RUN apt-get install -y -qq curl git python-pip wget wget
WORKDIR /opt
RUN git clone https://github.com/ianmiell/shutit-distro.git
RUN git clone https://github.com/ianmiell/shutit.git
WORKDIR shutit
RUN pip install -r requirements.txt

WORKDIR /space/git/shutit-distro/openssh
RUN /opt/shutit/shutit build --shutit_module_path .. --delivery bash

CMD ["/bin/bash"] 

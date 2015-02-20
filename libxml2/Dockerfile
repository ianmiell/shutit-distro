FROM imiell/sd_shutit

RUN apt-get update && apt-get install -y -qq curl git python-pip
WORKDIR /opt
RUN git clone https://github.com/ianmiell/shutit-distro.git

WORKDIR /opt/shutit/library/libxml2
RUN /opt/shutit/shutit build --shutit_module_path .. --delivery bash

CMD ["/bin/bash"] 

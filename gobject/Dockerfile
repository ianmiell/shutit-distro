FROM imiell/sd_shutit

RUN apt-get install -y -qq curl git python-pip wget
WORKDIR /opt
RUN git clone https://github.com/ianmiell/shutit-distro.git

WORKDIR /opt/shutit-distro/gobject
RUN /opt/shutit/shutit build --shutit_module_path .. --delivery bash

CMD ["/bin/bash"] 

FROM imiell/sd_shutit

WORKDIR /opt
RUN git clone https://github.com/ianmiell/shutit-distro.git

WORKDIR /opt/shutit-distro/python3
RUN /opt/shutit/shutit build --shutit_module_path .. --delivery bash

CMD ["/bin/bash"] 

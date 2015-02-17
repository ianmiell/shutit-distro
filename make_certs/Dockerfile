FROM imiell/sd_shutit

WORKDIR /opt
RUN git clone https://github.com/ianmiell/shutit-distro.git

WORKDIR /space/git/shutitdist/make_certs
RUN /opt/shutit/shutit build --shutit_module_path .. --delivery bash

CMD ["/bin/bash"] 

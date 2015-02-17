FROM imiell/sd_shutit

WORKDIR /opt
RUN git clone https://github.com/ianmiell/shutit-distro.git

WORKDIR /opt/shutit-distro/libgpg_error
RUN /opt/shutit/shutit build --shutit_module_path .. --delivery bash

CMD ["/bin/bash"] 

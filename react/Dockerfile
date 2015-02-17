FROM imiell/sd_node

WORKDIR /opt
RUN git clone https://github.com/ianmiell/shutit-distro.git

WORKDIR /home/imiell/shutit/library/react <- TODO You will likely need to to change this
RUN /opt/shutit/shutit build --shutit_module_path .. --delivery bash

CMD ["/bin/bash"] 

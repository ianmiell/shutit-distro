FROM imiell/sd_node

RUN apt-get update
RUN apt-get install -y -qq curl git python-pip
WORKDIR /opt
RUN git clone https://github.com/ianmiell/shutit.git
WORKDIR shutit
RUN pip install -r requirements.txt

WORKDIR /home/imiell/shutit/library/react <- TODO You will likely need to to change this
RUN /opt/shutit/shutit build --shutit_module_path /opt/shutit/library --delivery bash

CMD ["/bin/bash"] 

ARG=$1
export SHUTIT_PORT=${ARG:-8080}
#while [ 1 ]; do shutit serve -m .. 2>&1 > /tmp/shutit-distro_server.log; sleep 2; done

export N_SERVERS=100
#Handy
CURRDIR=$(pwd)
for p in $(jot $N_SERVERS 8100); do sleep 10 && cd $(dirname $(which shutit))/.. && echo SHUTIT_PORT=$p shutit serve -m $CURRDIR/.. --image_tag imiell/sd_base 2>&1 \| tee /tmp/shutit-distro_out_$p \&;  done | sh


ARG=$1
export SHUTIT_PORT=${ARG:-8080}
while [ 1 ]; do shutit serve -m .. 2>&1 > /tmp/shutit-distro_server.log; sleep 2; done

#Handy
#for p in $(jot 10 8081); do echo SHUTIT_PORT=$p shutit serve -m .. \| tee /tmp/shutit-distro_out_$p \&;  done | sh


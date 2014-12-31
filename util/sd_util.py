from shutit_module import ShutItModule

# To include, add this to build.sh
## Include util
#export PYTHONPATH=$PYTHONPATH:`pwd`/../..


# From: http://www.linuxfromscratch.org/blfs/view/stable/x/xcb-proto.html
#       to set up the environment
def setup_x_environment(shutit):
	shutit.send('export XORG_PREFIX=/usr')
	shutit.send('export XORG_CONFIG="--prefix=$XORG_PREFIX --sysconfdir=/etc --localstatedir=/var --disable-static"')


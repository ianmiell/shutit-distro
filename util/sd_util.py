from shutit_module import ShutItModule

# To include, add this to build.sh
## Include util
#export PYTHONPATH=$PYTHONPATH:`pwd`/../..


# From: http://www.linuxfromscratch.org/blfs/view/stable/x/xcb-proto.html
#       to set up the environment
def setup_x_environment(shutit):
	shutit.send('export XORG_PREFIX=/usr')
	shutit.send('export XORG_CONFIG="--prefix=$XORG_PREFIX --sysconfdir=/etc --localstatedir=/var --disable-static"')
	shutit.send('mkdir -p /etc/profile.d')
	shutit.send('touch /etc/profile.d/xorg.sh')
	shutit.add_line_to_file('/etc/profile.d/xorg.sh','XORG_PREFIX="/usr"')
	shutit.add_line_to_file('/etc/profile.d/xorg.sh','XORG_CONFIG="--prefix=$XORG_PREFIX --sysconfdir=/etc --localstatedir=/var --disable-static"')
	shutit.add_line_to_file('/etc/profile.d/xorg.sh','export XORG_PREFIX XORG_CONFIG')
	shutit.send('chmod 644 /etc/profile.d/xorg.sh')


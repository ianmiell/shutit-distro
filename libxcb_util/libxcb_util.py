"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class libxcb_util(ShutItModule):

	def build(self, shutit):
		import sd_util
		sd_util.setup_x_environment(shutit)
		shutit.send('mkdir -p /tmp/build/libxcb_util')
		shutit.send('cd /tmp/build/libxcb_util')
		shutit.get_url('xcb-util-0.4.0.tar.bz2',['http://xcb.freedesktop.org/dist'])
		shutit.send('bunzip2 -c xcb-util-0.4.0.tar.bz2 | tar -xf -')
		shutit.send('cd libxcb_util*')
		shutit.send('./configure $XORG_CONFIG')
		shutit.send('make')
		shutit.send('make install')
		return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/libxcb_util')
		return True

def module():
	return libxcb_util(
		'shutit.tk.sd.libxcb_util.libxcb_util', 158844782.008701,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.libxcb.libxcb']
	)


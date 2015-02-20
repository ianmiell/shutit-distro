"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class libxcb_util_keysyms(ShutItModule):

	def build(self, shutit):
		import sd_util
		sd_util.setup_x_environment(shutit)
		shutit.send('mkdir -p /tmp/build/libxcb_util_keysyms')
		shutit.send('cd /tmp/build/libxcb_util_keysyms')
		shutit.get_url('xcb-util-0.4.0.tar.bz2',['http://xcb.freedesktop.org/dist'])
		shutit.send('bunzip2 -c xcb-util-0.4.0.tar.bz2 | tar -xf -')
		shutit.send('cd libxcb_util_keysyms*')
		shutit.send('./configure $XORG_CONFIG')
		shutit.send('make')
		shutit.send('make install')
		return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/libxcb_util_keysyms')
		return True

def module():
	return libxcb_util_keysyms(
		'shutit.tk.sd.libxcb_util_keysyms.libxcb_util_keysyms', 158844782.008701,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.libxcb.libxcb']
	)


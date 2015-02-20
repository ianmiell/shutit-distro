"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class libxcb_util_renderutil(ShutItModule):

	def build(self, shutit):
		import sd_util
		sd_util.setup_x_environment(shutit)
		shutit.send('mkdir -p /tmp/build/libxcb_util_renderutil')
		shutit.send('cd /tmp/build/libxcb_util_renderutil')
		shutit.get_url('xcb-util-renderutil-0.3.9.tar.bz2',['http://xcb.freedesktop.org/dist'])
		shutit.send('bunzip2 -c xcb-util-0.4.0.tar.bz2 | tar -xf -')
		shutit.send('cd libxcb_util_renderutil*')
		shutit.send('./configure $XORG_CONFIG')
		shutit.send('make')
		shutit.send('make install')
		return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/libxcb_util_renderutil')
		return True

def module():
	return libxcb_util_renderutil(
		'shutit.tk.sd.libxcb_util_renderutil.libxcb_util_renderutil', 158844782.008704,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.libxcb.libxcb']
	)


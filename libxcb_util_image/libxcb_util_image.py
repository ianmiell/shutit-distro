"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class libxcb_util_image(ShutItModule):

	def build(self, shutit):
		import sd_util
		sd_util.setup_x_environment(shutit)
		shutit.send('mkdir -p /tmp/build/libxcb_util_image')
		shutit.send('cd /tmp/build/libxcb_util_image')
		shutit.get_url('xcb-util-image-0.4.0.tar.bz2',['http://xcb.freedesktop.org/dist'])
		shutit.send('bunzip2 -c xcb-util-0.4.0.tar.bz2 | tar -xf -')
		shutit.send('cd libxcb_util_image*')
		shutit.send('./configure $XORG_CONFIG')
		shutit.send('make')
		shutit.send('make install')
		return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/libxcb_util_image')
		return True

def module():
	return libxcb_util_image(
		'shutit.tk.sd.libxcb_util_image.libxcb_util_image', 158844782.008702,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.libxcb_util.libxcb_util']
	)


"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class xcb_util(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		import sd_util
		sd_util.setup_x_environment(shutit)
		shutit.send('mkdir -p /tmp/build/xcb_util')
		shutit.send('cd /tmp/build/xcb_util')
		shutit.send('wget -qO- http://xcb.freedesktop.org/dist/xcb-util-0.4.0.tar.bz2 | bunzip2 -c | tar -xf -')
		shutit.send('cd xcb-util*')
		shutit.send('./configure $XORG_CONFIG')
		shutit.send('make')
		shutit.send('make install')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/xcb_util')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return xcb_util(
		'shutit.tk.sd.xcb_util.xcb_util', 158844782.0259,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.libxau.libxau','shutit.tk.sd.xcb_proto.xcb_proto']
	)


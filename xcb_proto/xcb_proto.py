"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule

class xcb_proto(ShutItModule):

	def build(self, shutit):
		import sd_util
		sd_util.setup_x_environment(shutit)
		shutit.send('mkdir -p /tmp/build/xcb_proto')
		shutit.send('cd /tmp/build/xcb_proto')
		shutit.send('wget -qO- http://xcb.freedesktop.org/dist/xcb-proto-1.11.tar.bz2 | bunzip2 -c | tar -xf -')
		shutit.send('cd xcb-proto*')
		shutit.send('./configure $XORG_CONFIG')
		shutit.send('make install')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/xcb_proto')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return xcb_proto(
		'shutit.tk.sd.xcb_proto.xcb_proto', 158844782.008123,
		description='',
		maintainer='',
		depends=['shutit.tk.setup']
	)


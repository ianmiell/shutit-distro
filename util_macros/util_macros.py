"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule

class util_macros(ShutItModule):

	def build(self, shutit):
		import sd_util
		sd_util.setup_x_environment(shutit)
		shutit.send('mkdir -p /tmp/build/util_macros')
		shutit.send('cd /tmp/build/util_macros')
		shutit.send('wget -qO- http://xorg.freedesktop.org/releases/individual/util/util-macros-1.19.0.tar.bz2 | bunzip2 -c | tar -xf -')
		shutit.send('cd util*')
		shutit.send('./configure $XORG_CONFIG')
		shutit.send('make install')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/util_macros')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return util_macros(
		'shutit.tk.sd.util_macros.util_macros', 158844782.0019,
		description='',
		maintainer='',
		depends=['shutit.tk.setup']
	)


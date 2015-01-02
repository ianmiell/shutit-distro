"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule

class libxau(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		import sd_util
		sd_util.setup_x_environment(shutit)
		shutit.send('mkdir -p /tmp/build/libxau')
		shutit.send('cd /tmp/build/libxau')
		shutit.send('wget -qO- http://xorg.freedesktop.org/releases/individual/lib/libXau-1.0.8.tar.bz2 | bunzip2 -c | tar -xf -')
		shutit.send('cd libX*')
		shutit.send('./configure $XORG_CONFIG')
		shutit.send('make')
		shutit.send('make install')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/libxau')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return libxau(
		'shutit.tk.sd.libxau.libxau', 158844782.0082,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.x7proto.x7proto']
	)


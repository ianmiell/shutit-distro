"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class alsa_lib(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/alsa_lib')
		shutit.send('cd /tmp/build/alsa_lib')
		shutit.send('wget -qO- http://alsa.cybermirror.org/lib/alsa-lib-1.0.28.tar.bz2 | bunzip2 -c | tar -xf -')
		shutit.send('cd alsa*')
		shutit.send('./configure')
		shutit.send('make')
		shutit.send('make install')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/alsa_lib')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return alsa_lib(
		'shutit.tk.sd.alsa_lib.alsa_lib', 158844782.0066,
		description='',
		maintainer='',
		depends=['shutit.tk.setup']
	)


"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class pkg_config(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/pkg_config')
		shutit.send('cd /tmp/build/pkg_config')
		shutit.send('curl -L http://pkgconfig.freedesktop.org/releases/pkgconfig-0.18.tar.gz | tar -zxf -')
		shutit.send('cd pkgconfig-*')
		shutit.send('./configure --prefix=/usr')
		shutit.send('make')
		shutit.send('make install')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	#def check_ready(self, shutit):
	#	return True
	
	#def start(self, shutit):
	#	return True

	#def stop(self, shutit):
	#	return True

	#def finalize(self, shutit):
	#	return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return pkg_config(
		'shutit.tk.sd.pkg_config.pkg_config', 158844782.00031,
		description='',
		maintainer='',
		depends=['shutit.tk.setup']
	)


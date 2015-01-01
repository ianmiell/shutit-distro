"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class libidn(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/libidn')
		shutit.send('cd /tmp/build/libidn')
		shutit.send('wget -qO- http://ftp.gnu.org/gnu/libidn/libidn-1.29.tar.gz | tar -zxf -')
		shutit.send('cd libidn*')
		shutit.send('./configure --prefix=/usr --disable-static')
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
	return libidn(
		'shutit.tk.sd.libidn.libidn', 158844782.0017,
		description='',
		maintainer='',
		depends=['shutit.tk.setup']
	)


"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class libarchive(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/libarchive')
		shutit.send('cd /tmp/build/libarchive')
		shutit.send('wget -qO- http://www.libarchive.org/downloads/libarchive-3.1.2.tar.gz | tar -zxf -')
		shutit.send('cd libarchive-*')
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

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/libarchive')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return libarchive(
		'shutit.tk.sd.libarchive.libarchive', 158844782.0062,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.lzo.lzo']
	)


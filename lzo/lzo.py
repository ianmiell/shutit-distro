"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class lzo(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/lzo')
		shutit.send('cd /tmp/build/lzo')
		shutit.send('wget -qO- http://www.oberhumer.com/opensource/lzo/download/lzo-2.08.tar.gz | tar -zxf -')
		shutit.send('cd lzo-*')
		shutit.send('./configure --prefix=/usr --enable-shared --disable-static --docdir=/usr/share/doc/lzo-2.08')
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
	return lzo(
		'shutit.tk.sd.lzo.lzo', 158844782.0005,
		description='',
		maintainer='',
		depends=['shutit.tk.setup']
	)


"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class libjpeg(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/libjpeg_turbo')
		shutit.send('cd /tmp/build/libjpeg_turbo')
		shutit.send('wget -qO- http://downloads.sourceforge.net/libjpeg-turbo/libjpeg-turbo-1.3.1.tar.gz | tar -zxf -')
		shutit.send('cd libj*')
		shutit.send('''sed -i -e '/^docdir/     s:$:/libjpeg-turbo-1.3.1:' -e '/^exampledir/ s:$:/libjpeg-turbo-1.3.1:' Makefile.in''')
		shutit.send('./configure --prefix=/usr --mandir=/usr/share/man --with-jpeg8 --disable-static')
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
		shutit.send('rm -rf /tmp/build/libjpeg_turbo')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return libjpeg(
		'shutit.tk.sd.libjpeg.libjpeg', 158844782.0113,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.nasm.nasm']
	)


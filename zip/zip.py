"""ShutIt module. See http://shutit.tk/
"""

from shutit_module import ShutItModule


class zip(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/zip')
		shutit.send('cd /tmp/build/zip')
		shutit.send('wget -qO- http://downloads.sourceforge.net/infozip/zip30.tar.gz | tar -zxf -')
		shutit.send('cd zip*')
		shutit.send('make -f unix/Makefile generic_gcc')
		shutit.send('make prefix=/usr MANDIR=/usr/share/man/man1 -f unix/Makefile install')
		return True

	def get_config(self, shutit):
		return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/zip')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return zip(
		'shutit.tk.sd.zip.zip', 158844782.00801,
		description='',
		maintainer='',
		depends=['shutit.tk.setup']
	)


"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class libgcrypt(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/libgcrypt')
		shutit.send('cd /tmp/build/libgcrypt')
		shutit.send('wget -qO- ftp://ftp.gnupg.org/gcrypt/libgcrypt/libgcrypt-1.6.2.tar.bz2 | bunzip2 -c | tar -xf -')
		shutit.send('cd libg*')
		shutit.send('./configure --prefix=/usr')
		shutit.send('make')
		shutit.send('make install')
		shutit.send('install -v -dm755   /usr/share/doc/libgcrypt-1.6.2')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/libgcrypt')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return libgcrypt(
		'shutit.tk.sd.libgcrypt.libgcrypt', 158844782.001355,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.libgpg_error.libgpg_error']
	)


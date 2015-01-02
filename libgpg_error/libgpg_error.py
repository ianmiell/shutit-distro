"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class libgpg_error(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/libgpg_error')
		shutit.send('cd /tmp/build/libgpg_error')
		shutit.send('wget -qO- ftp://ftp.gnupg.org/gcrypt/libgpg-error/libgpg-error-1.17.tar.bz2 | bunzip2 -c | tar -xf -')
		shutit.send('cd libgpg*')
		shutit.send('./configure --prefix=/usr --disable-static')
		shutit.send('make')
		shutit.send('make install')
		shutit.send('install -v -m644 -D README /usr/share/doc/libgpg-error-1.17/README')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/libgpg_error')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return libgpg_error(
		'shutit.tk.sd.libgpg_error.libgpg_error', 158844782.00135,
		description='',
		maintainer='',
		depends=['shutit.tk.setup']
	)


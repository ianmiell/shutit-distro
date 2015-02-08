"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class python3(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir /tmp/build/python')
		shutit.send('cd /tmp/build/python')
		shutit.send('wget -qO- https://www.python.org/ftp/python/3.4.2/Python-3.4.2.tar.xz | xz -d | tar -xf -')
		shutit.send('cd Python-*')
		shutit.send('./configure --prefix=/usr --enable-shared --with-system-expat --with-system-ffi --enable-unicode=ucs4 --without-ensurepip')
		shutit.send('make')
		shutit.send('make install',check_exit=False) # why? seems ok
		shutit.send('/usr/lib/libpython3.4m.so')
		shutit.send('/usr/lib/libpython3.so')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/python')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return python3(
		'shutit.tk.sd.python3.python3', 158844782.002553,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.libffi.libffi','shutit.tk.sd.sqlite.sqlite','shutit.tk.sd.make_certs.make_certs']
	)


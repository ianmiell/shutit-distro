"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class python2(ShutItModule):

	def build(self, shutit):
		shutit.send('mkdir /tmp/build/python')
		shutit.send('cd /tmp/build/python')
		shutit.send('wget -qO- http://www.python.org/ftp/python/2.7.8/Python-2.7.8.tar.xz | xz -d | tar -xf -')
		shutit.send('cd Python-*')
		shutit.send('./configure --prefix=/usr --enable-shared --with-system-expat --with-system-ffi --enable-unicode=ucs4')
		shutit.send('make')
		shutit.send('make install',check_exit=False) # why? seems ok
		shutit.send('chmod -v 755 /usr/lib/libpython2.7.so.1.0')
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
	return python2(
		'shutit.tk.sd.python2.python2', 158844782.00255,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.libffi.libffi','shutit.tk.sd.sqlite.sqlite','shutit.tk.sd.make_certs.make_certs']
	)


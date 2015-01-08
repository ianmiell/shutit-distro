"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class haproxy(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/haproxy')
		shutit.send('cd /tmp/build/haproxy')
		shutit.send('wget -qO- http://www.haproxy.org/download/1.5/src/haproxy-1.5.10.tar.gz | tar -zxf -')
		shutit.send('cd haproxy*')
		shutit.send('make TARGET=linux2628 USE_PCRE=1 USE_OPENSSL=1 ADDLIB=-lz DEBUG=-s USE_FUTEX=1')
		shutit.send('make install')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/haproxy')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return haproxy(
		'shutit.tk.sd.haproxy.haproxy', 158844782.0231,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.pcre.pcre']
	)


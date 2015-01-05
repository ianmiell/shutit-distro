"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class libevent(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/libevent')
		shutit.send('cd /tmp/build/libevent')
		shutit.send('wget -qO- https://github.com/downloads/libevent/libevent/libevent-2.0.21-stable.tar.gz | tar -zxf -')
		shutit.send('cd libevent*')
		shutit.send('./configure --prefix=/usr')
		shutit.send('make')
		shutit.send('make install')
		return True

	def get_config(self, shutit):
		return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/libevent')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return libevent(
		'shutit.tk.sd.libevent.libevent', 158844782.0266,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.make_certs.make_certs']
	)


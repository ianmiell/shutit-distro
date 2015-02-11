"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class libsnappy(ShutItModule):

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/libsnappy')
		shutit.send('cd /tmp/build/libsnappy')
		shutit.send('wget -qO- https://snappy.googlecode.com/files/snappy-1.1.1.tar.gz | tar -zxf -')
		shutit.send('cd snappy*')
		shutit.send('./configure --prefix=/usr')
		shutit.send('make')
		shutit.send('make install')
		return True

	def get_config(self, shutit):
		return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/libsnappy')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return libsnappy(
		'shutit.tk.sd.libsnappy.libsnappy', 158844782.0267,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.make_certs.make_certs']
	)


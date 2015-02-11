"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class libpopt(ShutItModule):

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/libpopt')
		shutit.send('cd /tmp/build/libpopt')
		shutit.send('wget -qO- http://rpm5.org/files/popt/popt-1.16.tar.gz | tar -zxf -')
		shutit.send('cd popt*')
		shutit.send('./configure --prefix=/usr --disable-static')
		shutit.send('make')
		shutit.send('make install')
		return True

	def get_config(self, shutit):
		return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/libpopt')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return libpopt(
		'shutit.tk.sd.libpopt.libpopt', 158844782.02675,
		description='',
		maintainer='',
		depends=['shutit.tk.setup']
	)


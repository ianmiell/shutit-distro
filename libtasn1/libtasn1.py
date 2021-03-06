"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class libtasn1(ShutItModule):

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/libtasn1')
		shutit.send('cd /tmp/build/libtasn1')
		shutit.send('wget -qO- http://ftp.gnu.org/gnu/libtasn1/libtasn1-4.2.tar.gz | tar -zxf -')
		shutit.send('cd libtasn1*')
		shutit.send('./configure --prefix=/usr --disable-static')
		shutit.send('make')
		shutit.send('make install')
		return True

	def get_config(self, shutit):
		return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/libtasn1')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return libtasn1(
		'shutit.tk.sd.libtasn1.libtasn1', 158844782.00795,
		description='',
		maintainer='',
		depends=['shutit.tk.setup']
	)


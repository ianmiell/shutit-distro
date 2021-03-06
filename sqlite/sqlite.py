"""ShutIt module. See http://shutit.tk/
"""

from shutit_module import ShutItModule


class sqlite(ShutItModule):


	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/sqlite')
		shutit.send('cd /tmp/build/sqlite')
		shutit.send('wget -qO- http://www.sqlite.org/2014/sqlite-autoconf-3080701.tar.gz | gunzip -c - | tar -xf -')
		shutit.send('cd sqlite-autoconf-*')
		shutit.send('./configure --prefix=/usr')
		shutit.send('make')
		shutit.send('make install')
		return True

	#def get_config(self, shutit):
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/sqlite')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return sqlite(
		'shutit.tk.sd.sqlite.sqlite', 158844782.00254,
		description='',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.setup']
	)


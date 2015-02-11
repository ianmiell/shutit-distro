"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class rpm(ShutItModule):

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/rpm')
		shutit.send('cd /tmp/build/rpm')
		shutit.send('wget -qO- http://rpm.org/releases/rpm-4.11.x/rpm-4.11.2.tar.bz2 | bunzip2 -c | tar -xf -')
		shutit.send('cd rpm*')
		shutit.send('''CPPFLAGS='-I/usr/include/nspr -I/usr/include/nss' ./configure --prefix=/usr --with-external-db --without-lua''')
		shutit.send('make')
		shutit.send('make install')
		return True

	def get_config(self, shutit):
		return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/rpm')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return rpm(
		'shutit.tk.sd.rpm.rpm', 158844782.0268,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.make_certs.make_certs','shutit.tk.sd.nss.nss','shutit.tk.sd.nspr.nspr','shutit.tk.sd.libpopt.libpopt','shutit.tk.sd.berkeleydb.berkeleydb']
	)


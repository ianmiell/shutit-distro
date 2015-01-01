"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class cyrus_sasl(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/cyrus_sasl')
		shutit.send('cd /tmp/build/cyrus_sasl')
		shutit.send('wget -qO- ftp://ftp.cyrusimap.org/cyrus-sasl/cyrus-sasl-2.1.26.tar.gz | tar -zxf -')
		shutit.send('cd cyrus-sasl*')
		shutit.send('wget -qO- http://www.linuxfromscratch.org/patches/blfs/svn/cyrus-sasl-2.1.26-fixes-3.patch | patch -Np1 -i -')
		shutit.send('autoreconf -fi')
		shutit.send('./configure --prefix=/usr --sysconfdir=/etc --enable-auth-sasldb --with-dbpath=/var/lib/sasl/sasldb2 --with-saslauthd=/var/run/saslauthd')
		shutit.send('make')
		shutit.send('make install')
		shutit.send('install -v -dm700 /var/lib/sasl')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	#def check_ready(self, shutit):
	#	return True
	
	#def start(self, shutit):
	#	return True

	#def stop(self, shutit):
	#	return True

	#def finalize(self, shutit):
	#	return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return cyrus_sasl(
		'shutit.tk.sd.cyrus_sasl.cyrus_sasl', 158844782.0251,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.berkeleydb.berkeleydb','shutit.tk.sd.sqlite.sqlite']
	)


"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class berkeleydb(ShutItModule):

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/berkeleydb')
		shutit.send('cd /tmp/build/berkeleydb')
		shutit.send('wget -qO- http://download.oracle.com/berkeley-db/db-6.1.19.tar.gz | tar -zxf -')
		shutit.send('cd db*')
		shutit.send('cd build_unix')
		shutit.send('../dist/configure --prefix=/usr --enable-compat185 --enable-dbm --disable-static --enable-cxx')
		shutit.send('make')
		shutit.send('make docdir=/usr/share/doc/db-6.1.19 install')
		shutit.send('chown -v -R root:root /usr/bin/db_* /usr/include/db{,_185,_cxx}.h /usr/lib/libdb*.{so,la} /usr/share/doc/db-6.1.19')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/berkeleydb')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return berkeleydb(
		'shutit.tk.sd.berkeleydb.berkeleydb', 158844782.0249,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.tcl.tcl','shutit.tk.sd.java_binary.java_binary','shutit.tk.sd.sharutils.sharutils']
	)


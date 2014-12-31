"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class openjade(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/openjade')
		shutit.send('cd /tmp/build/openjade')
		shutit.send('wget -qO- http://downloads.sourceforge.net/openjade/openjade-1.3.2.tar.gz | tar -zxf -')
		shutit.send('cd openjade*')
		shutit.send('wget -qO- http://www.linuxfromscratch.org/patches/blfs/7.6/openjade-1.3.2-gcc_4.6-1.patch | patch -Np1 -i -')
		shutit.send('''sed -i -e '/getopts/{N;s#&G#g#;s#do .getopts.pl.;##;}' -e '/use POSIX/ause Getopt::Std;' msggen.pl''')
		shutit.send('./configure --prefix=/usr --mandir=/usr/share/man --enable-http --disable-static --enable-default-catalog=/etc/sgml/catalog --enable-default-search-path=/usr/share/sgml --datadir=/usr/share/sgml/openjade-1.3.2')
		shutit.send('make')
		shutit.send('make install')
		shutit.send('make install-man')
		shutit.send('ln -v -sf openjade /usr/bin/jade')
		shutit.send('ln -v -sf libogrove.so /usr/lib/libgrove.so')
		shutit.send('ln -v -sf libospgrove.so /usr/lib/libspgrove.so')
		shutit.send('ln -v -sf libostyle.so /usr/lib/libstyle.so')
		shutit.send('install -v -m644 dsssl/catalog /usr/share/sgml/openjade-1.3.2/')
		shutit.send('install -v -m644 dsssl/*.{dtd,dsl,sgm} /usr/share/sgml/openjade-1.3.2')
		shutit.send('install-catalog --add /etc/sgml/openjade-1.3.2.cat /usr/share/sgml/openjade-1.3.2/catalog')
		shutit.send('install-catalog --add /etc/sgml/sgml-docbook.cat /etc/sgml/openjade-1.3.2.cat')
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
	return openjade(
		'shutit.tk.sd.openjade.openjade', 158844782.0104,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.docbook_sssl.docbook_sssl']
	)


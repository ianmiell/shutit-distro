"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class opensp(ShutItModule):

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/opensp')
		shutit.send('cd /tmp/build/opensp')
		shutit.send('wget -qO- http://downloads.sourceforge.net/openjade/OpenSP-1.5.2.tar.gz | tar -zxf -')
		shutit.send('cd Open*')
		shutit.send('''sed -i 's/32,/253,/' lib/Syntax.cxx''')
		shutit.send('''sed -i 's/LITLEN          240 /LITLEN          8092/' unicode/{gensyntax.pl,unicode.syn}''')
		shutit.send('./configure --prefix=/usr --disable-static --disable-doc-build --enable-default-catalog=/etc/sgml/catalog --enable-http --enable-default-search-path=/usr/share/sgml')
		shutit.send('make pkgdatadir=/usr/share/sgml/OpenSP-1.5.2')
		shutit.send('make pkgdatadir=/usr/share/sgml/OpenSP-1.5.2 install')
		shutit.send('ln -v -sf onsgmls /usr/bin/nsgmls')
		shutit.send('ln -v -sf osgmlnorm /usr/bin/sgmlnorm')
		shutit.send('ln -v -sf ospam /usr/bin/spam')
		shutit.send('ln -v -sf ospcat /usr/bin/spcat')
		shutit.send('ln -v -sf ospent /usr/bin/spent')
		shutit.send('ln -v -sf osx /usr/bin/sx')
		shutit.send('ln -v -sf osx /usr/bin/sgml2xml')
		shutit.send('ln -v -sf libosp.so /usr/lib/libsp.so')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/opensp')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return opensp(
		'shutit.tk.sd.opensp.opensp', 158844782.0101,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.sgml_common.sgml_common']
	)


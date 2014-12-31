"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class docbook_dsssl(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/docbook_dsssl')
		shutit.send('cd /tmp/build/docbook_dsssl')
		shutit.send('curl -L http://downloads.sourceforge.net/docbook/docbook-dsssl-1.79.tar.bz2 | bunzip2 -c | tar -xf -')
		shutit.send('cd docbook*')
		shutit.send('install -v -m755 bin/collateindex.pl /usr/bin')
		shutit.send('install -v -m644 bin/collateindex.pl.1 /usr/share/man/man1')
		shutit.send('install -v -d -m755 /usr/share/sgml/docbook/dsssl-stylesheets-1.79')
		shutit.send('cp -v -R * /usr/share/sgml/docbook/dsssl-stylesheets-1.79') 
		shutit.send('install-catalog --add /etc/sgml/dsssl-docbook-stylesheets.cat /usr/share/sgml/docbook/dsssl-stylesheets-1.79/catalog')
		shutit.send('install-catalog --add /etc/sgml/dsssl-docbook-stylesheets.cat /usr/share/sgml/docbook/dsssl-stylesheets-1.79/common/catalog')
		shutit.send('install-catalog --add /etc/sgml/sgml-docbook.cat /etc/sgml/dsssl-docbook-stylesheets.cat')
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
	return docbook_dsssl(
		'shutit.tk.sd.docbook_dsssl.docbook_dsssl', 158844782.0102,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.sgml_common.sgml_common']
	)


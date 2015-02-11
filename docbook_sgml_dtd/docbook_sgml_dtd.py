"""ShutIt module. See http://shutit.tk/
"""

from shutit_module import ShutItModule


class docbook_sgml_dtd(ShutItModule):

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/docbook_sgml_dtd')
		shutit.send('cd /tmp/build/docbook_sgml_dtd')
		version = shutit.cfg[self.module_id]['version']
		shutit.send('wget -qO- http://www.docbook.org/sgml/3.1/docbk31.zip > docbook_sgml_dtd.zip')
		shutit.send('unzip docbook_sgml_dtd.zip')
		shutit.send('''sed -i -e '/ISO 8879/d' -e 's|DTDDECL "-//OASIS//DTD DocBook V3.1//EN"|SGMLDECL|g' docbook.cat''')
		shutit.send('install -v -d -m755 /usr/share/sgml/docbook/sgml-dtd-3.1')
		shutit.send('chown -R root:root .')
		shutit.send('install -v docbook.cat /usr/share/sgml/docbook/sgml-dtd-3.1/catalog')
		shutit.send('cp -v -af *.dtd *.mod *.dcl /usr/share/sgml/docbook/sgml-dtd-3.1')
		shutit.send('install-catalog --add /etc/sgml/sgml-docbook-dtd-3.1.cat /usr/share/sgml/docbook/sgml-dtd-3.1/catalog')
		shutit.send('install-catalog --add /etc/sgml/sgml-docbook-dtd-3.1.cat /etc/sgml/sgml-docbook.cat')
		return True

	def get_config(self, shutit):
		shutit.get_config(self.module_id,'version','4.5')
		return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/docbook_sgml_dtd')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return docbook_sgml_dtd(
		'shutit.tk.sd.docbook_sgml_dtd.docbook_sgml_dtd', 158844782.0103,
		description='',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.sgml_common.sgml_common']
	)


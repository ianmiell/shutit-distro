"""ShutIt module. See http://shutit.tk/
"""

from shutit_module import ShutItModule


class docbook_utils(ShutItModule):


	def is_installed(self, shutit):
		return False


	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/docbook_utils')
		shutit.send('cd /tmp/build/docbook_utils')
		shutit.send('wget -qO- ftp://sources.redhat.com/pub/docbook-tools/new-trials/SOURCES/docbook-utils-0.6.14.tar.gz | tar -zxf -')
		shutit.send('cd docbook*')
		shutit.send('wget -qO- http://www.linuxfromscratch.org/patches/blfs/7.6/docbook-utils-0.6.14-grep_fix-1.patch | patch -Np1 -i -')
		shutit.send('''sed -i 's:/html::' doc/HTML/Makefile.in''')
		shutit.send('./configure --prefix=/usr --mandir=/usr/share/man')
		shutit.send('make')
		shutit.send('make docdir=/usr/share/doc install')
		shutit.send('ln -svf docbook2htmldoctype /usr/bin/db2htmldoctype')
		shutit.send('ln -svf docbook2psdoctype /usr/bin/db2psdoctype')
		shutit.send('ln -svf docbook2dvidoctype /usr/bin/db2dvidoctype')
		shutit.send('ln -svf docbook2mandoctype /usr/bin/db2mandoctype')
		shutit.send('ln -svf docbook2pdfdoctype /usr/bin/db2pdfdoctype')
		shutit.send('ln -svf docbook2rtfdoctype /usr/bin/db2rtfdoctype')
		shutit.send('ln -svf docbook2texdoctype /usr/bin/db2texdoctype')
		shutit.send('ln -svf docbook2texidoctype /usr/bin/db2texidoctype')
		shutit.send('ln -svf docbook2txtdoctype /usr/bin/db2txtdoctype')
		return True

	def get_config(self, shutit):
		shutit.get_config(self.module_id,'version','4.5')
		return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/docbook_utils')
		return True
	def finalize(self, shutit):
		#shutit.send('rm -rf
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return docbook_utils(
		'shutit.tk.sd.docbook_utils.docbook_utils', 158844782.0105,
		description='',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.docbook_sgml_dtd.docbook_sgml_dtd','shutit.tk.sd.openjade.openjade','shutit.tk.sd.docbook_dsssl.docbook_dsssl']
	)


"""ShutIt module. See http://shutit.tk/
"""

from shutit_module import ShutItModule


class sgml_common(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')


	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/sgml_common')
		shutit.send('cd /tmp/build/sgml_common')
		shutit.send('wget -qO- ftp://sources.redhat.com/pub/docbook-tools/new-trials/SOURCES/sgml-common-0.6.3.tgz | tar -zxf -')
		shutit.send('cd sgml-common*')
		shutit.send('wget -qO- http://www.linuxfromscratch.org/patches/blfs/7.6/sgml-common-0.6.3-manpage-1.patch | patch -Np1 -i -')
		shutit.send('autoreconf -f -i')
		shutit.send('./configure --prefix=/usr --sysconfdir=/etc')
		shutit.send('make')
		shutit.send('make docdir=/usr/share/doc install')
		shutit.send('install-catalog --add /etc/sgml/sgml-ent.cat /usr/share/sgml/sgml-iso-entities-8879.1986/catalog')
		shutit.send('install-catalog --add /etc/sgml/sgml-docbook.cat /etc/sgml/sgml-ent.cat')
		return True

	#def get_config(self, shutit):
	#	return True

	#def check_ready(self, shutit):
	#	return True
	
	#def start(self, shutit):
	#	return True

	#def stop(self, shutit):
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/sgml_common')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return sgml_common(
		'shutit.tk.sd.sgml_common.sgml_common', 158844782.0034,
		description='',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.setup']
	)


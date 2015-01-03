"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class open_ldap_client(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/open_ldap_client')
		shutit.send('cd /tmp/build/open_ldap_client')
		shutit.send('wget -qO- ftp://ftp.openldap.org/pub/OpenLDAP/openldap-release/openldap-2.4.40.tgz | tar -zxf -')
		shutit.send('cd openldap*')
		shutit.send('wget -qO- http://www.linuxfromscratch.org/patches/blfs/svn/openldap-2.4.40-blfs_paths-1.patch | patch -Np1 -i -')
		shutit.send('wget -qO- http://www.linuxfromscratch.org/patches/blfs/svn/openldap-2.4.40-symbol_versions-1.patch | patch -Np1 -i -')
		shutit.send('autoconf')
		shutit.send(r'''sed -i '/6.0.20/ a\\t__db_version_compat' configure''')
		shutit.send('./configure --prefix=/usr     --sysconfdir=/etc --disable-static  --enable-dynamic  --disable-debug   --disable-slapd')
		shutit.send('make depend')
		shutit.send('make')
		shutit.send('make install')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/open_ldap_client')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return open_ldap_client(
		'shutit.tk.sd.open_ldap_client.open_ldap_client', 158844782.0253,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.berkeleydb.berkeleydb','shutit.tk.sd.cyrus_sasl.cyrus_sasl']
	)


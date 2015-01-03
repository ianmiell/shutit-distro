"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class open_ldap(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/open_ldap')
		shutit.send('cd /tmp/build/open_ldap')
		shutit.send('wget -qO- ftp://ftp.openldap.org/pub/OpenLDAP/openldap-release/openldap-2.4.40.tgz | tar -zxf -')
		shutit.send('cd openldap*')
		shutit.send('groupadd -g 83 ldap')
		shutit.send('useradd -c "OpenLDAP Daemon Owner" -d /var/lib/openldap -u 83 -g ldap -s /bin/false ldap')
		shutit.send('wget -qO- http://www.linuxfromscratch.org/patches/blfs/svn/openldap-2.4.40-blfs_paths-1.patch | patch -Np1 -i -')
		shutit.send('wget -qO- http://www.linuxfromscratch.org/patches/blfs/svn/openldap-2.4.40-symbol_versions-1.patch | patch -Np1 -i -')
		shutit.send('autoconf')
		shutit.send(r'''sed -i '/6.0.20/ a\\t__db_version_compat' configure''')
		shutit.send('./configure --prefix=/usr --sysconfdir=/etc --localstatedir=/var --libexecdir=/usr/lib --disable-static --disable-debug --enable-dynamic --enable-crypt --enable-spasswd --enable-modules --enable-rlookups --enable-backends=mod --enable-overlays=mod --disable-ndb --disable-sql')
		shutit.send('make depend')
		shutit.send('make')
		shutit.send('make install')
		shutit.send('chmod -v 700 /var/lib/openldap')
		shutit.send('chown -v -R ldap:ldap /var/lib/openldap')
		shutit.send('chmod -v 640 /etc/openldap/{slapd.{conf,ldif},DB_CONFIG.example}')
		shutit.send('chown -v root:ldap /etc/openldap/{slapd.{conf,ldif},DB_CONFIG.example}')
		shutit.send('install -v -dm700 -o ldap -g ldap /etc/openldap/slapd.d')
		shutit.send('install -v -dm755 /usr/share/doc/openldap-2.4.40')
		shutit.send('cp -vfr doc/drafts /usr/share/doc/openldap-2.4.40')
		shutit.send('cp -vfr doc/rfc /usr/share/doc/openldap-2.4.40')
		shutit.send('cp -vfr doc/guide /usr/share/doc/openldap-2.4.40')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/open_ldap')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return open_ldap(
		'shutit.tk.sd.open_ldap.open_ldap', 158844782.0253,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.berkeleydb.berkeleydb','shutit.tk.sd.cyrus_sasl.cyrus_sasl']
	)


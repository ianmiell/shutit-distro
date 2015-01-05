"""ShutIt module. See http://shutit.tk
"""
#http://www.linuxfromscratch.org/blfs/view/svn/postlfs/mitkrb.html configs and context and configureation 
from shutit_module import ShutItModule


class postgresql(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/postgresql')
		shutit.send('cd /tmp/build/postgresql')
		shutit.send('wget -qO- http://ftp.postgresql.org/pub/source/v9.4.0/postgresql-9.4.0.tar.bz2 | bunzip2 -c | tar -xf -')
		shutit.send('cd postgres*')
		shutit.send('''sed -i '/DEFAULT_PGSOCKET_DIR/s@/tmp@/run/postgresql@' src/include/pg_config_manual.h''')
		shutit.send('./configure --prefix=/usr --enable-thread-safety --docdir=/usr/share/doc/postgresql-9.4.0')
		shutit.send('make')
		shutit.send('make install')
		shutit.send('make install-docs')
		# TODO: server http://www.linuxfromscratch.org/blfs/view/svn/server/postgresql.html
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/postgresql')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return postgresql(
		'shutit.tk.sd.postgresql.postgresql', 158844782.0255,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.tcl.tcl','shutit.tk.sd.open_ldap.open_ldap','shutit.tk.sd.linux_pam.linux_pam','shutit.tk.sd.mit_kerberos_v5.mit_kerberos_v5']
	)


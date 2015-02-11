"""ShutIt module. See http://shutit.tk
"""
#http://www.linuxfromscratch.org/blfs/view/svn/postlfs/mitkrb.html configs and context and configureation 
from shutit_module import ShutItModule


class mit_kerberos_v5(ShutItModule):

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/mit_kerberos_v5')
		shutit.send('cd /tmp/build/mit_kerberos_v5')
		shutit.send('wget -qO- http://web.mit.edu/kerberos/www/dist/krb5/1.13/krb5-1.13-signed.tar | tar -xf -')
		shutit.send('tar -zxf krb5-1.13.tar.gz')
		shutit.send('cd krb*')
		shutit.send('cd src')
		shutit.send(r'''sed -e "s@python2.5/Python.h@& python2.7/Python.h@g" -e "s@-lpython2.5]@&,\n  AC_CHECK_LIB(python2.7,main,[PYTHON_LIB=-lpython2.7])@g" -i configure.in''')
		shutit.send(r'''sed -e 's@\^u}@^u cols 300}@' -i tests/dejagnu/config/default.exp''')
		shutit.send('autoconf')
		shutit.send('./configure --prefix=/usr --sysconfdir=/etc --localstatedir=/var/lib --with-system-et --with-system-ss --with-system-verto=no --enable-dns-for-realm')
		shutit.send('make')
		shutit.send('make install')
		shutit.send('chmod -v 755 /usr/lib/libgssapi_krb5.so')
		shutit.send('chmod -v 755 /usr/lib/libgssrpc.so')
		shutit.send('chmod -v 755 /usr/lib/libk5crypto.so')
		shutit.send('chmod -v 755 /usr/lib/libkadm5clnt.so')
		shutit.send('chmod -v 755 /usr/lib/libkadm5srv.so')
		shutit.send('chmod -v 755 /usr/lib/libkdb5.so')
		#shutit.send('chmod -v 755 /usr/lib/libkdb_ldap.so') # not here? why? TODO
		shutit.send('chmod -v 755 /usr/lib/libkrad.so')
		shutit.send('chmod -v 755 /usr/lib/libkrb5.so')
		shutit.send('chmod -v 755 /usr/lib/libkrb5support.so')
		shutit.send('chmod -v 755 /usr/lib/libverto.so')
		shutit.send('mv -v /usr/lib/libkrb5.so.3* /lib')
		shutit.send('mv -v /usr/lib/libk5crypto.so.3* /lib')
		shutit.send('mv -v /usr/lib/libkrb5support.so.0* /lib')
		shutit.send('ln -v -sf ../../lib/libkrb5.so.3.3 /usr/lib/libkrb5.so')
		shutit.send('ln -v -sf ../../lib/libk5crypto.so.3.1 /usr/lib/libk5crypto.so')
		shutit.send('ln -v -sf ../../lib/libkrb5support.so.0.1 /usr/lib/libkrb5support.so')
		shutit.send('mv -v /usr/bin/ksu /bin')
		shutit.send('chmod -v 755 /bin/ksu')
		shutit.send('install -v -dm755 /usr/share/doc/krb5-1.13')
		shutit.send('cp -vfr ../doc/* /usr/share/doc/krb5-1.13')
		# Abandoned as we don't intend to actually configure kerberos or use it in anger.
		#shutit.send_host_file('/etc/krb5.conf','context/etc/krb5.conf')
		#shutit.send('kdb5_util create -r localhost -s',expect='master key:')
		#shutit.send('mypassword') # TODO: password config
		#shutit.send('kadmin.local')
		#shutit.send('add_policy dict-only')
		#shutit.send('addprinc -policy dict-only root')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/mit_kerberos_v5')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return mit_kerberos_v5(
		'shutit.tk.sd.mit_kerberos_v5.mit_kerberos_v5', 158844782.0254,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.linux_pam.linux_pam']
	)


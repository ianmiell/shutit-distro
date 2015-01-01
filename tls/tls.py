"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class tls(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/tls')
		shutit.send('cd /tmp/build/tls')
		shutit.send('wget -qO- ftp://ftp.gnutls.org/gcrypt/gnutls/v' + shutit.cfg[self.module_id]['major_version'] + '/gnutls-' + shutit.cfg[self.module_id]['major_version'] + '.' + shutit.cfg[self.module_id]['minor_version'] + '.tar.xz | xz -d | tar -xf -')
		shutit.send('cd gnutls-*')
		# Needed? Dep on version?
		shutit.send(r"sed -i -e '201 i#ifdef ENABLE_PKCS11' -e '213 i#endif' lib/gnutls_privkey.c")
		shutit.send('./configure --prefix=/usr --with-default-trust-store-file=/etc/ssl/ca-bundle.crt')
		shutit.send('make')
		shutit.send('make install')
		return True

	def get_config(self, shutit):
		shutit.get_config(self.module_id,'major_version','3.3')
		shutit.get_config(self.module_id,'minor_version','11')
		return True

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
	return tls(
		'shutit.tk.sd.tls.tls', 158844782.0080,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.nettle.nettle','shutit.tk.sd.make_certs.make_certs','shutit.tk.sd.libtasn1.libtasn1']
	)


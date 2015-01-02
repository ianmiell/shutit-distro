"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class make_certs(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/make_certs')
		shutit.send('cd /tmp/build/make_certs')
		shutit.send_host_file('/usr/bin/make-cert.pl','context/make-cert.pl')
		shutit.send_host_file('/usr/bin/make-ca.pl','context/make-ca.pl')
		shutit.send_host_file('/usr/bin/remove-expired-certs.sh','context/remove-expired-certs.sh')
		shutit.send('chmod +x /usr/bin/make-cert.pl')
		shutit.send('chmod +x /usr/bin/make-ca.pl')
		shutit.send('chmod +x /usr/bin/remove-expired-certs.sh')
		shutit.send('wget http://anduin.linuxfromscratch.org/sources/other/certdata.txt')
		shutit.send('make-ca.pl')
		shutit.send('remove-expired-certs.sh certs')
		shutit.send('install -d /etc/ssl/certs')
		shutit.send('cp -v certs/*.pem /etc/ssl/certs')
		shutit.send('c_rehash')
		shutit.send('install BLFS-ca-bundle*.crt /etc/ssl/ca-bundle.crt')
		shutit.send('ln -sfv ../ca-bundle.crt /etc/ssl/certs/ca-certificates.crt')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/make_certs')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return make_certs(
		'shutit.tk.sd.make_certs.make_certs', 158844782.00031,
		description='',
		maintainer='',
		depends=['shutit.tk.setup']
	)


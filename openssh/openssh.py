"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class openssh(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')


	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/openssh')
		shutit.send('cd /tmp/build/openssh')
		shutit.send('wget -qO- http://ftp.openbsd.org/pub/OpenBSD/OpenSSH/portable/openssh-6.7p1.tar.gz | tar -zxf -')
		shutit.send('cd openssh-*')
		shutit.send('install -v -m700 -d /var/lib/sshd')
		shutit.send('chown   -v root:sys /var/lib/sshd')
		shutit.send('groupadd -g 50 sshd')
		shutit.send('''useradd -c 'sshd PrivSep' -d /var/lib/sshd -g sshd -s /bin/false -u 50 sshd''')
		shutit.send('./configure --prefix=/usr --sysconfdir=/etc/ssh --with-md5-passwords --with-privsep-path=/var/lib/sshd')
		shutit.send('make')
		shutit.send('make install')
		shutit.send('install -v -m755 contrib/ssh-copy-id /usr/bin')
		shutit.send('install -v -m644 contrib/ssh-copy-id.1 /usr/share/man/man1')
		shutit.send('install -v -m755 -d /usr/share/doc/openssh-6.7p1')
		shutit.send('install -v -m644 INSTALL LICENCE OVERVIEW README* /usr/share/doc/openssh-6.7p1')
		return True

	def get_config(self, shutit):
		#shutit.get_config(self.module_id,'minimize',boolean=True,default=True) #TODO
		return True

	#def start(self, shutit):
	#	return True

	#def stop(self, shutit):
	#    return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/openssh')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return openssh(
		'shutit.tk.sd.openssh.openssh', 158844782.03,
		description='ssh client',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.setup']
	)


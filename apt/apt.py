"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class apt(ShutItModule):

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/apt')
		shutit.send('cd /tmp/build/apt')
		shutit.send('git clone git://anonscm.debian.org/apt/apt.git')
		shutit.send('cd apt')
		shutit.send('cp /usr/share/automake-1.15/config.guess buildlib/')
		shutit.send('cp /usr/share/automake-1.15/config.sub buildlib/')
		shutit.send('autoreconf -f -i',check_exit=False) # fails, not sure why
		shutit.send('''sed -i 's/^archset=.*/archset="x86_64-linux-gnu"/' configure # hard-code build to x86_64''')
		shutit.send('./configure --prefix=/usr')
		shutit.send('make',check_exit=False) # fails, but works when you retry (?)
		shutit.send('make') # god knows why
		shutit.send('mkdir -p /etc/apt/sources.list.d/')
		shutit.send('touch /etc/apt/sources.list')
		shutit.send('echo "deb http://http.debian.net/debian jessie main" > /etc/apt/sources.list')
		shutit.send('echo "deb http://http.debian.net/debian jessie-updates main" >> /etc/apt/sources.list')
		shutit.send('echo "deb http://security.debian.org jessie/updates main" >> /etc/apt/sources.list')
		shutit.send('mkdir -p /etc/apt/preferences.d/')
		shutit.send('mkdir -p /etc/apt/apt.conf.d/')
		shutit.send('mkdir -p /usr/lib/apt/')
		shutit.send('mkdir -p /etc/apt/trusted.gpg.d/')
#gpgv binary required as well?

# TODO: copy these from debian:jessie
#root@ef4c18bc1c54:/# ls /etc/apt/trusted.gpg.d/ 
#debian-archive-jessie-automatic.gpg	      debian-archive-jessie-stable.gpg	    debian-archive-squeeze-stable.gpg	 debian-archive-wheezy-stable.gpg
#debian-archive-jessie-security-automatic.gpg  debian-archive-squeeze-automatic.gpg  debian-archive-wheezy-automatic.gpg
		shutit.send('cd bin')
		shutit.send('cp lib* /usr/lib')
		shutit.send('cp apt* /usr/bin')
		shutit.send('cp -r methods /usr/lib/apt')
		shutit.send('cd ../include')
		shutit.send('cp -r apt-pkg /usr/include')
		#-rwxr-xr-x 1 root root     9528 Jan  8 08:27 mthdcat  #?
		#-rwxr-xr-x 1 root root    78272 Jan  8 08:27 extract-control #?
		# These files might be useful, but aren't required
		#apt: /etc/apt/apt.conf.d/01autoremove
		#apt: /etc/apt/apt.conf.d/20changelog
		#shutit.send('make install')
		return True

	#def get_config(self, shutit):
	#	return True

	#def check_ready(self, shutit):
	#	return True
	
	#def start(self, shutit):
	#	return True

	#def stop(self, shutit):
	#    return True
	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/apt')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return apt(
		'shutit.tk.sd.apt.apt', 158844782.02825,
		description='',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.curl.curl','shutit.tk.sd.xmlto.xmlto','shutit.tk.sd.berkeleydb.berkeleydb','shutit.tk.sd.git.git','shutit.tk.sd.gtest.gtest','shutit.tk.sd.dpkg.dpkg']
	)



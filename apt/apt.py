"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class apt(ShutItModule):


	def is_installed(self, shutit):
		return False


	def build(self, shutit):
#http://algebraicthunk.net/~dburrows/blog/entry/howto-get-the-apt-source-repository/
		shutit.send('mkdir -p /tmp/build/apt')
		shutit.send('cd /tmp/build/apt')
		shutit.send('git clone git://anonscm.debian.org/apt/apt.git')
		shutit.send('cd apt')
		shutit.send('cp /usr/share/automake-1.14/config.guess buildlib/')
		shutit.send('cp /usr/share/automake-1.14/config.sub buildlib/')
		shutit.send('autoreconf -f -i') # don't think this is needed
#checking debian architecture... ./configure: line 4975: dpkg-architecture: command not found
#configure: error: failed: use --host= or output from dpkg-architecture
# hard-code line 4975 to amd64(?)
#archset="x86_64-linux-gnu"
		shutit.send('''sed -i 's/^archset=.*/archset="x86_64-linux-gnu"/' configure''')
		shutit.send('./configure --prefix=/usr')
		shutit.send('make')
		shutit.pause_point('')
# copy the bin objects to lib
#imiell@lp01728:/space/git/dockerbook$ apt-file show apt | grep ^apt:
#apt: /etc/apt/apt.conf.d/01autoremove
#apt: /etc/apt/apt.conf.d/20changelog
#apt: /etc/cron.daily/apt
#apt: /etc/kernel/postinst.d/apt-auto-removal
#apt: /etc/logrotate.d/apt
#apt: /usr/bin/apt-cache
#apt: /usr/bin/apt-cdrom
#apt: /usr/bin/apt-config
#apt: /usr/bin/apt-get
#apt: /usr/bin/apt-key
#apt: /usr/bin/apt-mark
#apt: /usr/lib/apt/methods/bzip2
#apt: /usr/lib/apt/methods/cdrom
#apt: /usr/lib/apt/methods/copy
#apt: /usr/lib/apt/methods/file
#apt: /usr/lib/apt/methods/ftp
#apt: /usr/lib/apt/methods/gpgv
#apt: /usr/lib/apt/methods/gzip
#apt: /usr/lib/apt/methods/http
#apt: /usr/lib/apt/methods/lzma
#apt: /usr/lib/apt/methods/mirror
#apt: /usr/lib/apt/methods/rred
#apt: /usr/lib/apt/methods/rsh
#apt: /usr/lib/apt/methods/ssh
#apt: /usr/lib/apt/methods/xz
#apt: /usr/lib/dpkg/methods/apt/desc.apt
#apt: /usr/lib/dpkg/methods/apt/install
#apt: /usr/lib/dpkg/methods/apt/names
#apt: /usr/lib/dpkg/methods/apt/setup
#apt: /usr/lib/dpkg/methods/apt/update
#apt: /usr/share/apt/ubuntu-archive.gpg
#apt: /usr/share/bug/apt/script

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


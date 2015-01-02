"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class cups(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/cups')
		shutit.send('cd /tmp/build/cups')
		shutit.send('wget -qO- http://www.cups.org/software/1.7.5/cups-1.7.5-source.tar.bz2 | bunzip2 -c | tar -xf -')
		shutit.send('cd cups*')
		shutit.send('useradd -c "Print Service User" -d /var/spool/cups -g lp -s /bin/false -u 9 lp') # already there
		shutit.send('groupadd -g 19 lpadmin')
		shutit.send('''sed -i 's#@CUPS_HTMLVIEW@#firefox#' desktop/cups.desktop.in''')
		shutit.send('curl -L http://www.linuxfromscratch.org/patches/blfs/7.6/cups-1.7.5-content_type-1.patch | patch -Np1 -i -')
		shutit.send('curl -L http://www.linuxfromscratch.org/patches/blfs/7.6/cups-1.7.5-blfs-1.patch | patch -Np1 -i -')
		shutit.send('aclocal -I config-scripts')
		shutit.send('autoconf -I config-scripts')
		shutit.send('CC=gcc ./configure --libdir=/usr/lib --with-rcdir=/tmp/cupsinit --with-docdir=/usr/share/cups/doc --with-system-groups=lpadmin')
		shutit.send('make')
		shutit.send('make install')
		shutit.send('rm -rf /tmp/cupsinit')
		shutit.send('ln -svfn ../cups/doc /usr/share/doc/cups-1.7.5')
		shutit.send('echo "ServerName /var/run/cups/cups.sock" > /etc/cups/client.conf')
		shutit.send('rm -rf /usr/share/cups/banners')
		shutit.send('rm -rf /usr/share/cups/data/testprint')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	#def start(self, shutit):
	#	return True

	#def stop(self, shutit):
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/cups')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return cups(
		'shutit.tk.sd.cups.cups', 158844782.0108,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.libgcrypt.libgcrypt']
	)


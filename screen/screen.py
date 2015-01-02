"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class screen(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/screen')
		shutit.send('cd /tmp/build/screen')
		shutit.send('wget -qO- http://ftp.gnu.org/gnu/screen/screen-4.2.1.tar.gz | tar -zxf -')
		shutit.send('cd screen*')
		shutit.send('./configure --prefix=/usr --infodir=/usr/share/info --mandir=/usr/share/man --with-socket-dir=/run/screen --with-pty-group=5 --with-sys-screenrc=/etc/screenrc')
		shutit.send('sed -i -e "s%/usr/local/etc/screenrc%/etc/screenrc%" {etc,doc}/*')
		shutit.send('make')
		shutit.send('make install')
		shutit.send('install -m 644 etc/etcscreenrc /etc/screenrc')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/screen')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return screen(
		'shutit.tk.sd.screen.screen', 158844782.0237,
		description='',
		maintainer='',
		depends=['shutit.tk.setup']
	)


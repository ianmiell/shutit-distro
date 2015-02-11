"""ShutIt module. See http://shutit.tk
"""
from shutit_module import ShutItModule


class xterm(ShutItModule):

	def build(self, shutit):
		import sd_util
		sd_util.setup_x_environment(shutit)
		shutit.send('mkdir -p /tmp/build/xterm')
		shutit.send('cd /tmp/build/xterm')
		shutit.send('wget -qO- ftp://invisible-island.net/xterm/xterm-314.tgz | tar -zxf -')
		shutit.send('mkdir -p /etc/X11/app-defaults')
		shutit.send_host_file('/etc/X11/app-defaults/XTerm','context/etc/X11/app-defaults/XTerm')
		shutit.send('cd xterm*')
		shutit.send('''sed -i '/v0/{n;s/new:/new:kb=^?:/}' termcap''')
		shutit.send(r'''printf '\tkbs=\\177,\n' >> terminfo''')
		shutit.send('TERMINFO=/usr/share/terminfo')
		shutit.send('./configure $XORG_CONFIG --with-app-defaults=/etc/X11/app-defaults')
		shutit.send('make')
		shutit.send('make install')
		shutit.send('make install-ti')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/xterm')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return xterm(
		'shutit.tk.sd.xterm.xterm', 158844782.0261,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.xorg_apps.xorg_apps']
	)


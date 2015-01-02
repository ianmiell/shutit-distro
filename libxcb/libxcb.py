"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class libxcb(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		import sd_util
		sd_util.setup_x_environment(shutit)
		shutit.send('mkdir -p /tmp/build/libxcb')
		shutit.send('cd /tmp/build/libxcb')
		shutit.send('wget -qO- http://xcb.freedesktop.org/dist/libxcb-1.11.tar.bz2 | bunzip2 -c | tar -xf -')
		shutit.send('cd libxcb*')
		shutit.send('sed "s/pthread-stubs//" -i configure')
		shutit.send('''./configure $XORG_CONFIG --enable-xinput --docdir='${datadir}'/doc/libxcb-1.11''')
		shutit.send('make')
		shutit.send('make install')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/libxcb')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return libxcb(
		'shutit.tk.sd.libxcb.libxcb', 158844782.0087,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.libxau.libxau','shutit.tk.sd.xcb_proto.xcb_proto']
	)


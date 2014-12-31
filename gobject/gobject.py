"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class gobject(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/gobject')
		shutit.send('cd /tmp/build/gobject')
		shutit.send('wget -qO- http://ftp.gnome.org/pub/gnome/sources/gobject-introspection/1.40/gobject-introspection-1.40.0.tar.xz | xz -d | tar -xf -')	
		shutit.send('cd gobject*')
		shutit.send('./configure --prefix=/usr --disable-static')
		shutit.send('make')
		shutit.send('make install')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

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
	return gobject(
		'shutit.tk.sd.gobject.gobject', 158844782.00955,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.glib.glib']
	)


"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class glib(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/glib')
		shutit.send('cd /tmp/build/glib')
		shutit.send('wget -qO- http://ftp.gnome.org/pub/gnome/sources/glib/2.40/glib-2.40.0.tar.xz | xz -d | tar -xf -')
		shutit.send('cd glib*')
		shutit.send('./configure --prefix=/usr --with-pcre=system')
		shutit.send('make')
		shutit.send('make install')
		# Remove old glib.so's to avoid confusion (eg atk and pango breaks later otherwise)
		#shutit.send('rm -f /lib/x86_64-linux-gnu/libglib-2.0.so.0 /usr/lib/x86_64-linux-gnu/libgio-2.0.a /usr/lib/x86_64-linux-gnu/libgio-2.0.so')
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
	return glib(
		'shutit.tk.sd.glib.glib', 158844782.0091,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.python2.python2','shutit.tk.sd.pcre.pcre']
	)


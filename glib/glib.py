"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class glib(ShutItModule):

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/glib')
		shutit.send('cd /tmp/build/glib')
		shutit.send('wget -qO- http://ftp.gnome.org/pub/gnome/sources/glib/2.40/glib-2.40.0.tar.xz | xz -d | tar -xf -')
		shutit.send('cd glib*')
		shutit.send('./configure --prefix=/usr --with-pcre=system')
		shutit.send('make')
		shutit.send('make install')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/glib')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return glib(
		'shutit.tk.sd.glib.glib', 158844782.0091,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.pcre.pcre']
	)


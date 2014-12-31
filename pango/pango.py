"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class pango(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/pango')
		shutit.send('cd /tmp/build/pango')
		shutit.send('wget -qO- http://ftp.gnome.org/pub/gnome/sources/pango/1.36/pango-1.36.7.tar.xz | xz -d | tar -xf -')
		shutit.send('cd pango*')
		shutit.send('./configure --prefix=/usr --sysconfdir=/etc')
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
	return pango(
		'shutit.tk.sd.pango.pango', 158844782.0119,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.cairo.cairo','shutit.tk.sd.harfbuzz.harfbuzz','shutit.tk.sd.xorg_libs.xorg_libs','shutit.tk.sd.freetype2.freetype2','shutit.tk.sd.glib.glib','shutit.tk.sd.gobject.gobject']
	)


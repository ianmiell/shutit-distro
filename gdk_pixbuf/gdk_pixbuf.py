"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class gdk_pixbuf(ShutItModule):

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/gdk_pixbuf')
		shutit.send('cd /tmp/build/gdk_pixbuf')
		shutit.send('wget -qO- http://ftp.gnome.org/pub/gnome/sources/gdk-pixbuf/2.30/gdk-pixbuf-2.30.8.tar.xz | xz -d | tar -xf -')
		shutit.send('cd gdk-pixbuf*')
		shutit.send('./configure --prefix=/usr --with-x11') # --with-x11?
		shutit.send('make')
		shutit.send('make install')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/gdk_pixbuf')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return gdk_pixbuf(
		'shutit.tk.sd.gdk_pixbuf.gdk_pixbuf', 158844782.01195,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.glib.glib','shutit.tk.sd.libjpeg.libjpeg','shutit.tk.sd.libpng.libpng','shutit.tk.sd.libtiff.libtiff','shutit.tk.sd.xorg_libs.xorg_libs','shutit.tk.sd.gobject.gobject']
	)


"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class cairo(ShutItModule):

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/cairo')
		shutit.send('cd /tmp/build/cairo')
		shutit.send('wget -qO- http://cairographics.org/releases/cairo-1.12.16.tar.xz | xz -d | tar -xf -')
		shutit.send('cd cairo*')
		shutit.send('CFLAGS="$CFLAGS -ffat-lto-objects" ./configure --prefix=/usr     --disable-static --enable-tee')
		shutit.send('make')
		shutit.send('make install')
		return True

	def is_installed(self,shutit):
		return False
	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/cairo')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return cairo(
		'shutit.tk.sd.cairo.cairo', 158844782.0117,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.libpng.libpng','shutit.tk.sd.glib.glib','shutit.tk.sd.pixman.pixman']
	)


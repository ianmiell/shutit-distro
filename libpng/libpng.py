"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class libpng(ShutItModule):

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/libpng')
		shutit.send('cd /tmp/build/libpng')
		shutit.send('wget -qO- http://downloads.sourceforge.net/libpng/libpng-1.6.13.tar.xz | xz -d | tar -xf -')
		shutit.send('cd libpng*')
		shutit.send('wget -QO- http://downloads.sourceforge.net/libpng-apng/libpng-1.6.13-apng.patch.gz | patch -p1 -')
		shutit.send('./configure --prefix=/usr --disable-static')
		shutit.send('make')
		shutit.send('make install')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/libpng')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return libpng(
		'shutit.tk.sd.libpng.libpng', 158844782.0084,
		description='',
		maintainer='',
		depends=['shutit.tk.setup']
	)


"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class libmng(ShutItModule):

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/libmng')
		shutit.send('cd /tmp/build/libmng')
		shutit.send('wget -qO- http://downloads.sourceforge.net/libmng/libmng-2.0.2.tar.xz | xz -d | tar -xf -')
		shutit.send('cd libmng*')
		shutit.send(r'''sed -i "s:#include <jpeg:#include <stdio.h>\n&:" libmng_types.h''')
		shutit.send('./configure --prefix=/usr --disable-static')
		shutit.send('make')
		shutit.send('make install')
		shutit.send('install -v -m755 -d /usr/share/doc/libmng-2.0.2')
		shutit.send('install -v -m644 doc/*.txt /usr/share/doc/libmng-2.0.2')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/libmng')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return libmng(
		'shutit.tk.sd.libmng.libmng', 158844782.012101,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.lcms.lcms']
	)


"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class fontconfig(ShutItModule):

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/fontconfig')
		shutit.send('cd /tmp/build/fontconfig')
		shutit.send('wget -qO- http://www.freedesktop.org/software/fontconfig/release/fontconfig-2.11.1.tar.bz2 | bunzip2 -c | tar -xf -')
		shutit.send('cd fontconfig*')
		shutit.send('./configure --prefix=/usr --sysconfdir=/etc --localstatedir=/var --disable-docs --docdir=/usr/share/doc/fontconfig-2.11.1')
		shutit.send('make')
		shutit.send('make install')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/fontconfig')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return fontconfig(
		'shutit.tk.sd.fontconfig.fontconfig', 158844782.01,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.freetype2_pre_harfbuzz.freetype2_pre_harfbuzz']
	)


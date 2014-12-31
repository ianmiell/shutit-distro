"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class freetype2_pre_harfbuzz(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/freetype2_pre_harfbuzz')
		shutit.send('cd /tmp/build/freetype2_pre_harfbuzz')
		shutit.send('wget -qO- http://downloads.sourceforge.net/freetype/freetype-2.5.3.tar.bz2 | bunzip2 -c | tar -xf -')
		shutit.send('cd freetype*')
		#tar -xf ../freetype-doc-2.5.4.tar.bz2 --strip-components=2 -C docs
		shutit.send('sed -i  -e "/AUX.*.gxvalid/s@^# @@" -e "/AUX.*.otvalid/s@^# @@" modules.cfg')
		shutit.send(r'''sed -ri -e 's:.*(#.*SUBPIXEL.*) .*:\1:' include/config/ftoption.h''')
		shutit.send('./configure --prefix=/usr --disable-static --without-harfbuzz')
		shutit.send('make')
		shutit.send('make install')
		#install -v -m755 -d /usr/share/doc/freetype-2.5.4 &&
		#cp -v -R docs/*     /usr/share/doc/freetype-2.5.4
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
	return freetype2_pre_harfbuzz(
		'shutit.tk.sd.freetype2_pre_harfbuzz.freetype2_pre_harfbuzz', 158844782.0098,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.which.which','shutit.tk.sd.libpng.libpng']
	)


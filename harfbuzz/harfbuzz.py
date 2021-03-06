"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class harfbuzz(ShutItModule):

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/harfbuzz')
		shutit.send('cd /tmp/build/harfbuzz')
		shutit.send('wget -qO- http://www.freedesktop.org/software/harfbuzz/release/harfbuzz-0.9.35.tar.bz2 | bunzip2 -c | tar -xf -')
		shutit.send('cd harfbuzz*')
		shutit.send('./configure --prefix=/usr --with-gobject')
		shutit.send('make')
		shutit.send('make install')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/harfbuzz')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return harfbuzz(
		'shutit.tk.sd.harfbuzz.harfbuzz', 158844782.00985,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.icu.icu','shutit.tk.sd.gobject.gobject','shutit.tk.sd.freetype2_pre_harfbuzz.freetype2_pre_harfbuzz']
	)


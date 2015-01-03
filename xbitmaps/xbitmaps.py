"""ShutIt module. See http://shutit.tk
"""
from shutit_module import ShutItModule


class xbitmaps(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		import sd_util
		sd_util.setup_x_environment(shutit)
		shutit.send('mkdir -p /tmp/build/xbitmaps')
		shutit.send('cd /tmp/build/xbitmaps')
		shutit.send('wget -qO- http://xorg.freedesktop.org/archive/individual/data/xbitmaps-1.1.1.tar.bz2 | bunzip2 -c | tar -xf -')
		shutit.send('cd xbitmaps-*')
		shutit.send('./configure $XORG_CONFIG')
		shutit.send('make install')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/xbitmaps')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return xbitmaps(
		'shutit.tk.sd.xbitmaps.xbitmaps', 158844782.0258,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.util_macros.util_macros']
	)


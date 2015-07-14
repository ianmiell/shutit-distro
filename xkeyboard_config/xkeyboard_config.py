"""ShutIt module. See http://shutit.tk
"""
from shutit_module import ShutItModule


class xkeyboard_config(ShutItModule):

	def build(self, shutit):
		import sd_util
		sd_util.setup_x_environment(shutit)
		shutit.send('mkdir -p /tmp/build/xkeyboard_config')
		shutit.send('cd /tmp/build/xkeyboard_config')
		shutit.get_url('xkeyboard-config-2.14.tar.bz2',['http://xorg.freedesktop.org/archive/individual/data/xkeyboard-config'])
		shutit.send('bunzip2 -c xkeyboard-config-2.14.tar.bz2 | tar -xf -')
		shutit.send('cd xkeyboard*')
		shutit.send('./configure $XORG_CONFIG --with-xkb-rules-symlink=xorg')
		shutit.send('make')
		shutit.send('make install')
		return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/xkeyboard_config')
		return True


def module():
	return xkeyboard_config(
		'shutit.tk.sd.xkeyboard_config.xkeyboard_config', 158844782.02603,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.xcursor_themes.xcursor_themes']
	)


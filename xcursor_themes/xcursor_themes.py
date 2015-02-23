"""ShutIt module. See http://shutit.tk
"""
from shutit_module import ShutItModule


class xcursor_themes(ShutItModule):

	def build(self, shutit):
		import sd_util
		sd_util.setup_x_environment(shutit)
		shutit.send('mkdir -p /tmp/build/xcursor_themes')
		shutit.send('cd /tmp/build/xcursor_themes')
		shutit.get_url('xcursor-themes-1.0.4.tar.bz2',['http://xorg.freedesktop.org/archive/individual/data'])
		shutit.send('bunzip2 -c xcursor-themes-1.0.4.tar.bz2 | tar -xf -')
		shutit.send('cd xcursor*')
		shutit.send('./configure $XORG_CONFIG')
		shutit.send('make')
		shutit.send('make install')
		return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/xcursor_themes')
		return True


def module():
	return xcursor_themes(
		'shutit.tk.sd.xcursor_themes.xcursor_themes', 158844782.02601,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.xcursor_gen.xcursor_gen']
	)


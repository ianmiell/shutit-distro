"""ShutIt module. See http://shutit.tk
"""
from shutit_module import ShutItModule


class xcursor_gen(ShutItModule):

	def build(self, shutit):
		import sd_util
		sd_util.setup_x_environment(shutit)
		shutit.send('mkdir -p /tmp/build/xcursor_gen')
		shutit.send('cd /tmp/build/xcursor_gen')
		shutit.get_url('xcursorgen-1.0.6.tar.bz2',['http://xorg.freedesktop.org/releases/individual/app'])
		shutit.send('bunzip2 -c xcursorgen-1.0.6.tar.bz2 | tar -xf -')
		shutit.send('cd xcursorgen*')
		shutit.send('./configure $XORG_CONFIG')
		shutit.send(' make')
		shutit.send('make install')
		return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/xcursor_gen')
		return True


def module():
	return xcursor_gen(
		'shutit.tk.sd.xcursor_gen.xcursor_gen', 158844782.026009,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.xorg_apps.xorg_apps']
	)


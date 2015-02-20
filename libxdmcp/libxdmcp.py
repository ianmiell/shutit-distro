"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule

class libxdmcp(ShutItModule):

	def build(self, shutit):
		import sd_util
		sd_util.setup_x_environment(shutit)
		shutit.send('mkdir -p /tmp/build/libxdmcp')
		shutit.send('cd /tmp/build/libxdmcp')
		shutit.get_url('libXdmcp-1.1.1.tar.bz2',['http://xorg.freedesktop.org/releases/individual/lib'])
		shutit.send('bunzip2 -c libXdmcp-1.1.1.tar.bz2 | tar -xf -')
		shutit.send('cd libX*')
		shutit.send('./configure $XORG_CONFIG')
		shutit.send('make')
		shutit.send('make install')
		return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/libxdmcp')
		return True

def module():
	return libxdmcp(
		'shutit.tk.sd.libxdmcp.libxdmcp', 158844782.008201,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.x7proto.x7proto']
	)


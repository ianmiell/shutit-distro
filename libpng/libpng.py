"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class libpng(ShutItModule):

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/libpng')
		shutit.send('cd /tmp/build/libpng')
		f = 'libpng-1.6.13.tar.xz'
		shutit.get_url(f,['http://ftp.osuosl.org/pub/blfs/conglomeration/libpng','http://downloads.sourceforge.net/libpng'])
		shutit.send('xz -d ' + f + '| tar -xf -')
		shutit.send('cd libpng*')
		shutit.send('wget -QO- http://downloads.sourceforge.net/libpng-apng/libpng-1.6.13-apng.patch.gz | patch -p1 -')
		shutit.send('./configure --prefix=/usr --disable-static')
		shutit.send('make')
		shutit.send('make install')
		return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/libpng')
		return True

def module():
	return libpng(
		'shutit.tk.sd.libpng.libpng', 158844782.0084,
		description='',
		maintainer='',
		depends=['shutit.tk.setup']
	)


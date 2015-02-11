"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class giflib(ShutItModule):

	def build(self, shutit):
		#www.linuxfromscratch.org/blfs/view/svn/general/giflib.html
		shutit.send('mkdir -p /tmp/build/giflib')
		shutit.send('cd /tmp/build/giflib')
		shutit.send('wget -qO- http://downloads.sourceforge.net/giflib/giflib-5.1.0.tar.bz2 | bunzip2 -c | tar -xf -')
		shutit.send('cd giflib*')
		shutit.send('./configure --prefix=/usr --disable-static')
		shutit.send('make')
		shutit.send('make install')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/giflib')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return giflib(
		'shutit.tk.sd.giflib.giflib', 158844782.0057,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.xmlto.xmlto']
	)


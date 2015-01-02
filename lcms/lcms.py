"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class lcms(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/lcms')
		shutit.send('cd /tmp/build/lcms')
		shutit.send('wget -qO- http://downloads.sourceforge.net/lcms/lcms2-2.6.tar.gz | tar -zxf -')
		shutit.send('cd lcms*')
		shutit.send('./configure --prefix=/usr --disable-static')
		shutit.send('make')
		shutit.send('make install')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/lcms')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return lcms(
		'shutit.tk.sd.lcms.lcms', 158844782.0121,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.libjpeg.libjpeg','shutit.tk.sd.libtiff.libtiff']
	)


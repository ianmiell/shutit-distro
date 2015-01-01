"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class libtiff(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/libtiff')
		shutit.send('cd /tmp/build/libtiff')
		shutit.send('wget -qO- http://download.osgeo.org/libtiff/tiff-4.0.3.tar.gz | tar -zxf -')
		shutit.send('cd tiff*')
		shutit.send('''sed -i '/glDrawPixels/a glFlush();' tools/tiffgt.c''')
		shutit.send('./configure --prefix=/usr --disable-static')
		shutit.send('make')
		shutit.send('make install')
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
	return libtiff(
		'shutit.tk.sd.libtiff.libtiff', 158844782.0114,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.libjpeg.libjpeg']
	)


"""ShutIt module. See http://shutit.tk/
"""

from shutit_module import ShutItModule


class curl(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')


	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/curl')
		shutit.send('cd /tmp/build/curl')
		shutit.send('wget -qO- --no-check-certificate http://curl.haxx.se/download/curl-7.39.0.tar.gz | tar -zxf -')
		shutit.send('cd curl-*')
		shutit.send('./configure --prefix=/usr --disable-static --enable-threaded-resolver')
		shutit.send('make')
		shutit.send('make install')
		shutit.send('find docs \( -name "Makefile*" -o -name "*.1" -o -name "*.3" \) -exec rm {} \;')
		shutit.send('install -v -d -m755 /usr/share/doc/curl-7.39.0')
		shutit.send('cp -v -R docs/*     /usr/share/doc/curl-7.39.0')
		return True

	#def get_config(self, shutit):
	#	return True

	#def check_ready(self, shutit):
	#	return True
	
	#def start(self, shutit):
	#	return True

	#def stop(self, shutit):
	#	return True

	def finalize(self, shutit):
		#shutit.send('rm -rf
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return curl(
		'shutit.tk.sd.curl.curl', 158844782.00115,
		description='curl built from source',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.pkg_config.pkg_config']
	)


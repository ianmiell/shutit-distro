"""ShutIt module. See http://shutit.tk/
"""

from shutit_module import ShutItModule


class zip(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')


	def build(self, shutit):
		#http://www.info-zip.org/Zip.html 
		shutit.send('mkdir -p /tmp/build/zip')
		shutit.send_host_file('/tmp/build/zip/unzip60.tar.xz','context/unzip60.tar.xz')
		shutit.send('cd /tmp/build/zip')
		shutit.send('xz -d unzip60.tar.xz')
		shutit.send('tar -xf unzip60.tar')
		shutit.send('cd unzip60')
		shutit.send('make -f unix/Makefile IZ_BZIP2=/opt/bzip2/bzip2-1.0.6 IZ_ZLIB=../../zlib/zlib-1.2.5 generic')
		shutit.send('make -f unix/Makefile install')

		shutit.send('cd /tmp/build/zip')
		shutit.send('wget -O- http://downloads.sourceforge.net/infozip/zip30.tar.gz | tar -zxf -')
		shutit.send('cd zip30')
		shutit.send('make -f unix/Makefile generic_gcc')
		shutit.send('make prefix=/usr MANDIR=/usr/share/man/man1 -f unix/Makefile install')
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
	return zip(
		'shutit.tk.sd.zip.zip', 158844782.00245,
		description='',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.pkg_config.pkg_config']
	)


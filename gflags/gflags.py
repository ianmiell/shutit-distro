"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class gflags(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/gflags')
		shutit.send('cd /tmp/build/gflags')
		shutit.send('wget -qO- https://gflags.googlecode.com/files/gflags-2.0.tar.gz | tar -zxf -')
		shutit.send('cd gflags*')
		shutit.send('mkdir build')
		shutit.send('cd build')
		shutit.send('./configure --prefix=/usr')
		#shutit.send('cmake ..')
		#shutit.send(r'''sed -i 's/\/usr\/local/\/usr/g' cmake_install.cmake''')
		shutit.send('make')
		shutit.send('make install')
		return True

	def get_config(self, shutit):
		return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/gflags')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return gflags(
		'shutit.tk.sd.gflags.gflags', 158844782.0264,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.make_certs.make_certs','shutit.tk.sd.cmake.cmake']
	)


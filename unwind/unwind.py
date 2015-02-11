"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class unwind(ShutItModule):

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/unwind')
		shutit.send('cd /tmp/build/unwind')
		shutit.get_url('libunwind-1.1.tar.gz',['http://download.savannah.gnu.org/releases/libunwind'])
		shutit.send('tar -zxf libunwind-1.1.tar.gz')
		shutit.send('rm -f libunwind-1.1.tar.gz')
		shutit.send('cd libunwind-*')
		shutit.send('./configure --prefix=/usr')
		#shutit.send('cmake ..')
		#shutit.send(r'''sed -i 's/\/usr\/local/\/usr/g' cmake_install.cmake''')
		shutit.send('make')
		shutit.send('make install')
		return True

	def get_config(self, shutit):
		return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/unwind')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return unwind(
		'shutit.tk.sd.unwind.unwind', 158844782.028915,
		description='',
		maintainer='',
		depends=['shutit.tk.setup']
	)


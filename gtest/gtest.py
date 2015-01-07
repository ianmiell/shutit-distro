"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class gtest(ShutItModule):


	def is_installed(self, shutit):
		return False


	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/gtest')
		shutit.send('cd /tmp/build/gtest')
		shutit.send('wget http://googletest.googlecode.com/files/gtest-1.7.0.zip')
		shutit.send('unzip gtest-1.7.0.zip')
		shutit.send('rm gtest-1.7.0.zip')
		shutit.send('cd gtest-1.7.0')
		shutit.send('./configure')
		shutit.send('make')
		shutit.send('cp -a include/gtest /usr/include')
		shutit.send('cp -a lib/.libs/* /usr/lib/')
		shutit.send('ldconfig -v #gTestframework is now ready to use. Just don\'t forget to link your project against the library by setting -lgtest as linker flag and optionally, if you did not write your own test mainroutine, the explicit -lgtest_main flag.')
		return True

	#def get_config(self, shutit):
	#	return True

	#def check_ready(self, shutit):
	#	return True
	
	#def start(self, shutit):
	#	return True

	#def stop(self, shutit):
	#    return True
	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/gtest')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return gtest(
		'shutit.tk.sd.gtest.gtest', 158844782.028225,
		description='',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.setup']
	)


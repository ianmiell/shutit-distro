"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class osquery(ShutItModule):


	def is_installed(self, shutit):
		return False


	def build(self, shutit):
#DONE? shutit.install('libgoogle-glog-dev')
#DONE? shutit.install('librpm-dev')
#DONE? shutit.install('libsnappy-dev')
#DONE? shutit.install('libprocps3-dev')
#DONE? shutit.install('libunwind8-dev')
#DONE? shutit.install('libblkid-dev')
#DONE? shutit.install('libudev-dev')
#DONE? shutit.install('uuid-dev')
#DONE? shutit.install('libssl-dev')
#DONE? shutit.install('libbz2-dev')
		shutit.send('pip install jinja2')
		shutit.send('export CPATH=/usr/lib/x86_64-linux-gnu:/opt/rocksdb/include')
		shutit.send('export LIBRARY_PATH=/usr/local/lib')
		shutit.send('cd /opt')
		shutit.send('git clone https://github.com/facebook/osquery.git')
		shutit.send('cd /opt/osquery')
		shutit.send('git submodule init')
		shutit.send('git submodule update')
		shutit.send('make')
		return True

	#def get_config(self, shutit):
	#	return True

	#def check_ready(self, shutit):
	#	return True
	
	#def start(self, shutit):
	#	return True

	#def stop(self, shutit):
	#    return True
	#def finalize(self, shutit):
	#	return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return osquery(
		'shutit.tk.osquery.osquery', 158844782.028,
		description='Facebook\'s OSQuery sql tool',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.git.git','shutit.tk.sd.qt4.qt4','shutit.tk.sd.sqlite.sqlite','shutit.tk.sd.python_pip.python_pip','shutit.tk.sd.libevent.libevent','shutit.tk.sd.boost.boost','shutit.tk.sd.libgoogle_glog.libgoogle_glog','shutit.tk.sd.rpm.rpm','shutit.tk.sd.libsnappy.libsnappy','shutit.tk.sd.cmake.cmake','shutit.tk.sd.doxygen.doxygen']
	)


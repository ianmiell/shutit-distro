"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class osquery(ShutItModule):

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/osquery')
		shutit.send('cd /tmp/build/osquery')
		shutit.send('pip install jinja2')
		shutit.send('git clone https://github.com/facebook/osquery.git')
		shutit.send('cd osquery')
		shutit.send('git submodule init')
		shutit.send('git submodule update')
		shutit.send('make')
		shutit.send('make install')
		return True

	def get_config(self, shutit):
		#shutit.get_config(self.module_id,'minimize',boolean=True,default=True) #TODO
		return True

	#def start(self, shutit):
	#	return True

	#def stop(self, shutit):
	#    return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/osquery')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return osquery(
		'shutit.tk.sd.osquery.osquery', 158844782.029,
		description='Facebook\'s OSQuery sql tool',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.git.git','shutit.tk.sd.qt4.qt4','shutit.tk.sd.sqlite.sqlite','shutit.tk.sd.python_pip.python_pip','shutit.tk.sd.libevent.libevent','shutit.tk.sd.boost.boost','shutit.tk.sd.libgoogle_glog.libgoogle_glog','shutit.tk.sd.rpm.rpm','shutit.tk.sd.libsnappy.libsnappy','shutit.tk.sd.cmake.cmake','shutit.tk.sd.doxygen.doxygen','shutit.tk.sd.rocksdb.rocksdb','shutit.tk.sd.thrift.thrift','shutit.tk.sd.dpkg.dpkg','shutit.tk.sd.unwind.unwind','shutit.tk.sd.apt.apt','shutit.tk.sd.lsb_release.lsb_release']
	)


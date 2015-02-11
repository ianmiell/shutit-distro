"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class rocksdb(ShutItModule):

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/rocksdb')
		shutit.send('cd /tmp/build/rocksdb')
		shutit.send('git clone https://github.com/facebook/rocksdb.git')
		shutit.send('cd rocksdb')
		shutit.send('make')
		shutit.send('make all')
		shutit.send('make install')
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
		shutit.send('rm -rf /tmp/build/rocksdb')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return rocksdb(
		'shutit.tk.sd.rocksdb.rocksdb', 158844782.0265,
		description='Facebook\'s rocksdb',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.git.git','shutit.tk.sd.gflags.gflags']
	)


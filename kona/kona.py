"""ShutIt module. See http://shutit.tk/
"""

from shutit_module import ShutItModule


class kona(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')


	def build(self, shutit):
		shutit.send('cd /tmp/build')
		shutit.send('git clone https://github.com/kevinlawler/kona.git')
		shutit.send('cd kona')
		shutit.send('make')
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
	#def finalize(self, shutit):
	#	return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return kona(
		'shutit.tk.sd.kona.kona', 158844782.0228,
		description='Open source K interpreter',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.git.git','shutit.tk.sd.libxslt.libxslt']
	)


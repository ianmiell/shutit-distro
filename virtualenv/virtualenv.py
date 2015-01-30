"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class virtualenv(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')


	def build(self, shutit):
		shutit.send('pip install virtualenv')
		return True

	def get_config(self, shutit):
		return True

	#def start(self, shutit):
	#	return True

	#def stop(self, shutit):
	#    return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/virtualenv')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return virtualenv(
		'shutit.tk.sd.virtualenv.virtualenv', 158844782.0311,
		description='python virtualenv',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.python_pip.python_pip']
	)


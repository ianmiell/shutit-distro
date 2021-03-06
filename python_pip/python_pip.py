"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class python_pip(ShutItModule):

	def build(self, shutit):
		shutit.send('python --version')
		shutit.send('wget -qO- https://bootstrap.pypa.io/get-pip.py | python')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return python_pip(
		'shutit.tk.sd.python_pip.python_pip', 158844782.0068,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.make_certs.make_certs']
	)


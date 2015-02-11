"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class rhc(ShutItModule):

	def build(self, shutit):
		shutit.send('gem install rhc')
		return True

	def get_config(self, shutit):
		return True

	#def start(self, shutit):
	#	return True

	#def stop(self, shutit):
	#    return True

	def finalize(self, shutit):
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return rhc(
		'shutit.tk.sd.rhc.rhc', 158844782.0318,
		description='RedHat OpenShift Client tool',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.ruby.ruby']
	)


"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class docl(ShutItModule):

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/docl')
		shutit.send('cd /tmp/build/docl')
		shutit.send('gem install docl')
		return True

	def get_config(self, shutit):
		return True

	#def start(self, shutit):
	#	return True

	#def stop(self, shutit):
	#    return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/docl')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return docl(
		'shutit.tk.sd.docl.docl', 158844782.03046,
		description='docl',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.ruby.ruby','shutit.tk.sd.make_certs.make_certs','shutit.tk.sd.git.git']
	)


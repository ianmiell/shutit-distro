"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class docl(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')


	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/docl')
		shutit.send('cd /tmp/build/docl')
		return True

	def get_config(self, shutit):
		#shutit.get_config(self.module_id,'minimize',boolean=True,default=True) #TODO
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


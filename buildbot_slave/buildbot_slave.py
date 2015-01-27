"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class buildbot_slave(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')


	def build(self, shutit):
		shutit.send('pip install buildbot_slave')
		return True

	def get_config(self, shutit):
		return True

	#def start(self, shutit):
	#	return True

	#def stop(self, shutit):
	#    return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/buildbot_slave')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return buildbot_slave(
		'shutit.tk.sd.buildbot_slave.buildbot_slave', 158844782.0315,
		description='python buildbot slave',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.virtualenv.virtualenv']
	)


"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class buildbot_master(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')


	def build(self, shutit):
		shutit.send('pip install buildbot_master')
		return True

	def get_config(self, shutit):
		return True

	#def start(self, shutit):
	#	return True

	#def stop(self, shutit):
	#    return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/buildbot_master')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return buildbot_master(
		'shutit.tk.sd.buildbot_master.buildbot_master', 158844782.0314,
		description='python buildbot master',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.virtualenv.virtualenv']
	)


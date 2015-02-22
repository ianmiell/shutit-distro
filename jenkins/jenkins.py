"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class jenkins(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')


	def build(self, shutit):
		shutit.send('cd /opt')
		shutit.send('wget http://mirrors.jenkins-ci.org/war/1.598/jenkins.war')
		shutit.send('chmod 644 /opt/jenkins.war')
		shutit.add_to_bashrc('export JENKINS_HOME=/jenkins')
		return True

	def get_config(self, shutit):
		return True

	#def start(self, shutit):
	#	return True

	#def stop(self, shutit):
	#    return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/jenkins')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return jenkins(
		'shutit.tk.sd.jenkins.jenkins', 158844782.0312,
		description='jenkins server',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.openjdk.openjdk']
	)


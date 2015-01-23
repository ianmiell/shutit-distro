"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class maven(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')


	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/maven')
		shutit.send('cd /tmp/build/maven')
		shutit.send('wget -qO- http://mirror.ox.ac.uk/sites/rsync.apache.org/maven/maven-3/3.2.5/source/apache-maven-3.2.5-src.tar.gz | tar -zxf -')
		shutit.send('cd apache-maven*')
		shutit.send('export M2_HOME="/opt/maven"')
		shutit.send('ant')
		return True

	def get_config(self, shutit):
		#shutit.get_config(self.module_id,'minimize',boolean=True,default=True) #TODO
		return True

	#def start(self, shutit):
	#	return True

	#def stop(self, shutit):
	#    return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/maven')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return maven(
		'shutit.tk.sd.maven.maven', 158844782.03045,
		description='Apache maven',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.openjdk.openjdk','shutit.tk.sd.ant.ant','shutit.tk.sd.nss.nss']
	)


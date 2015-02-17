"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class maven(ShutItModule):

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/maven')
		shutit.send('cd /tmp/build/maven')
		shutit.send('wget -qO- http://mirror.ox.ac.uk/sites/rsync.apache.org/maven/maven-3/3.2.5/source/apache-maven-3.2.5-src.tar.gz | tar -zxf -')
		shutit.send('cd apache-maven*')
		shutit.send('export M2_HOME=/opt/maven')
		shutit.add_to_bashrc('export M2_HOME=/opt/maven')
		shutit.add_to_bashrc('export PATH=${PATH}:/opt/maven/bin')
		shutit.send('ant')
		return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/maven')
		return True

def module():
	return maven(
		'shutit.tk.sd.maven.maven', 158844782.03045,
		description='Apache maven',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.openjdk.openjdk','shutit.tk.sd.ant.ant','shutit.tk.sd.nss.nss']
	)


"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class junit(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/junit')
		shutit.send('cd /tmp/build/junit')
		shutit.send('wget -qO- https://launchpad.net/debian/+archive/primary/+files/junit4_4.11.orig.tar.gz | tar -zxf -')
		shutit.send('cd junit*')
		shutit.send('wget -qO- http://hamcrest.googlecode.com/files/hamcrest-1.3.tgz | tar -zxf -')
		shutit.send('cp -v hamcrest-1.3/hamcrest-core-1.3{,-sources}.jar lib/')
		shutit.send('ant dist')
		shutit.send('install -v -m755 -d /usr/share/{doc,java}/junit-4.11')
		shutit.send('chown -R root:root .')
		shutit.send('cp -v -R junit*/javadoc/*             /usr/share/doc/junit-4.11')
		shutit.send('cp -v junit*/junit*.jar               /usr/share/java/junit-4.11')
		shutit.send('cp -v hamcrest-1.3/hamcrest-core*.jar /usr/share/java/junit-4.11')
		shutit.add_to_bashrc('export CLASSPATH=$CLASSPATH:/usr/share/java/junit-4.11')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	#def check_ready(self, shutit):
	#	return True
	
	#def start(self, shutit):
	#	return True

	#def stop(self, shutit):
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/junit')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return junit(
		'shutit.tk.sd.junit.junit', 158844782.0126,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.ant.ant','shutit.tk.sd.make_certs.make_certs']
	)


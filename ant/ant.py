"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class ant(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/ant')
		shutit.send('cd /tmp/build/ant')
		shutit.send('wget -qO- http://archive.apache.org/dist/ant/source/apache-ant-1.9.4-src.tar.bz2 | bunzip2 -c | tar -xf -')
		shutit.send('wget -qO- http://anduin.linuxfromscratch.org/sources/other/junit-4.11.jar > junit-4.11.jar')
		shutit.send('cd apache-ant*')
		shutit.send('wget -qO- http://hamcrest.googlecode.com/files/hamcrest-1.3.tgz | tar -zxf -')
		shutit.send('cp -v ../junit-4.11.jar hamcrest-1.3/hamcrest-core-1.3.jar lib/optional')
		shutit.send('./build.sh -Ddist.dir=/opt/ant-1.9.4 dist')
		shutit.send('ln -v -sfn ant-1.9.4 /opt/ant')
		shutit.add_to_bashrc('export PATH=$PATH:/opt/ant/bin')
		shutit.add_to_bashrc('export ANT_HOME=/opt/ant')
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
		shutit.send('rm -rf /tmp/build/ant')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return ant(
		'shutit.tk.sd.ant.ant', 158844782.0123,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.java_binary.java_binary']
	)


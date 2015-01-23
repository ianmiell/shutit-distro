"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class mesos(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')


	def build(self, shutit):
		shutit.send('mkdir -p /opt/mesos')
		shutit.send('cd /opt/mesos')
		shutit.send('pip install boto')
## Install Maven (***Only required for Mesos 0.18.1 or newer***).
#$ sudo apt-get install maven
		return True

	def get_config(self, shutit):
		#shutit.get_config(self.module_id,'minimize',boolean=True,default=True) #TODO
		return True

	#def start(self, shutit):
	#	return True

	#def stop(self, shutit):
	#    return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/mesos')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return mesos(
		'shutit.tk.sd.mesos.mesos', 158844782.0305,
		description='Apache mesos',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.make_certs.make_certs','shutit.tk.sd.curl.curl','shutit.tk.sd.maven.maven','shutit.tk.sd.python_pip.python_pip','shutit.tk.sd.subversion.subversion','shutit.tk.sd.cyrus_sasl.cyrus_sasl','shutit.tk.sd.apache_portable_runtime.apache_portable_runtime']
	)


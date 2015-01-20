"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class google_compute(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')


	def build(self, shutit):
		shutit.send('mkdir -p /opt/google_compute')
		shutit.send('cd /opt/google_compute')
		shutit.multisend('wget -qO- https://sdk.cloud.google.com | bash',{'Directory to extract under':'/opt','Do you want to help improve the Google Cloud SDK':'n','Enter path to an rc file to update, or leave blank to use':'','Modify profile to update your':'','Modify profile to enable bash completion':''})
		return True

	def get_config(self, shutit):
		#shutit.get_config(self.module_id,'minimize',boolean=True,default=True) #TODO
		return True

	#def start(self, shutit):
	#	return True

	#def stop(self, shutit):
	#    return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/google_compute')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return google_compute(
		'shutit.tk.sd.google_compute.google_compute', 158844782.0303,
		description='Google compute engine resources',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.make_certs.make_certs','shutit.tk.sd.curl.curl','shutit.tk.sd.which.which']
	)


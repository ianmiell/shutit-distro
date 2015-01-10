"""ShutIt module. See http://shutit.tk
cf: http://msopentech.com/blog/2014/11/07/creating-asp-net-vnext-docker-container-using-mono-2/
"""

from shutit_module import ShutItModule


class vnext(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/vnext')
		shutit.send('cd /tmp/build/vnext')
		shutit.send('curl -s https://raw.githubusercontent.com/aspnet/Home/master/kvminstall.sh | sh')
		shutit.add_to_bashrc('source /root/.kre/kvm/kvm.sh')
		shutit.send('source /root/.kre/kvm/kvm.sh')
		shutit.send('kvm upgrade')
		shutit.send('kvm alias default | xargs -i ln -s /root/.kre/packages/{} /root/.kre/packages/default')
		return True

	def get_config(self, shutit):
		return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/vnext')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return vnext(
		'shutit.tk.sd.vnext.vnext', 158844782.0296,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.mono.mono','shutit.tk.sd.curl.curl']
	)


"""ShutIt module. See http://shutit.tk/
"""

from shutit_module import ShutItModule

class go(ShutItModule):

	def is_installed(self,shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self,shutit):
		shutit.send('mkdir -p /tmp/build/go')
		shutit.send('cd /tmp/build/go')
		shutit.send('wget -qO- --no-check-certificate https://storage.googleapis.com/golang/go' + shutit.cfg[self.module_id]['version'] + '.src.tar.gz | tar -zxf -')
		shutit.send('cd go/src/')
		shutit.send('GOROOT_FINAL=/usr ./make.bash')
		shutit.send('mv /tmp/build/go/go/bin/go /usr/bin')
		shutit.send('mv /tmp/build/go/go/bin/gofmt /usr/bin')
		return True

	def get_config(self,shutit):
		shutit.get_config(self.module_id,'version','1.3.3')
		return True

	#def check_ready(self,shutit):
	#    return True
	
	#def start(self,shutit):
	#    return True

	#def stop(self,shutit):
	#    return True

	def finalize(self,shutit):
		#shutit.send('rm -rf
		return True

	#def remove(self,shutit):
	#    return True

	#def test(self,shutit):
	#    return True

def module():
	return go(
		'shutit.tk.sd.go.go', 158844782.0077,
		description='Go language setup (direct from source)',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.pkg_config.pkg_config']
	)


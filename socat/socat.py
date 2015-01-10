"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class socat(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/socat')
		shutit.send('cd /tmp/build/socat')
		shutit.get_url('socat-2.0.0-b7.tar.gz',['http://www.dest-unreach.org/socat/download'])
		shutit.send('tar -zxf socat-2.0.0-b7.tar.gz')
		shutit.send('rm -f socat-2.0.0-b7.tar.gz')
		shutit.send('cd socat-*')
		shutit.send('./configure --prefix=/usr')
		shutit.send('make')
		shutit.send('make MANDEST=/usr/share/man install')
		return True

	def get_config(self, shutit):
		return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/socat')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return socat(
		'shutit.tk.sd.socat.socat', 158844782.0294,
		description='',
		maintainer='',
		depends=['shutit.tk.setup']
	)


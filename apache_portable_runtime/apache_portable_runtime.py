"""ShutIt module. See http://shutit.tk/
"""

from shutit_module import ShutItModule


class apache_portable_runtime(ShutItModule):

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/apr')
		shutit.send('cd /tmp/build/apr')
		shutit.get_url('apr-1.5.1.tar.gz',['http://mirror.catn.com/pub/apache/apr','http://mirror.ox.ac.uk/sites/rsync.apache.org/apr'])
		shutit.send('tar -zxf apr-1.5.1.tar.gz')
		shutit.send('cd apr-' + shutit.cfg[self.module_id]['version'])
		shutit.send('./configure --prefix=/usr')
		shutit.send('make')
		shutit.send('make install')
		return True

	def is_installed(self,shutit):
		return False

	def get_config(self, shutit):
		shutit.get_config(self.module_id,'version','1.5.1')
		return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/apr')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return apache_portable_runtime(
		'shutit.tk.sd.apache_portable_runtime.apache_portable_runtime', 158844782.0049,
		description='',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.setup']
	)


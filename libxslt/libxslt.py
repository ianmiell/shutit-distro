"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class libxslt(ShutItModule):

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/libxslt')
		shutit.send('cd /tmp/build/libxslt')
		shutit.send('wget -qO- http://xmlsoft.org/sources/libxslt-' + shutit.cfg[self.module_id]['version'] + '.tar.gz | tar -zxf -')
		shutit.send('cd libxslt-*')
		shutit.send('./configure --prefix=/usr')
		shutit.send('make')
		shutit.send('make install')
		return True

	def get_config(self, shutit):
		shutit.get_config(self.module_id,'version','1.1.28')
		return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/libxslt')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return libxslt(
		'shutit.tk.sd.libxslt.libxslt', 158844782.0052,
		description='',
		maintainer='',
		depends=['shutit.tk.setup']
	)


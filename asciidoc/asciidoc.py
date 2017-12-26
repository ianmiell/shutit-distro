"""ShutIt module. See http://shutit.tk/
"""

from shutit_module import ShutItModule


class asciidoc(ShutItModule):

	def build(self, shutit):
		#http://www.methods.co.nz/asciidoc/INSTALL.html#X1
		shutit.send('mkdir -p /tmp/build/asciidoc')
		shutit.send('cd /tmp/build/asciidoc')
		shutit.get_url('asciidoc-' + shutit.cfg[self.module_id]['version'] + '.tar.gz',['https://distfiles.macports.org/asciidoc/','http://downloads.sourceforge.net/project/asciidoc/asciidoc/' + shutit.cfg[self.module_id]['version']])
		shutit.send('tar -zxf asciidoc-' + shutit.cfg[self.module_id]['version'] + '.tar.gz')
		shutit.send('cd asciidoc-' + shutit.cfg[self.module_id]['version'])
		shutit.send('./configure --prefix=/usr')
		shutit.send('make')
		shutit.send('make install')
		return True

	def is_installed(self,shutit):
		return False

	def get_config(self, shutit):
		shutit.get_config(self.module_id,'version','8.6.9')
		return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/asciidoc')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return asciidoc(
		'shutit.tk.sd.asciidoc.asciidoc', 158844782.006,
		description='',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.setup']
	)


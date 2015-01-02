"""ShutIt module. See http://shutit.tk/
"""

from shutit_module import ShutItModule


class asciidoc(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')


	def build(self, shutit):
		#http://www.methods.co.nz/asciidoc/INSTALL.html#X1
		shutit.send('mkdir -p /tmp/build/asciidoc')
		shutit.send('cd /tmp/build/asciidoc')
		shutit.send('wget -qO- http://downloads.sourceforge.net/project/asciidoc/asciidoc/' + shutit.cfg[self.module_id]['version'] + '/asciidoc-' + shutit.cfg[self.module_id]['version'] + '.tar.gz | tar -zxf -')
		shutit.send('cd asciidoc-' + shutit.cfg[self.module_id]['version'])
		shutit.send('./configure --prefix=/usr')
		shutit.send('make')
		shutit.send('make install')
		return True

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
		depends=['shutit.tk.sd.python2.python2']
	)


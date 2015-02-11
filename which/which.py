"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule

class which(ShutItModule):

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/which')
		shutit.send('cd /tmp/build/which')
		shutit.send('wget -qO- http://ftp.gnu.org/gnu/which/which-2.20.tar.gz | tar -zxf -')
		shutit.send('cd which-*')
		shutit.send('./configure --prefix=/usr')
		shutit.send('make')
		shutit.send('make install')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/which')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return which(
		'shutit.tk.sd.which.which', 158844782.0015,
		description='',
		maintainer='',
		depends=['shutit.tk.setup']
	)


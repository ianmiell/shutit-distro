"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class nasm(ShutItModule):

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/nasm')
		shutit.send('cd /tmp/build/nasm')
		shutit.send('wget -qO- http://www.nasm.us/pub/nasm/releasebuilds/2.11.05/nasm-2.11.05.tar.xz | xz -d | tar -xf -')
		shutit.send('cd nasm*')
		shutit.send('./configure --prefix=/usr')
		shutit.send('make')
		shutit.send('make install')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/nasm')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return nasm(
		'shutit.tk.sd.nasm.nasm', 158844782.0111,
		description='',
		maintainer='',
		depends=['shutit.tk.setup']
	)


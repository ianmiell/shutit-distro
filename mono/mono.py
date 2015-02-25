"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class mono(ShutItModule):

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/mono')
		shutit.send('cd /tmp/build/mono')
		shutit.get_url('mono-3.10.0.tar.bz2',['http://download.mono-project.com/sources/mono'])
		shutit.send('bunzip2 mono-3.10.0.tar.bz2')
		shutit.send('tar -xf mono-3.10.0.tar')
		shutit.send('cd mono-*')
		shutit.send('./configure --prefix=/usr')
		shutit.send('make')
		shutit.send('make install')
		return True

	def get_config(self, shutit):
		return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/mono')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return mono(
		'shutit.tk.sd.mono.mono', 158844782.0295,
		description='',
		maintainer='',
		depends=['shutit.tk.setup']
	)


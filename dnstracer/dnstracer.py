"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class dnstracer(ShutItModule):

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/dnstracer')
		shutit.send('cd /tmp/build/dnstracer')
		shutit.send('wget -qO- http://www.mavetju.org/download/dnstracer-1.9.tar.gz | tar -zxf -')
		shutit.send('cd dnstracer*')
		shutit.send('./configure --prefix=/usr')
		shutit.send('make')
		shutit.send('make install')
		return True

	def get_config(self, shutit):
		return True

	#def start(self, shutit):
	#	return True

	#def stop(self, shutit):
	#    return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/dnstracer')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return dnstracer(
		'shutit.tk.sd.dnstracer.dnstracer', 158844782.0316,
		description='dnstracer',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.setup']
	)


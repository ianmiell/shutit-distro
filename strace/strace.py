"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class strace(ShutItModule):

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/strace')
		shutit.send('cd /tmp/build/strace')
		shutit.send('wget -qO- http://sourceforge.net/projects/strace/files/strace/4.6/strace-4.6.tar.xz | xz -d | tar -xf -')
		shutit.send('cd strace*')
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
		shutit.send('rm -rf /tmp/build/strace')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return strace(
		'shutit.tk.sd.strace.strace', 158844782.0309,
		description='strace',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.setup']
	)


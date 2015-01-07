"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class apt(ShutItModule):


	def is_installed(self, shutit):
		return False


	def build(self, shutit):
#http://algebraicthunk.net/~dburrows/blog/entry/howto-get-the-apt-source-repository/
		shutit.send('mkdir -p /tmp/build/apt')
		shutit.send('cd /tmp/build/apt')
		shutit.send('git clone git://anonscm.debian.org/apt/apt.git')
		shutit.send('cd apt')
		shutit.pause_point('')
		shutit.send('autoreconf -f -i')
		shutit.send('./configure --prefix=/usr')
		shutit.send('make')
		shutit.send('make install')
		return True

	#def get_config(self, shutit):
	#	return True

	#def check_ready(self, shutit):
	#	return True
	
	#def start(self, shutit):
	#	return True

	#def stop(self, shutit):
	#    return True
	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/apt')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return apt(
		'shutit.tk.sd.apt.apt', 158844782.02825,
		description='',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.curl.curl','shutit.tk.sd.xmlto.xmlto','shutit.tk.sd.berkeleydb.berkeleydb']
	)


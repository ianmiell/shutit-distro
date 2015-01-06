"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class dpkg(ShutItModule):


	def is_installed(self, shutit):
		return False


	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/dpkg')
		shutit.send('cd /tmp/build/dpkg')
		shutit.send('git clone -b 1.17.23 git://anonscm.debian.org/dpkg/dpkg.git')
		shutit.send('cd dpkg')
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
		shutit.send('rm -rf /tmp/build/dpkg')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return dpkg(
		'shutit.tk.sd.dpkg.dpkg', 158844782.0282,
		description='',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.git.git']
	)


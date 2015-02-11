"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class deis_client(ShutItModule):

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/deis_client')
		shutit.send('cd /tmp/build/deis_client')
		shutit.send('curl -sSL http://deis.io/deis-cli/install.sh | sh')
		shutit.send('ln -fs $PWD/deis /usr/bin/deis')
		return True

	def get_config(self, shutit):
		return True

	#def start(self, shutit):
	#	return True

	#def stop(self, shutit):
	#    return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/deis_client')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return deis_client(
		'shutit.tk.sd.deis_client.deis_client', 158844782.0307,
		description='deis_client',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.curl.curl']
	)


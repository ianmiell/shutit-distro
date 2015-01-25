"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class nmap(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')


	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/nmap')
		shutit.send('cd /tmp/build/nmap')
		shutit.send('wget -qO- https://nmap.org/dist/nmap-6.47.tar.bz2 | bunzip2 -c | tar -xf -')
		shutit.send('cd nmap*')
		shutit.send('./configure')
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
		shutit.send('rm -rf /tmp/build/nmap')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return nmap(
		'shutit.tk.sd.nmap.nmap', 158844782.0306,
		description='nmap',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.make_certs.make_certs']
	)


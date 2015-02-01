"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class bind(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')


	def build(self, shutit):
		# TODO: follow this: http://www.linuxfromscratch.org/blfs/view/cvs/server/bind.html
		shutit.send('mkdir -p /tmp/build/bind')
		shutit.send('cd /tmp/build/bind')
		shutit.send('wget -qO- http://ftp.isc.org/isc/bind9/9.9.6/bind-9.9.6.tar.gz | tar -zxf -')
		shutit.send('cd bind*')
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
		shutit.send('rm -rf /tmp/build/bind')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return bind(
		'shutit.tk.sd.bind.bind', 158844782.0317,
		description='bind',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.setup']
	)


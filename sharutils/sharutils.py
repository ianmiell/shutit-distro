"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class sharutils(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/sharutils')
		shutit.send('cd /tmp/build/sharutils')
		shutit.send('wget -qO- http://ftp.gnu.org/gnu/sharutils/sharutils-4.14.tar.xz | xz -d | tar -xf -')
		shutit.send('cd sharutils*')
		shutit.send('./configure --prefix=/usr')
		shutit.send('make')
		shutit.send('make install')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	#def check_ready(self, shutit):
	#	return True
	
	#def start(self, shutit):
	#	return True

	#def stop(self, shutit):
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/sharutils')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return sharutils(
		'shutit.tk.sd.sharutils.sharutils', 158844782.0012,
		description='',
		maintainer='',
		depends=['shutit.tk.setup']
	)


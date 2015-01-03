"""ShutIt module. See http://shutit.tk
"""
from shutit_module import ShutItModule


class elfutils(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('wget -qO- https://fedorahosted.org/releases/e/l/elfutils/0.161/elfutils-0.161.tar.bz2 | bunzip2 -c | tar -xf -')
		shutit.send('cd elfutils-*')
		shutit.send('./configure --prefix=/usr --program-prefix="eu-"')
		shutit.send('make')
		shutit.send('make install')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/elfutils')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return elfutils(
		'shutit.tk.sd.elfutils.elfutils', 158844782.02565,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.make_certs.make_certs']
	)


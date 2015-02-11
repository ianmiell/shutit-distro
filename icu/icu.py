"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class icu(ShutItModule):

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/icu')
		shutit.send('cd /tmp/build/icu')
		shutit.send('wget -qO- http://download.icu-project.org/files/icu4c/53.1/icu4c-53_1-src.tgz | tar -zxf -')
		shutit.send('cd icu')
		shutit.send('cd source')
		shutit.send('./configure --prefix=/usr')
		shutit.send('make')
		shutit.send('make install')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/icu')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return icu(
		'shutit.tk.sd.icu.icu', 158844782.0032,
		description='',
		maintainer='',
		depends=['shutit.tk.setup']
	)


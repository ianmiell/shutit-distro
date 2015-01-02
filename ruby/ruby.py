"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class ruby(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/ruby')
		shutit.send('cd /tmp/build/ruby')
		shutit.send('wget -qO- http://cache.ruby-lang.org/pub/ruby/2.2/ruby-2.2.0.tar.gz | tar -zxf -')
		shutit.send('cd ruby*')
		shutit.send('./configure --prefix=/usr')
		shutit.send('make')
		shutit.send('make install')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/ruby')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return ruby(
		'shutit.tk.sd.ruby.ruby', 158844782.0025,
		description='',
		maintainer='',
		depends=['shutit.tk.setup']
	)


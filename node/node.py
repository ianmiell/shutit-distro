"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class node(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/node')
		shutit.send('cd /tmp/build/node')
		shutit.send('wget -qO- http://node.org/dist/v0.10.35/node-v0.10.35.tar.gz | tar -zxf -')
		shutit.send('cd node*')
		shutit.send('./configure --prefix=/usr')
		shutit.send('make')
		shutit.send('make install')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/node')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return node(
		'shutit.tk.sd.node.node', 158844782.0232,
		description='',
		maintainer='',
		depends=['shutit.tk.setup']
	)


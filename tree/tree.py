"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class tree(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/tree')
		shutit.send('cd /tmp/build/tree')
		shutit.send('wget -qO- http://mama.indstate.edu/users/ice/tree/src/tree-1.7.0.tgz | tar -zxf -')
		shutit.send('cd tree*')
		shutit.send('make')
		shutit.send('make MANDIR=/usr/share/man/man1 install')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/tree')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return tree(
		'shutit.tk.sd.tree.tree', 158844782.0239,
		description='',
		maintainer='',
		depends=['shutit.tk.setup']
	)


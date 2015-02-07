"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class react(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('wget http://facebook.github.io/react/downloads/react-0.12.2.zip')
		shutit.send('unzip react-0.12.2.zip')
		shutit.send('npm install -g react-tools')
		shutit.send('npm install -g react')
		return True

def module():
	return react(
		'shutit.tk.sd.react.react', 158844782.0302,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.node.node']
	)


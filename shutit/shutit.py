"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class shutit(ShutItModule):

	def build(self, shutit):
		shutit.send('mkdir -p /opt')
		shutit.send('cd /opt')
		shutit.send('git clone https://github.com/ianmiell/shutit.git')
		shutit.send('cd shutit')
		shutit.send('pip install -r requirements.txt')
		shutit.add_to_bashrc('export PATH=$PATH:/opt/shutit')
		return True

def module():
	return shutit(
		'shutit.tk.sd.shutit.shutit', 158844782.0299,
		description='A ShutIt environment from which you can reliably build an image in delivery --bash, built from source',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.git.git','shutit.tk.sd.curl.curl','shutit.tk.sd.python_pip.python_pip']
	)


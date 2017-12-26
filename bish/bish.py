"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class bish(ShutItModule):

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/bish')
		shutit.send('cd /tmp/build/bish')
		shutit.send('git clone https://github.com/tdenniston/bish')
		shutit.send('cd bish')
		shutit.send('''sed -i 's/std::ifstream t(path/std::ifstream t(path.c_str()/' src/Parser.cpp''')
		shutit.send('make')
		shutit.send('cp bish /usr/bin/bish')
		return True

	def is_installed(self,shutit):
		return False
	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/bish')
		return True

def module():
	return bish(
		'shutit.tk.sd.bish.bish', 158844782.0322,
		description='',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.git.git']
	)


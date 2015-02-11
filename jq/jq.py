"""ShutIt module. See http://shutit.tk/
"""

from shutit_module import ShutItModule


class jq(ShutItModule):

	def build(self, shutit):
		shutit.send('cd /tmp/build')
		shutit.send('git clone https://github.com/stedolan/jq.git')
		shutit.send('cd jq')
		shutit.send('autoreconf -i')
		shutit.send('./configure --prefix=/usr')
		shutit.send('make')
		shutit.send('make check')
		shutit.send('make install')
		return True

	#def get_config(self, shutit):
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/jq')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return jq(
		'shutit.tk.sd.jq.jq', 158844782.01075,
		description='JQ - sed for JSON',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.git.git','shutit.tk.sd.onigurama.onigurama']
	)


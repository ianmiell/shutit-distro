"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class zaproxy(ShutItModule):

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/zaproxy')
		shutit.get_url('ZAP_2.3.1_Linux.tar.gz',['http://sourceforge.net/projects/zaproxy/files/2.3.1'])
		shutit.send('tar -zxf ZAP_*tar.gz')
		shutit.send('cd ZAP*')
		shutit.pause_point('')
		return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/zaproxy')
		return True

def module():
	return zaproxy(
		'shutit.tk.sd.zaproxy.zaproxy', 158844782.0319,
		description='HTTP intercepting proxy',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.openjdk.openjdk']
	)


"""ShutIt module. See http://shutit.tk
"""
from shutit_module import ShutItModule


class intrace(ShutItModule):

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/intrace')
		shutit.send('cd /tmp/build/intrace')
		shutit.get_url('intrace-1.5.tgz',['https://intrace.googlecode.com/files'])
		shutit.send('tar -zxf intrace-1.5.tgz')
		shutit.send('cd intrace*')
		shutit.send('''sed -i 's/-Werror//' Makefile''')
		shutit.send('make')
		shutit.send('mv intrace /usr/bin/intrace')
		return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/intrace')
		return True

def module():
	return intrace(
		'shutit.tk.sd.intrace.intrace', 158844782.027,
		description='Intrace - like traceroute but piggybacks TCP',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.make_certs.make_certs']
	)


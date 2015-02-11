"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class thrift(ShutItModule):

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/thrift')
		shutit.send('cd /tmp/build/thrift')
		shutit.send('wget -qO- http://mirror.gopotato.co.uk/apache/thrift/0.9.2/thrift-0.9.2.tar.gz | tar -zxf -')
		shutit.send('cd thrift*')
		shutit.send('./configure --prefix=/usr')
		shutit.send('make')
		shutit.send('make install')
		return True

	#def get_config(self, shutit):
	#	return True

	#def check_ready(self, shutit):
	#	return True
	
	#def start(self, shutit):
	#	return True

	#def stop(self, shutit):
	#    return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/thrift')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return thrift(
		'shutit.tk.sd.thrift.thrift', 158844782.0283,
		description='',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.boost.boost','shutit.tk.sd.libevent.libevent','shutit.tk.sd.glib.glib','shutit.tk.sd.ruby.ruby','shutit.tk.sd.node.node']
		# TODO: depend on more languages, cf #https://thrift.apache.org/docs/BuildingFromSource
	)


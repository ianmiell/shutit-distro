"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class erlang(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/erlang')
		shutit.send('cd /tmp/build/erlang')
		shutit.send('wget -qO- http://www.erlang.org/download/otp_src_17.3.tar.gz | tar -zxf -')
		shutit.send('cd otp*')
		shutit.send('./configure --prefix=/usr')
		shutit.send('make')
		shutit.send('make install')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/erlang')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return erlang(
		'shutit.tk.sd.erlang.erlang', 158844782.901112531353,
		description='',
		maintainer='',
		depends=['shutit.tk.setup']
	)


"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class xdotool(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		import sd_util
		sd_util.setup_x_environment(shutit)
		shutit.send('mkdir -p /tmp/build/xdotool')
		shutit.send('cd /tmp/build/xdotool')
		shutit.get_url('xdotool-2.20110530.1.tar.gz',['http://semicomplete.googlecode.com/files'])
		shutit.send('tar -zxf xdotool-2.20110530.1.tar.gz')
		shutit.send('rm -f xdotool-2.20110530.1.tar.gz')
		shutit.send('cd xdotool-*')
		shutit.send('make')	
		shutit.send('make install')	
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/xdotool')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return xdotool(
		'shutit.tk.sd.xdotool.xdotool', 158844782.0292,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.xterm.xterm']
	)


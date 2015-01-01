"""ShutIt module. See http://shutit.tk/
"""
from shutit_module import ShutItModule

class sthttpd(ShutItModule):

	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('groupadd thttpd')
		shutit.send('mkdir -p /tmp/build/sthttpd')
		shutit.send('cd /tmp/build/sthttpd')
		shutit.send('git clone git://opensource.dyc.edu/sthttpd sthttpd')
		shutit.send('cd sthttpd')
		shutit.send('./autogen.sh')
		shutit.send('./configure --prefix=/usr')
		shutit.send('make')
		shutit.send('make install')
		return True

	#def get_config(self, shutit):
	#    return True

	#def check_ready(self, shutit):
	#    return True
	
	#def start(self, shutit):
	#    return True

	#def stop(self, shutit):
	#    return True

	def finalize(self, shutit):
		#shutit.send('rm -rf
		return True

	#def remove(self, shutit):
	#    return True

	#def test(self, shutit):
	#    return True

def module():
	return sthttpd(
		'shutit.tk.sd.sthttpd.sthttpd', 158844782.0236,
		description='Small lightweight web server',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.git.git','shutit.tk.sd.libxslt.libxslt']
	)


"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class inotify_tools(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')


	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/inotify_tools')
		shutit.send('cd /tmp/build/inotify_tools')
		shutit.send('wget -qO- http://github.com/downloads/rvoicilas/inotify-tools/inotify-tools-3.14.tar.gz | tar -zxf -')
		shutit.send('cd inotify*')
		shutit.send('./configure --prefix=/usr')
		shutit.send('make')
		shutit.send('make install')
		return True

	def get_config(self, shutit):
		return True

	#def start(self, shutit):
	#	return True

	#def stop(self, shutit):
	#    return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/inotify_tools')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return inotify_tools(
		'shutit.tk.sd.inotify_tools.inotify_tools', 158844782.0308,
		description='inotify_tools',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.make_certs.make_certs']
	)


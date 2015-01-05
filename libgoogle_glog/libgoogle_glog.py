"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class libgoogle_glog(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/libgoogle_glog')
		shutit.send('cd /tmp/build/libgoogle_glog')
		shutit.send('wget -qO- https://google-glog.googlecode.com/files/glog-0.3.3.tar.gz | tar -zxf -')
		shutit.send('cd glog*')
		shutit.send('./configure --prefix=/usr')
		shutit.send('make')
		shutit.send('make install')
		return True

	def get_config(self, shutit):
		return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/libgoogle_glog')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return libgoogle_glog(
		'shutit.tk.sd.libgoogle_glog.libgoogle_glog', 158844782.0269,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.make_certs.make_certs']
	)


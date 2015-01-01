"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class x7proto(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		import sd_util
		sd_util.setup_x_environment(shutit)
		shutit.send('mkdir /tmp/build/x7proto')
		shutit.send('cd /tmp/build/x7proto')
		shutit.send('mkdir build')
		shutit.send('cd build')
		shutit.send_host_file('/tmp/build/x7proto/proto-7.7.md5','context/proto-7.7.md5')
		shutit.send('''grep -v '^#' ../proto-7.7.md5 | awk '{print $2}' | wget -i- -c -B http://xorg.freedesktop.org/releases/individual/proto/''')
		shutit.send('md5sum -c ../proto-7.7.md5')
		shutit.login(command='bash -e')
		shutit.send('''for package in $(grep -v '^#' ../proto-7.7.md5 | awk '{print $2}'); do packagedir=${package%.tar.bz2}; tar -xf $package; pushd $packagedir; ./configure $XORG_CONFIG; make; make install; popd; rm -rf $packagedir; done''')
		shutit.logout()
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	#def check_ready(self, shutit):
	#	return True
	
	#def start(self, shutit):
	#	return True

	#def stop(self, shutit):
	#	return True

	#def finalize(self, shutit):
	#	return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return x7proto(
		'shutit.tk.sd.x7proto.x7proto', 158844782.00802,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.util_macros.util_macros','shutit.tk.sd.libxslt.libxslt']
	)


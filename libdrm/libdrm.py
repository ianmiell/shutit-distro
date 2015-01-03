"""ShutIt module. See http://shutit.tk
"""
from shutit_module import ShutItModule


class libdrm(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		import sd_util
		sd_util.setup_x_environment(shutit) # required?
		shutit.send('wget -qO- http://dri.freedesktop.org/libdrm/libdrm-2.4.58.tar.bz2 | bunzip2 -c | tar -xf -')
		shutit.send('cd libdrm-*')
		shutit.send('sed -e "/pthread-stubs/d" -i configure.ac')
		shutit.send('autoreconf -fiv')
		shutit.send('./configure --prefix=/usr --enable-udev')
		shutit.send('make')
		shutit.send('make install')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/libdrm')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return libdrm(
		'shutit.tk.sd.libdrm.libdrm', 158844782.0256,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.xorg_libs.xorg_libs']
	)


"""ShutIt module. See http://shutit.tk
"""
from shutit_module import ShutItModule


class mesalib(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		import sd_util
		sd_util.setup_x_environment(shutit) # required?
		shutit.send('wget -qO- ftp://ftp.freedesktop.org/pub/mesa/10.3.5/MesaLib-10.3.5.tar.bz2 | bunzip2 -c | tar -xf -')
		shutit.send('cd Mesa*')
		shutit.send('wget -qO- http://www.linuxfromscratch.org/patches/blfs/svn/MesaLib-10.3.5-add_xdemos-1.patch | patch -Np1 -i -')
		shutit.send('./autogen.sh CFLAGS="-O2" CXXFLAGS="-O2" --prefix=$XORG_PREFIX --sysconfdir=/etc --enable-texture-float --enable-gles1 --enable-gles2 --enable-openvg --enable-osmesa --enable-xa --enable-gbm --enable-gallium-egl --enable-gallium-gbm --enable-glx-tls --with-egl-platforms="drm,x11" --with-gallium-drivers="nouveau,r300,r600,radeonsi,svga,swrast"')
		shutit.send('make')
		shutit.send('make install')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/mesalib')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return mesalib(
		'shutit.tk.sd.mesalib.mesalib', 158844782.0257,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.libdrm.libdrm','shutit.tk.sd.python2.python2','shutit.tk.sd.llvm.llvm','shutit.tk.sd.elfutils.elfutils']
	)


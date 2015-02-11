"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class xorg_libs(ShutItModule):

	def build(self, shutit):
		import sd_util
		sd_util.setup_x_environment(shutit)
		shutit.send('mkdir -p /tmp/build/xorg_libs')
		shutit.send('cd /tmp/build/xorg_libs')
		shutit.send_host_file('/tmp/build/xorg_libs/lib-7.7.md5','context/lib-7.7.md5')
		shutit.send('''grep -v '^#' lib-7.7.md5 | awk '{print $2}' | wget -i- -c -B http://xorg.freedesktop.org/releases/individual/lib/''')
		shutit.send('md5sum -c lib-7.7.md5')
		shutit.login(command='bash -e')
		shutit.run_script(r'''for package in $(grep -v '^#' lib-7.7.md5 | awk '{print $2}')
		do
		  packagedir=${package%.tar.bz2}
		  tar -xf $package
		  pushd $packagedir
		  case $packagedir in
		    libXfont-[0-9]* )
		      ./configure $XORG_CONFIG --disable-devel-docs
		    ;;
		    libXt-[0-9]* )
		      ./configure $XORG_CONFIG --with-appdefaultdir=/etc/X11/app-defaults
		    ;;
		    * )
		      ./configure $XORG_CONFIG
		    ;;
		  esac
		  make
		  make install
		  popd
		  rm -rf $packagedir
		  /sbin/ldconfig
		done''')
		shutit.logout()
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/xorg_libs')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return xorg_libs(
		'shutit.tk.sd.xorg_libs.xorg_libs', 158844782.0106,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.fontconfig.fontconfig','shutit.tk.sd.libxcb.libxcb']
	)


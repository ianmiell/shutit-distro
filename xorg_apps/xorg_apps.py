"""ShutIt module. See http://shutit.tk
"""
from shutit_module import ShutItModule


class xorg_apps(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		import sd_util
		sd_util.setup_x_environment(shutit)
		shutit.send('mkdir -p /tmp/build/xorg_apps')
		shutit.send('cd /tmp/build/xorg_apps')
		shutit.send_host_file('/tmp/build/xorg_apps/app-7.7.md5','context/app-7.7.md5')
		shutit.send('''grep -v '^#' app-7.7.md5 | awk '{print $2}' | wget -i- -c -B http://xorg.freedesktop.org/releases/individual/app/''')
		shutit.send('md5sum -c app-7.7.md5')
		shutit.login(command='bash -e')
		shutit.run_script(r'''for package in $(grep -v '^#' ../app-7.7.md5 | awk '{print $2}')
			do
			  packagedir=${package%.tar.bz2}
			  tar -xf $package
			  pushd $packagedir
			  case $packagedir in
			    luit-[0-9]* )
			      line1="#ifdef _XOPEN_SOURCE"
			      line2="#  undef _XOPEN_SOURCE"
			      line3="#  define _XOPEN_SOURCE 600"
			      line4="#endif"
			 
			      sed -i -e "s@#ifdef HAVE_CONFIG_H@$line1\n$line2\n$line3\n$line4\n\n&@" sys.c
			      unset line1 line2 line3 line4
			    ;;
			  esac
			  ./configure $XORG_CONFIG
			  make
			  as_root make install
			  popd
			  rm -rf $packagedir
			done
		''')

		shutit.logout()
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/xorg_apps')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return xorg_apps(
		'shutit.tk.sd.xorg_apps.xorg_apps', 158844782.026,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.libpng.libpng','shutit.tk.sd.mesalib.mesalib','shutit.tk.sd.xbitmaps.xbitmaps','shutit.tk.sd.xcb_util.xcb_util','shutit.tk.sd.linux_pam.linux_pam']
	)


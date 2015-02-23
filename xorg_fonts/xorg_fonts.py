"""ShutIt module. See http://shutit.tk
"""
from shutit_module import ShutItModule


class xorg_fonts(ShutItModule):

	def build(self, shutit):
		import sd_util
		sd_util.setup_x_environment(shutit)
		shutit.send('mkdir -p /tmp/build/xorg_fonts')
		shutit.send('cd /tmp/build/xorg_fonts')
		shutit.send_host_file('font-7.7.md5','context/font-7.7.md5')
		shutit.send('mkdir -p font')
		shutit.send('cd font')
		shutit.send(r'''grep -v '^#' ../font-7.7.md5 | awk '{print $2}' | wget -i- -c -B http://xorg.freedesktop.org/releases/individual/font/ ''')
		shutit.send('md5sum -c ../font-7.7.md5')
		shutit.login(command='bash -e')
		shutit.run_script(r'''for package in $(grep -v '^#' ../font-7.7.md5 | awk '{print $2}')
            do
              packagedir=${package%.tar.bz2}
              tar -xf $package
              pushd $packagedir
              ./configure $XORG_CONFIG
              make
              make install
              popd
              rm -rf $packagedir
            done
        ''')
		shutit.logout()
		shutit.send('install -v -d -m755 /usr/share/fonts')
		shutit.send('ln -svfn $XORG_PREFIX/share/fonts/X11/OTF /usr/share/fonts/X11-OTF')
		shutit.send('ln -svfn $XORG_PREFIX/share/fonts/X11/TTF /usr/share/fonts/X11-TTF')
		return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/xorg_fonts')
		return True


def module():
	return xorg_fonts(
		'shutit.tk.sd.xorg_fonts.xorg_fonts', 158844782.02602,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.xcursor_themes.xcursor_themes']
	)


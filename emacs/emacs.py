"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class emacs(ShutItModule):


	def is_installed(self, shutit):
		return False


	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/emacs')
		shutit.send('cd /tmp/build/emacs')
		shutit.send('wget -qO- http://ftp.gnu.org/pub/gnu/emacs/emacs-24.4.tar.xz | xz -d | tar -xf -')
		shutit.send('cd emacs*')
		shutit.send('./configure --prefix=/usr --with-gif=no --localstatedir=/var')
		shutit.send('make bootstrap')
		shutit.send('make install')
		shutit.send('chown -v -R root:root /usr/share/emacs/24.4')
		#shutit.send('gtk-update-icon-cache -qf /usr/share/icons/hicolor') # only with gtk+
		return True

	#def get_config(self, shutit):
	#	return True

	#def check_ready(self, shutit):
	#	return True
	
	#def start(self, shutit):
	#	return True

	#def stop(self, shutit):
	#    return True
	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/emacs')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return emacs(
		'shutit.tk.sd.emacs.emacs', 158844782.0289,
		description='',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.setup']
# TODO: optional deps:  X Window System, alsa-lib-1.0.28, D-Bus-1.8.12, GnuTLS-3.3.11, gobject-introspection-1.42.0, GPM-1.20.7, GTK+-2.24.25 or GTK+-3.14.6, ImageMagick-6.9.0-0, libjpeg-turbo-1.3.1, libpng-1.6.16, librsvg-2.40.6, LibTIFF-4.0.3, and libungif 
	)


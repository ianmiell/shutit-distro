"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class gtk2(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/gtk2')
		shutit.send('cd /tmp/build/gtk2')
		shutit.send('wget -qO- http://ftp.gnome.org/pub/gnome/sources/gtk+/2.24/gtk+-2.24.24.tar.xz | xz -d | tar -xf -')
		shutit.send('cd gtk*')
		shutit.send(r'''sed -i 's#l \(gtk-.*\).sgml#& -o \1#' docs/{faq,tutorial}/Makefile.in''')
		shutit.send('''sed -i 's#.*@man_#man_#' docs/reference/gtk/Makefile.in''')
		shutit.send('''sed -i -e 's#pltcheck.sh#$(NULL)#g' gtk/Makefile.in''')
		shutit.send('./configure --prefix=/usr --sysconfdir=/etc')
		shutit.send('make')
		shutit.send('make install')
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
	return gtk2(
		'shutit.tk.sd.gtk2.gtk2', 158844782.0120,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.atk.atk','shutit.tk.sd.gdk_pixbuf.gdk_pixbuf','shutit.tk.sd.pango.pango','shutit.tk.sd.cairo.cairo']
	)


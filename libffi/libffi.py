"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class libffi(ShutItModule):

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/libffi')
		shutit.send('cd /tmp/build/libffi')
		shutit.send('wget -qO- ftp://sourceware.org/pub/libffi/libffi-3.2.1.tar.gz | tar -zxf -')
		shutit.send('cd libffi-*')
		shutit.send("sed -e '/^includesdir/ s/$(libdir).*$/$(includedir)/' -i include/Makefile.in")
		shutit.send("sed -e '/^includedir/ s/=.*$/=@includedir@/' -e 's/^Cflags: -I${includedir}/Cflags:/' -i libffi.pc.in")
		shutit.send('./configure --prefix=/usr --disable-static')
		shutit.send('make')
		shutit.send('make install')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/libffi')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return libffi(
		'shutit.tk.sd.libffi.libffi', 158844782.0016,
		description='',
		maintainer='',
		depends=['shutit.tk.setup']
	)


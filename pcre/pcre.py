"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class pcre(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/pcre')
		shutit.send('cd /tmp/build/pcre')
		shutit.send('wget -qO- ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/pcre-8.36.tar.bz2 | bunzip2 -c | tar -xf -')
		shutit.send('cd pcre*')
		#shutit.send('./configure --prefix=/usr --docdir=/usr/share/doc/pcre-8.36 --enable-unicode-properties --enable-pcre16 --enable-pcre32 --enable-pcregrep-libz --enable-pcregrep-libbz2 --enable-pcretest-libreadline --disable-static') # TODO: reinstate the enables
		shutit.send('./configure --prefix=/usr --docdir=/usr/share/doc/pcre-8.36 --enable-unicode-properties --enable-pcre16 --enable-pcre32 --disable-static')
		shutit.send('make')
		shutit.send('make install')
		shutit.send('mv -v /usr/lib/libpcre.so.* /lib')
		shutit.send('ln -sfv ../../lib/$(readlink /usr/lib/libpcre.so) /usr/lib/libpcre.so')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/pcre')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return pcre(
		'shutit.tk.sd.pcre.pcre', 158844782.002545,
		description='',
		maintainer='',
		depends=['shutit.tk.setup']
	)


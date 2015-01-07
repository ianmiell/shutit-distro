"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class cpio(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/cpio')
		shutit.send('cd /tmp/build/cpio')
		shutit.get_url('cpio-2.11.tar.bz2',['http://ftp.gnu.org/pub/gnu/cpioasd','ftp://ftp.osuosl.org/.2/gentoo/distfiles/cpio-2.11.tar.bz2'])
		shutit.send('bunzip2 -c cpio-2.11.tar.bz2 | tar -xf -')
		shutit.send('rm cpio-2.11.tar.bz2')
		shutit.send('cd cpio*')
		shutit.send('''sed -i -e '/gets is a/d' gnu/stdio.in.h''')
		shutit.send('./configure --prefix=/usr --bindir=/bin --enable-mt --with-rmt=/usr/libexec/rmt')
		shutit.send('make install')
		shutit.send('make')
		return True 

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/cpio')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return cpio(
		'shutit.tk.sd.cpio.cpio', 158844782.0014,
		description='',
		maintainer='',
		depends=['shutit.tk.setup']
	)


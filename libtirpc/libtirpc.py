"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class libtirpc(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/libtirpc')
		shutit.send('cd /tmp/build/libtirpc')
		shutit.send('wget -qO- http://downloads.sourceforge.net/project/libtirpc/libtirpc/0.2.5/libtirpc-0.2.5.tar.bz2 | bunzip2 -c | tar -xf -')
		shutit.send('cd libtirpc*')
		shutit.send('./configure --prefix=/usr --sysconfdir=/etc --disable-static --disable-gssapi')
		shutit.send('make')
		shutit.send('make install')
		shutit.send('mv -v /usr/lib/libtirpc.so.* /lib')
		shutit.send('ln -sf ../../lib/libtirpc.so.1.0.10 /usr/lib/libtirpc.so')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/libtirpc')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return libtirpc(
		'shutit.tk.sd.libtirpc.libtirpc', 158844782.0234,
		description='',
		maintainer='',
		depends=['shutit.tk.setup']
	)


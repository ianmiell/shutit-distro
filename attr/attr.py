"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class attr(ShutItModule):

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/attr')
		shutit.send('cd /tmp/build/attr')
		shutit.send('wget -qO- http://download.savannah.gnu.org/releases/attr/attr-2.4.47.src.tar.gz | tar -zxf -')
		shutit.send('cd attr*')
		shutit.send('./configure --prefix=/usr --bindir=/bin')
		shutit.send('make')
		shutit.send('make install install-dev install-lib')
		shutit.send('chmod -v 755 /usr/lib/libattr.so')
		shutit.send('mv -v /usr/lib/libattr.so.* /lib')
		shutit.send('ln -sf ../../lib/$(readlink /usr/lib/libattr.so) /usr/lib/libattr.so')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/attr')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return attr(
		'shutit.tk.sd.attr.attr', 158844782.0226,
		description='',
		maintainer='',
		depends=['shutit.tk.setup']
	)


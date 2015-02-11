"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class atk(ShutItModule):

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/atk')
		shutit.send('cd /tmp/build/atk')
		shutit.send('wget -qO- http://ftp.gnome.org/pub/gnome/sources/atk/2.12/atk-2.12.0.tar.xz | xz -d | tar -xf -')
		shutit.send('cd atk*')
		shutit.send('./configure --prefix=/usr')
		shutit.send('make')
		shutit.send('make install')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/atk')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return atk(
		'shutit.tk.sd.atk.atk', 158844782.0107,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.glib.glib']
	)


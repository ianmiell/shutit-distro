"""ShutIt module. See http://shutit.tk/
"""

from shutit_module import ShutItModule


class xmlto(ShutItModule):

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/xmlto')
		shutit.send('cd /tmp/build/xmlto')
		shutit.send('wget -qO- https://fedorahosted.org/releases/x/m/xmlto/xmlto-' + shutit.cfg[self.module_id]['version'] + '.tar.bz2 | bunzip2 -c | tar -xf -')
		shutit.send('cd xmlto-' + shutit.cfg[self.module_id]['version'])
		shutit.send('./configure --prefix=/usr')
		shutit.send('make')
		shutit.send('make install')
		return True

	def get_config(self, shutit):
		shutit.get_config(self.module_id,'version','0.0.26')
		return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/xmlto')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return xmlto(
		'shutit.tk.sd.xmlto.xmlto', 158844782.0055,
		description='',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.make_certs.make_certs']
	)


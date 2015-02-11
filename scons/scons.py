"""ShutIt module. See http://shutit.tk/
"""

from shutit_module import ShutItModule


class scons(ShutItModule):

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/scons')
		shutit.send('cd /tmp/build/scons')
		shutit.send('wget -qO- http://sourceforge.net/projects/scons/files/scons/2.3.4/scons-2.3.4.tar.gz | tar -zxf -')
		shutit.send('cd scons-*')
		shutit.send('python setup.py install --prefix=/usr --standard-lib --optimize=1 --install-data=/usr/share')
		return True

	#def get_config(self, shutit):
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/scons')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return scons(
		'shutit.tk.sd.scons.scons', 158844782.0069,
		description='',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.setup']
	)


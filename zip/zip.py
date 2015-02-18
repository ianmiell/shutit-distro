"""ShutIt module. See http://shutit.tk/
"""

from shutit_module import ShutItModule


class zip(ShutItModule):

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/zip')
		shutit.send('cd /tmp/build/zip')
		f = 'zip30.tar.gz'
		shutit.get_url(f,['http://pkgs.fedoraproject.org/repo/pkgs/zip/zip30.tar.gz/7b74551e63f8ee6aab6fbc86676c0d37/',''])
		shutit.send('tar -zxf ' + f)
		shutit.send('cd zip*')
		shutit.send('make -f unix/Makefile generic_gcc')
		shutit.send('make prefix=/usr MANDIR=/usr/share/man/man1 -f unix/Makefile install')
		return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/zip')
		return True

def module():
	return zip(
		'shutit.tk.sd.zip.zip', 158844782.00801,
		description='',
		maintainer='',
		depends=['shutit.tk.setup']
	)


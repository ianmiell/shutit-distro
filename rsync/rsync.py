"""ShutIt module. See http://shutit.tk/
"""

from shutit_module import ShutItModule


class rsync(ShutItModule):

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/rsync')
		shutit.send('cd /tmp/build/rsync')
		shutit.send('wget -qO- http://rsync.samba.org/ftp/rsync/src/rsync-' + shutit.cfg[self.module_id]['version'] + '.tar.gz | tar -zxf -')
		shutit.send('cd rsync*')
		shutit.send('./configure --prefix=/usr')
		shutit.send('make')
		shutit.send('make install')
		return True

	def get_config(self, shutit):
		shutit.get_config(self.module_id,'version','3.1.1')
		return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/rsync')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return rsync(
		'shutit.tk.sd.rsync.rsync', 158844782.003,
		description='',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.setup']
	)


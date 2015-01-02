"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class lsof(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/lsof')
		shutit.send('cd /tmp/build/lsof')
		shutit.send('wget -qO- ftp://sunsite.ualberta.ca/pub/Mirror/lsof/lsof_4.88.tar.bz2 | bunzip2 -c | tar -xf -')
		shutit.send('cd lsof*')
		shutit.send('tar -xf lsof_4.88_src.tar')
		shutit.send('cd lsof_4.88_src')
		shutit.send('./Configure -n linux')
		shutit.send('make CFGL="-L./lib -ltirpc"')
		shutit.send('install -v -m0755 -o root -g root lsof /usr/bin')
		shutit.send('install -v lsof.8 /usr/share/man/man8')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/lsof')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return lsof(
		'shutit.tk.sd.lsof.lsof', 158844782.0235,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.libtirpc.libtirpc']
	)


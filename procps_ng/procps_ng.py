"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class procps_ng(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/procps_ng')
		shutit.send('cd /tmp/build/procps_ng')
		shutit.send('wget -qO- http://sourceforge.net/projects/procps-ng/files/Production/procps-ng-3.3.10.tar.xz | xz -d | tar -xf -')
		shutit.send('cd procps-ng*')
		shutit.send('./configure --prefix=/usr --exec-prefix= --libdir=/usr/lib --docdir=/usr/share/doc/procps-ng-3.3.10 --disable-static --disable-kill')
		shutit.send('make')
		shutit.send(r'''sed -i -r 's|(pmap_initname)\\\$|\1|' testsuite/pmap.test/pmap.exp''')
		shutit.send('make check')
		shutit.send('make install')
		shutit.send('mv -v /usr/bin/pidof /bin')
		shutit.send('mv -v /usr/lib/libprocps.so.* /lib')
		shutit.send('ln -sfv ../../lib/$(readlink /usr/lib/libprocps.so) /usr/lib/libprocps.so')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	#def check_ready(self, shutit):
	#	return True
	
	#def start(self, shutit):
	#	return True

	#def stop(self, shutit):
	#	return True

	#def finalize(self, shutit):
	#	return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return procps_ng(
		'shutit.tk.sd.procps_ng.procps_ng', 158844782.00251,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.pkg_config.pkg_config']
	)


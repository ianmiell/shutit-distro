"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class nspr(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/nspr')
		shutit.send('cd /tmp/build/nspr')
		shutit.send('wget -qO- http://ftp.mozilla.org/pub/mozilla.org/nspr/releases/v4.10.7/src/nspr-4.10.7.tar.gz | tar -zxf -')
		shutit.send('cd nspr*')
		shutit.send('cd nspr')
		shutit.send(r'''sed -ri 's#^(RELEASE_BINS =).*#\1#' pr/src/misc/Makefile.in''')
		shutit.send('''sed -i 's#$(LIBRARY) ##' config/rules.mk''')
		shutit.send('./configure --prefix=/usr --with-mozilla --with-pthreads $([ $(uname -m) = x86_64 ] && echo --enable-64bit)')
		shutit.send('make')
		shutit.send('make install')
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
	return nspr(
		'shutit.tk.sd.nspr.nspr', 158844782.0129,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.pkg_config.pkg_config']
	)


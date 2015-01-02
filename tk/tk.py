"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class tk(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/tk')
		shutit.send('cd /tmp/build/tk')
		shutit.send('wget -qO- http://downloads.sourceforge.net/tcl/tk8.6.3-src.tar.gz | tar -zxf -')
		shutit.send('cd tk8*')
		shutit.send('cd unix')
		shutit.send('./configure --prefix=/usr --mandir=/usr/share/man $([ $(uname -m) = x86_64 ] && echo --enable-64bit)')
		shutit.send('make')
		shutit.send(r'''sed -e "s@^\(TK_SRC_DIR='\).*@\1/usr/include'@" -e "/TK_B/s@='\(-L\)\?.*unix@='\1/usr/lib@" -i tkConfig.sh''')
		shutit.send('make install')
		shutit.send('make install-private-headers')
		shutit.send('ln -v -sf wish8.6 /usr/bin/wish')
		shutit.send('chmod -v 755 /usr/lib/libtk8.6.so')
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

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/tk')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return tk(
		'shutit.tk.sd.tk.tk', 158844782.0021,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.tcl.tcl','xorg required']
	)


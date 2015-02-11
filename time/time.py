"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class time(ShutItModule):

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/time')
		shutit.send('cd /tmp/build/time')
		shutit.send('wget -qO- http://ftp.gnu.org/gnu/time/time-1.7.tar.gz | tar -zxf -')
		shutit.send('cd time*')
		shutit.send('''sed -i 's/$(ACLOCAL)//' Makefile.in''')
		shutit.send('''sed -i 's/lu", ptok ((UL) resp->ru.ru_maxrss)/ld", resp->ru.ru_maxrss/' time.c''')
		shutit.send('./configure --prefix=/usr --infodir=/usr/share/info')
		shutit.send('make')
		shutit.send('make install')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/time')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return time(
		'shutit.tk.sd.time.time', 158844782.0238,
		description='',
		maintainer='',
		depends=['shutit.tk.setup']
	)


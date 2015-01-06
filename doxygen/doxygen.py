"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class doxygen(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/doxygen')
		shutit.send('cd /tmp/build/doxygen')
		shutit.send('wget -qO- http://ftp.stack.nl/pub/doxygen/doxygen-1.8.9.src.tar.gz | tar -zxf -')
		shutit.send('cd doxygen*')
		shutit.send('./configure --prefix /usr --docdir /usr/share/doc/doxygen-1.8.9')
		shutit.send('make')
		shutit.send('make MAN1DIR=share/man/man1 install')
		return True

	def get_config(self, shutit):
		return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/doxygen')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return doxygen(
		'shutit.tk.sd.doxygen.doxygen', 158844782.0277,
		description='',
		maintainer='',
		depends=['shutit.tk.setup']
#Optional deps: Graphviz-2.38.0, ghostscript-9.15, LLVM-3.5.0 (with clang), Python-2.7.9 or Python-3.4.2, Qt-4.8.6 (for doxywizard), texlive-20140525, and xapian-1.2.19 (for doxyindexer) 
	)


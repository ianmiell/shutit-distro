"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class doxygen(ShutItModule):

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
		depends=['shutit.tk.sd.llvm.llvm','shutit.tk.sd.qt4.qt4']
#Optional deps: Graphviz-2.38.0, ghostscript-9.15, texlive-20140525, and xapian-1.2.19 (for doxyindexer) 
	)


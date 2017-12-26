"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class boost(ShutItModule):

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/boost')
		shutit.send('cd /tmp/build/boost')
		shutit.get_url('boost_1_57_0.tar.bz2',['http://ftp.osuosl.org/pub/blfs/svn/b','http://downloads.sourceforge.net/boost'])
		shutit.send('bunzip2 -c boost_1_57_0.tar.bz2 | tar -xf -')
		shutit.send('cd boost*')
		shutit.send('''sed -e '1 i#ifndef Q_MOC_RUN' -e '$ a#endif' -i boost/type_traits/detail/has_binary_operator.hpp''')
		shutit.send('./bootstrap.sh --prefix=/usr')
		shutit.send('./b2 stage threading=multi') #--link=shared omitted as required by eg thrift
		shutit.send('./b2 install threading=multi') #--link=shared omitted as required by eg thrift
		return True

	def is_installed(self,shutit):
		return False
	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/boost')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return boost(
		'shutit.tk.sd.boost.boost', 158844782.0233,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.icu.icu']
	)


"""ShutIt module. See http://shutit.tk/
"""

from shutit_module import ShutItModule


class scons(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')


	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/scons')
		shutit.send('cd /tmp/build/scons')
		shutit.send('wget -qO- http://sourceforge.net/projects/scons/files/scons/2.3.4/scons-2.3.4.tar.gz | tar -zxf -')
		shutit.send('cd scons-*')
		#shutit.send('mkdir -p /tmp/pip_build_root/lxml/src/lxml/includes')
		#shutit.send('cp -r /tmp/build/libxml2/libxml2-2.9.2/include/libxml /tmp/pip_build_root/lxml/src/lxml/includes')
		#shutit.send('cp -r /tmp/build/libxslt/libxslt-1.1.28 /tmp/pip_build_root/lxml/src/lxml/includes')
		#shutit.send('pip install lxml')
		shutit.send('python setup.py install --prefix=/usr --standard-lib --optimize=1 --install-data=/usr/share')
		return True

	#def get_config(self, shutit):
	#	return True

	#def check_ready(self, shutit):
	#	return True
	
	#def start(self, shutit):
	#	return True

	#def stop(self, shutit):
	#	return True

	def finalize(self, shutit):
		#shutit.send('rm -rf
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return scons(
		'shutit.tk.sd.scons.scons', 158844782.0069,
		description='',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.libxslt.libxslt','shutit.tk.sd.python2.python2']
	)


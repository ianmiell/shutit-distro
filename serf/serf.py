"""ShutIt module. See http://shutit.tk/
"""

from shutit_module import ShutItModule


class serf(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')


	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/serf')
		shutit.send('cd /tmp/build/serf')
		shutit.send('wget -qO- http://serf.googlecode.com/svn/src_releases/serf-1.3.8.tar.bz2 | bunzip2 - | tar -xf -')
		shutit.send('pushd serf-*')
		shutit.send('sed -i "/Append/s:RPATH=libdir,::"   SConstruct')
		shutit.send('sed -i "/Default/s:lib_static,::"    SConstruct && sed -i "/Alias/s:install_static,::"  SConstruct')
		shutit.send('scons PREFIX=/usr')
		shutit.send('scons PREFIX=/usr install')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/serf')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return serf(
		'shutit.tk.sd.serf.serf', 158844782.007,
		description='',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.apache_portable_runtime_util.apache_portable_runtime_util','shutit.tk.sd.scons.scons']
	)


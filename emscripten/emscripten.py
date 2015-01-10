"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class emscripten(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		# http://kripken.github.io/emscripten-site/docs/getting_started/downloads.html#sdk-download-and-install
		# then: http://kripken.github.io/emscripten-site/docs/building_from_source/building_emscripten_from_source_on_linux.html
		shutit.send('mkdir -p /opt')
		shutit.send('cd /opt')
		shutit.send('wget -qO- https://s3.amazonaws.com/mozilla-games/emscripten/releases/emsdk-portable.tar.gz | tar -zxf -')
		shutit.send('cd emsdk*')
		shutit.send('./emsdk update')
		shutit.send('./emsdk install latest')
		shutit.send('./emsdk activate latest')
		shutit.send('source ./emsdk_env.sh')
		return True

	def get_config(self, shutit):
		return True

	def finalize(self, shutit):
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return emscripten(
		'shutit.tk.sd.emscripten.emscripten', 158844782.0276,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.fastcomp.fastcomp','shutit.tk.sd.make_certs.make_certs','shutit.tk.sd.git.git','shutit.tk.sd.node.node','shutit.tk.sd.openjdk.openjdk','shutit.tk.sd.cmake.cmake']
	)


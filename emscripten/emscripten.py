"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class emscripten(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/emscripten')
		shutit.send('cd /tmp/build/emscripten')
		shutit.send('wget -qO- https://s3.amazonaws.com/mozilla-games/emscripten/releases/emsdk-portable.tar.gz | tar -zxf -')
		shutit.send('cd emsdk*')
		shutit.pause_point('emscripten build')
		# http://kripken.github.io/emscripten-site/docs/getting_started/downloads.html#sdk-download-and-install
		# then: http://kripken.github.io/emscripten-site/docs/building_from_source/building_emscripten_from_source_on_linux.html
		return True

	def get_config(self, shutit):
		return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/emscripten')
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


"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class fastcomp(ShutItModule):

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/fastcomp')
		shutit.send('cd /tmp/build/fastcomp')
		shutit.send('git clone https://github.com/kripken/emscripten-fastcomp')
		shutit.send('cd emscripten-fastcomp')
		shutit.send('git clone https://github.com/kripken/emscripten-fastcomp-clang tools/clang')
		shutit.send('mkdir build')
		shutit.send('cd build')
		shutit.send('../configure --enable-optimized --disable-assertions --enable-targets=host,js --prefix=/usr')
		shutit.send('make')
		shutit.send('make install')
		shutit.send('''echo "LLVM_ROOT='/usr/bin/emscripten-fastcomp/build/bin'" > ~/.emscripten''')
		return True

	def get_config(self, shutit):
		return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/fastcomp')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return fastcomp(
		'shutit.tk.sd.fastcomp.fastcomp', 158844782.0275,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.git.git'],
		conflicts=['shutit.tk.sd.llvm.llvm']
	)


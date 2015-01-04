"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class llvm(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/llvm')
		shutit.send('cd /tmp/build/llvm')
		shutit.send('wget http://llvm.org/releases/3.5.0/cfe-3.5.0.src.tar.xz')
		shutit.send('wget http://llvm.org/releases/3.5.0/compiler-rt-3.5.0.src.tar.xz')
		shutit.send('wget -qO- http://llvm.org/releases/' + shutit.cfg[self.module_id]['version'] + '/llvm-' + shutit.cfg[self.module_id]['version'] + '.src.tar.xz | xz -d | tar -xf -')
		shutit.send('cd llvm-*')
		shutit.send('tar -xf ../cfe-3.5.0.src.tar.xz -C tools')
		shutit.send('tar -xf ../compiler-rt-3.5.0.src.tar.xz -C projects')
		shutit.send('mv tools/cfe-3.5.0.src tools/clang')
		shutit.send('mv projects/compiler-rt-3.5.0.src projects/compiler-rt')
		shutit.send('sed -e "s:/docs/llvm:/share/doc/llvm-' + shutit.cfg[self.module_id]['version'] + ':" -i Makefile.config.in')
		shutit.send('CC=gcc CXX=g++ ./configure --prefix=/usr --sysconfdir=/etc --enable-libffi --enable-optimized --enable-shared --disable-assertions')
		shutit.send('make')
		shutit.send('make install')
		shutit.send('chmod -v 644 /usr/lib/libclang*.a')
		shutit.send('chmod -v 644 /usr/lib/libLLVM*.a')
		shutit.send('chmod -v 644 /usr/lib/libLTO*.a')
		shutit.send('install -v -dm755 /usr/lib/clang-analyzer')
		shutit.send('cp -rfv tools/clang/tools/scan-build /usr/lib/clang-analyzer/')
		shutit.send('ln -sfv ../lib/clang-analyzer/scan-build/scan-build /usr/bin/')
		shutit.send('cp -rfv tools/clang/tools/scan-view /usr/lib/clang-analyzer/')
		shutit.send('ln -sfv ../lib/clang-analyzer/scan-view/scan-view /usr/bin/')
		shutit.send('ln -sfv /usr/bin/clang /usr/lib/clang-analyzer/scan-build/')
		shutit.send('mv -v /usr/lib/clang-analyzer/scan-build/scan-build.1 /usr/share/man/man1/')
		return True

	def get_config(self, shutit):
		shutit.get_config(self.module_id,'version','3.5.0')
		return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/llvm')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return llvm(
		'shutit.tk.sd.llvm.llvm', 158844782.0043,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.python2.python2']
	)


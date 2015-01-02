"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class java_binary(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/java_binary')
		shutit.send('cd /tmp/build/java_binary')
		shutit.send('wget -qO- http://anduin.linuxfromscratch.org/files/BLFS/OpenJDK-1.7.0.65/OpenJDK-1.7.0.65-x86_64-bin.tar.xz | xz -d | tar -xf -')
		shutit.send('install -vdm755 /opt/OpenJDK-1.7.0.65-bin')
		shutit.send('mv -v * /opt/OpenJDK-1.7.0.65-bin')
		shutit.send('chown -R root:root /opt/OpenJDK-1.7.0.65-bin')
		shutit.add_to_bashrc('export CLASSPATH=.:/usr/share/java')
		shutit.add_to_bashrc('export JAVA_HOME=/opt/OpenJDK-1.7.0.65-bin/OpenJDK-1.7.0.65-x86_64-bin')
		shutit.add_to_bashrc('export PATH=$PATH:/opt/OpenJDK-1.7.0.65-bin/OpenJDK-1.7.0.65-x86_64-bin/bin')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	#def check_ready(self, shutit):
	#	return True
	
	#def start(self, shutit):
	#	return True

	#def stop(self, shutit):
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/java_binary')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return java_binary(
		'shutit.tk.sd.java_binary.java_binary', 158844782.0122,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.alsa_lib.alsa_lib','shutit.tk.sd.cairo.cairo','shutit.tk.sd.cups.cups','shutit.tk.sd.giflib.giflib','shutit.tk.sd.gtk2.gtk2','shutit.tk.sd.lcms.lcms','shutit.tk.sd.xorg_libs.xorg_libs','shutit.tk.sd.libgcrypt.libgcrypt']
	)


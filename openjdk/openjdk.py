"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class openjdk(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/openjdk')
		shutit.send('cd /tmp/build/openjdk')
		shutit.send('wget -qO- http://icedtea.classpath.org/download/source/icedtea-2.5.2.tar.xz | xz -d | tar -xf -')
		shutit.send('wget -qO- http://icedtea.classpath.org/download/source/icedtea-web-1.5.1.tar.gz | tar -zxf -')
		shutit.send('cd icedtea-2*')
		shutit.send('wget -qO- http://www.linuxfromscratch.org/patches/blfs/7.6/icedtea-2.5.2-add_cacerts-1.patch > ../icedtea-2.5.2-add_cacerts-1.patch')
		shutit.send('wget -qO- http://www.linuxfromscratch.org/patches/blfs/7.6/icedtea-2.5.2-fixed_paths-1.patch > ../icedtea-2.5.2-fixed_paths-1.patch')
		shutit.send('wget -qO- http://www.linuxfromscratch.org/patches/blfs/7.6/icedtea-2.5.2-fix_new_giflib-1.patch > ../icedtea-2.5.2-fix_new_giflib-1.patch')
		shutit.send('wget -qO- http://www.linuxfromscratch.org/patches/blfs/7.6/icedtea-2.5.2-fix_tests-1.patch > ../icedtea-2.5.2-fix_tests-1.patch')
		shutit.send('wget -qO- https://github.com/downloads/mozilla/rhino/rhino1_7R4.zip > ../rhino1_7R4.zip')
		shutit.send('wget http://anduin.linuxfromscratch.org/files/BLFS/OpenJDK-1.7.0.65-2.5.2/corba.tar.bz2')
		shutit.send('wget http://anduin.linuxfromscratch.org/files/BLFS/OpenJDK-1.7.0.65-2.5.2/hotspot.tar.bz2')
		shutit.send('wget http://anduin.linuxfromscratch.org/files/BLFS/OpenJDK-1.7.0.65-2.5.2/openjdk.tar.bz2')
		shutit.send('wget http://anduin.linuxfromscratch.org/files/BLFS/OpenJDK-1.7.0.65-2.5.2/jaxp.tar.bz2')
		shutit.send('wget http://anduin.linuxfromscratch.org/files/BLFS/OpenJDK-1.7.0.65-2.5.2/jaxws.tar.bz2')
		shutit.send('wget http://anduin.linuxfromscratch.org/files/BLFS/OpenJDK-1.7.0.65-2.5.2/langtools.tar.bz2')
		shutit.send('wget http://anduin.linuxfromscratch.org/files/BLFS/OpenJDK-1.7.0.65-2.5.2/jdk.tar.bz2')
		shutit.send('unzip ../rhino1_7R4.zip')
		shutit.send('install -v -d -m755 /usr/share/java')
		shutit.send('install -v -m755 rhino1_7R4/*.jar /usr/share/java')
		shutit.send('patch -Np1 -i ../icedtea-2.5.2-add_cacerts-1.patch')
		shutit.send('patch -Np1 -i ../icedtea-2.5.2-fixed_paths-1.patch')
		shutit.send('patch -Np1 -i ../icedtea-2.5.2-fix_new_giflib-1.patch')
		shutit.send('patch -Np1 -i ../icedtea-2.5.2-fix_tests-1.patch')
#Before proceeding, you should ensure that your environment is properly set for building OpenJDK. First, review the content of the ANT_HOME variable. Second, the PATH variable should contain the paths to the java and ant executables. Last, the CLASSPATH variable should be set as explained on the Java-1.7.0.65 and JUnit-4.11 pages. 
#install procps?
#install findutils
		shutit.send('unset JAVA_HOME')
		shutit.send('./autogen.sh')
		shutit.send('./configure --with-jdk-home=/opt/OpenJDK-1.7.0.65-bin/OpenJDK-1.7.0.65-x86_64-bin --with-version-suffix=SHUTIT --enable-nss --disable-system-kerberos --with-parallel-jobs')
		shutit.send('make')
		shutit.send('chmod 0644 openjdk.build/j2sdk-image/lib/sa-jdi.jar')
		shutit.send('cp -R openjdk.build/j2sdk-image /opt/OpenJDK-1.7.0.65')
		shutit.send('chown -R root:root /opt/OpenJDK-1.7.0.65')
# TODO set up which jdk we want to use
#  There are now two OpenJDK SDKs installed in /opt. You should decide on which one you would like to use as the default. For example if you decide to use the precompiled OpenJDK, do the following as the root user:
#ln -v -nsf OpenJDK-1.7.0.65-bin /opt/jdk
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

	#def finalize(self, shutit):
	#	return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

# TODO: NSS? 
def module():
	return openjdk(
		'shutit.tk.sd.openjdk.openjdk', 158844782.0241,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.java_binary.java_binary','shutit.tk.sd.alsa_lib.alsa_lib','shutit.tk.sd.ant.ant','shutit.tk.sd.cpio.cpio','shutit.tk.sd.cups.cups','shutit.tk.sd.gtk2.gtk2','shutit.tk.sd.giflib.giflib','shutit.tk.sd.which.which','shutit.tk.sd.xorg_libs.xorg_libs','shutit.tk.sd.junit.junit','shutit.tk.sd.nss.nss','shutit.tk.sd.libpng.libpng','shutit.tk.sd.lcms.lcms']
	)


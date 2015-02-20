"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class openjdk(ShutItModule):

	def build(self, shutit):
		shutit.send('mkdir -p /usr/share/java')
		shutit.send('mkdir -p /tmp/build/openjdk')
		shutit.send('cd /tmp/build/openjdk')
		shutit.send('wget -qO- http://hg.openjdk.java.net/jdk8u/jdk8u/archive/jdk8u25-b18.tar.bz2 | bunzip2 -c | tar -xf -')
		shutit.send('cd jdk8*')
		shutit.send('wget -qO- http://anduin.linuxfromscratch.org/files/BLFS/OpenJDK-1.8.0.25/corba.tar.xz | xz -d | tar -xf -')
		shutit.send('wget -qO- http://anduin.linuxfromscratch.org/files/BLFS/OpenJDK-1.8.0.25/hotspot.tar.xz | xz -d | tar -xf -')
		shutit.send('wget -qO- http://anduin.linuxfromscratch.org/files/BLFS/OpenJDK-1.8.0.25/jaxp.tar.xz | xz -d | tar -xf -')
		shutit.send('wget -qO- http://anduin.linuxfromscratch.org/files/BLFS/OpenJDK-1.8.0.25/jaxws.tar.xz | xz -d | tar -xf -')
		shutit.send('wget -qO- http://anduin.linuxfromscratch.org/files/BLFS/OpenJDK-1.8.0.25/langtools.tar.xz | xz -d | tar -xf -')
		shutit.send('wget -qO- http://anduin.linuxfromscratch.org/files/BLFS/OpenJDK-1.8.0.25/jdk.tar.xz | xz -d | tar -xf -')
		shutit.send('wget -qO- http://anduin.linuxfromscratch.org/files/BLFS/OpenJDK-1.8.0.25/nashorn.tar.xz | xz -d | tar -xf -')
		shutit.send(r'''sed -e 's/DGifCloseFile(gif/&, NULL/' -e '/DGifOpen/s/c)/c, NULL)/' -i jdk/src/share/native/sun/awt/splashscreen/splashscreen_gif.c''')
		shutit.send(r'''sed 's/\([ \t]\)\]\([^\]\)/\1I]\2/g' -i hotspot/make/linux/makefiles/adjust-mflags.sh''')
		shutit.send('unset JAVA_HOME')
		shutit.send('sh ./configure --with-update-version=25 --with-build-number=b18 --with-milestone=BLFS --enable-unlimited-crypto --with-zlib=system --with-giflib=system')
		shutit.send('mkdir -p /usr/share/java') # required to get make to work
		shutit.send('make DEBUG_BINARIES=true all')
		shutit.send(r'find build/*/images/j2sdk-image -iname \*.jar -exec chmod a+r {} \;')
		shutit.send('chmod a+r build/*/images/j2sdk-image/lib/ct.sym')
		shutit.send('find build/*/images/j2sdk-image -iname \*.diz -delete')
		shutit.send('find build/*/images/j2sdk-image -iname \*.debuginfo -delete')
		shutit.send('cp -R build/*/images/j2sdk-image /opt/OpenJDK-1.8.0.25')
		shutit.send('chown -R root:root /opt/OpenJDK-1.8.0.25')
		shutit.send('mkdir -pv /usr/share/applications')
		shutit.send('ln -v -nsf /opt/OpenJDK-1.8.0.25 /opt/jdk')
		shutit.send_host_file('/etc/profile.d/openjdk.sh','context/etc/profile.d/openjdk.sh')
		shutit.send_host_file('/etc/profile.d/extrapaths.sh','context/etc/profile.d/extrapaths.sh')
		shutit.send('mkdir -p /var/cache/man')
		shutit.send('mandb -c /opt/jdk/man')
		shutit.send('mkdir -p /opt/jdk/bin')
		shutit.send_host_file('/opt/jdk/bin/mkcacerts','context/opt/jdk/bin/mkcacerts')
		shutit.send('chmod -c 0755 /opt/jdk/bin/mkcacerts')
		shutit.send('/opt/jdk/bin/mkcacerts -d "/etc/ssl/certs/" -k "/opt/jdk/bin/keytool" -s "/usr/bin/openssl" -o "/opt/jdk/jre/lib/security/cacerts"')
		shutit.send('cd /opt/jdk')
		shutit.send('bin/keytool -list -keystore jre/lib/security/cacerts',expect='assword')
		shutit.send('')
		return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/openjdk')
		return True

def module():
	return openjdk(
		'shutit.tk.sd.openjdk.openjdk', 158844782.0241,
		description='Java built from java binary',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.junit.junit','shutit.tk.sd.alsa_lib.alsa_lib','shutit.tk.sd.cpio.cpio','shutit.tk.sd.cups.cups','shutit.tk.sd.which.which','shutit.tk.sd.xorg_libs.xorg_libs','shutit.tk.sd.zip.zip','shutit.tk.sd.giflib.giflib']
	)


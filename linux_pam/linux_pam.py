"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class linux_pam(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		# First install cracklib and re-install shadow - these are tightly coupled steps
		shutit.send('mkdir -p /tmp/build/cracklib')
		shutit.send('cd /tmp/build/cracklib')
		shutit.send('wget -qO- http://downloads.sourceforge.net/cracklib/cracklib-2.9.2.tar.gz | tar -zxf -')
		shutit.send('wget http://downloads.sourceforge.net/cracklib/cracklib-words-20080507.gz')
		shutit.send('cd cracklib*')
		shutit.send('''sed -i '/skipping/d' util/packer.c''')
		shutit.send('./configure --prefix=/usr --disable-static --with-default-dict=/lib/cracklib/pw_dict')
		shutit.send('make')
		shutit.send('make install')
		shutit.send('mv -v /usr/lib/libcrack.so.* /lib')
		shutit.send('ln -sfv ../../lib/$(readlink /usr/lib/libcrack.so) /usr/lib/libcrack.so')
		shutit.send('install -v -m644 -D ../cracklib-words-20080507.gz /usr/share/dict/cracklib-words.gz')
		shutit.send('gunzip -v /usr/share/dict/cracklib-words.gz')
		shutit.send('ln -v -sf cracklib-words /usr/share/dict/words')
		shutit.send('echo $(hostname) >> /usr/share/dict/cracklib-extra-words')
		shutit.send('install -v -m755 -d /lib/cracklib')
		shutit.send('create-cracklib-dict /usr/share/dict/cracklib-words /usr/share/dict/cracklib-extra-words')
		shutit.send('wget -qO- http://pkg-shadow.alioth.debian.org/releases/shadow-4.2.1.tar.xz | xz -d | tar -xf -')
		shutit.send('cd shadow-*')
		shutit.send('''sed -i 's/groups$(EXEEXT) //' src/Makefile.in''')
		shutit.send(r'''find man -name Makefile.in -exec sed -i 's/groups\.1 / /' {} \;''')
		shutit.send(r'''sed -i -e 's@#ENCRYPT_METHOD DES@ENCRYPT_METHOD SHA512@' -e 's@/var/spool/mail@/var/mail@' etc/login.defs''')
		shutit.send('''sed -i 's/1000/999/' etc/useradd''')
		shutit.send('./configure --sysconfdir=/etc --with-group-name-max-length=32')
		shutit.send('make')
		shutit.send('make install')
		shutit.send('mv -v /usr/bin/passwd /bin')
		# Now install linux pam
		shutit.send('mkdir -p /tmp/build/linux_pam')
		shutit.send('cd /tmp/build/linux_pam')
		shutit.send('wget -qO- http://linux-pam.org/library/Linux-PAM-1.1.8.tar.bz2 | bunzip2 -c | tar -xf -')
		shutit.send('cd Linux*')
		shutit.send('./configure --prefix=/usr --sysconfdir=/etc --libdir=/usr/lib --enable-securedir=/lib/security --docdir=/usr/share/doc/Linux-PAM-1.1.8')
		shutit.send('make')
		shutit.send('install -v -m755 -d /etc/pam.d')
		shutit.run_script('''cat > /etc/pam.d/other << "EOF"
			auth     required       pam_deny.so
			account  required       pam_deny.so
			password required       pam_deny.so
			session  required       pam_deny.so
		EOF''')
		shutit.send('rm -rfv /etc/pam.d')
		shutit.send('make install')
		shutit.send('chmod -v 4755 /sbin/unix_chkpwd')
		shutit.send('mv -v /usr/lib/libpam.so.* /lib')
		shutit.send('ln -sfv ../../lib/$(readlink /usr/lib/libpam.so) /usr/lib/libpam.so')
		shutit.send('mv -v /usr/lib/libpam_misc.so.* /lib')
		shutit.send('ln -sfv ../../lib/$(readlink /usr/lib/libpam_misc.so) /usr/lib/libpam_misc.so')
		shutit.send('mv -v /usr/lib/libpamc.so.* /lib')
		shutit.send('ln -sfv ../../lib/$(readlink /usr/lib/libpamc.so) /usr/lib/libpamc.so')
		# From here http://www.linuxfromscratch.org/blfs/view/svn/postlfs/shadow.html
 		# Configuring Linux-PAM to Work with Shadow 
		shutit.send('''install -v -m644 /etc/login.defs /etc/login.defs.orig''')
		shutit.send('''sed -i "s/^FAIL_DELAY/# &/" /etc/login.defs''')
		shutit.send('''sed -i "s/^FAILLOG_ENAB/# &/" /etc/login.defs''')
		shutit.send('''sed -i "s/^LASTLOG_ENAB/# &/" /etc/login.defs''')
		shutit.send('''sed -i "s/^MAIL_CHECK_ENAB/# &/" /etc/login.defs''')
		shutit.send('''sed -i "s/^OBSCURE_CHECKS_ENAB/# &/" /etc/login.defs''')
		shutit.send('''sed -i "s/^PORTTIME_CHECKS_ENAB/# &/" /etc/login.defs''')
		shutit.send('''sed -i "s/^QUOTAS_ENAB/# &/" /etc/login.defs''')
		shutit.send('''sed -i "s/^CONSOLE MOTD_FILE/# &/" /etc/login.defs''')
		shutit.send('''sed -i "s/^FTMP_FILE NOLOGINS_FILE/# &/" /etc/login.defs''')
		shutit.send('''sed -i "s/^ENV_HZ PASS_MIN_LEN/# &/" /etc/login.defs''')
		shutit.send('''sed -i "s/^SU_WHEEL_ONLY/# &/" /etc/login.defs''')
		shutit.send('''sed -i "s/^CRACKLIB_DICTPATH/# &/" /etc/login.defs''')
		shutit.send('''sed -i "s/^PASS_CHANGE_TRIES/# &/" /etc/login.defs''')
		shutit.send('''sed -i "s/^PASS_ALWAYS_WARN/# &/" /etc/login.defs''')
		shutit.send('''sed -i "s/^CHFN_AUTH ENCRYPT_METHOD/# &/" /etc/login.defs''')
		shutit.send('''sed -i "s/^ENVIRON_FILE/# &/" /etc/login.defs''')
		shutit.send('mkdir -p /etc/pam.d')
		shutit.add_line_to_file('/etc/pam.d/system-account','account   required    pam_unix.so')
		shutit.add_line_to_file('/etc/pam.d/system-auth','auth   required    pam_unix.so')
		shutit.send_host_file('/etc/pam.d/system-password','context/etc/pam.d/system-password')
		shutit.add_line_to_file('/etc/pam.d/system-session','session   required    pam_unix.so')
		shutit.send_host_file('/etc/pam.d/login','context/etc/pam.d/login')
		shutit.add_line_to_file('/etc/pam.d/passwd','password   include    system-password')
		shutit.send_host_file('/etc/pam.d/su','context/etc/pam.d/su')
		shutit.send_host_file('/etc/pam.d/chage','context/etc/pam.d/chage')
		shutit.send_host_file('/etc/pam.d/other','context/etc/pam.d/other')
		shutit.run_script('''for PROGRAM in chfn chgpasswd chpasswd chsh groupadd groupdel groupmems groupmod newusers useradd userdel usermod
		do
		    install -v -m644 /etc/pam.d/chage /etc/pam.d/${PROGRAM}
		    sed -i "s/chage/$PROGRAM/" /etc/pam.d/${PROGRAM}
		done''')
		shutit.send('[ -f /etc/login.access ] && mv -v /etc/login.access{,.NOUSE}')
		shutit.send('[ -f /etc/limits ] && mv -v /etc/limits{,.NOUSE}')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/linux_pam')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return linux_pam(
		'shutit.tk.sd.linux_pam.linux_pam', 158844782.025,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.berkeleydb.berkeleydb','shutit.tk.sd.libtirpc.libtirpc']
	)


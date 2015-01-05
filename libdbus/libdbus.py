"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class libdbus(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		import sd_util
		sd_util.setup_x_environment(shutit)
		shutit.send('mkdir -p /tmp/build/libdbus')
		shutit.send('cd /tmp/build/libdbus')
		shutit.send('wget -qO- http://dbus.freedesktop.org/releases/dbus/dbus-1.8.12.tar.gz | tar -zxf -')
		shutit.send('cd dbus*')
		#shutit.send('groupadd -g 18 messagebus') # already there.
		#shutit.send('useradd -c "D-Bus Message Daemon User" -d /var/run/dbus -u 18 -g messagebus -s /bin/false messagebus') # already there.
		shutit.send('./configure --prefix=/usr --sysconfdir=/etc --localstatedir=/var --disable-doxygen-docs --disable-static --disable-systemd --without-systemdsystemunitdir --with-console-auth-dir=/run/console/ --docdir=/usr/share/doc/dbus-1.8.12')
		shutit.send('make')
		shutit.send('make install')
		shutit.send('dbus-uuidgen --ensure')
		shutit.send_host_file('/etc/dbus-1/session-local.conf','context/etc/dbus-1/session-local.conf')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/libdbus')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return libdbus(
		'shutit.tk.sd.libdbus.libdbus', 158844782.012102,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.xorg_libs.xorg_libs']
	)


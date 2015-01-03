"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class xinetd(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/xinetd')
		shutit.send('cd /tmp/build/xinetd')
		shutit.send('wget -qO- ftp://anduin.linuxfromscratch.org/BLFS/svn/x/xinetd-2.3.15.tar.gz | tar -zxf -')
		shutit.send('cd xinetd*')
		shutit.send('sed -i -e "s/exec_server/child_process/" xinetd/builtins.c')
		shutit.send('sed -i -e "/register unsigned count/s/register//" xinetd/itox.c')
		shutit.send('./configure --prefix=/usr --mandir=/usr/share/man --with-loadavg')
		shutit.send('make')
		shutit.send('make install')
		shutit.send_host_file('/etc/xinetd.conf','context/etc/xinetd.conf')
		shutit.send('install -v -d -m755 /etc/xinetd.d')
		shutit.send_host_file('/etc/xinetd.d/systat','context/etc/xinetd.d/systat')
		shutit.send_host_file('/etc/xinetd.d/chargen','context/etc/xinetd.d/chargen')
		shutit.send_host_file('/etc/xinetd.d/daytime','context/etc/xinetd.d/daytime')
		shutit.send_host_file('/etc/xinetd.d/time','context/etc/xinetd.d/time')
		# not doing boot scripts
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/xinetd')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return xinetd(
		'shutit.tk.sd.xinetd.xinetd', 158844782.0252,
		description='',
		maintainer='',
		depends=['shutit.tk.setup']
	)


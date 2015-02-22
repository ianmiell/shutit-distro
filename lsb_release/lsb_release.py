"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class lsb_release(ShutItModule):

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/lsb_release')
		shutit.send('cd /tmp/build/lsb_release')
		shutit.get_url('lsb-release-1.4.tar.gz',['http://sourceforge.net/projects/lsb/files/lsb_release/1.4'])
		shutit.send('tar -zxf lsb-release-1.4.tar.gz')
		shutit.send('cd lsb*')
		shutit.send('sed -i "s|n/a|unavailable|" lsb_release')
		shutit.send('./help2man -N --include ./lsb_release.examples --alt_version_key=program_version ./lsb_release > lsb_release.1')
		shutit.send('install -v -m 644 lsb_release.1 /usr/share/man/man1/lsb_release.1')
		shutit.send('install -v -m 755 lsb_release /usr/bin/lsb_release')
		return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/lsb_release')
		return True


def module():
	return lsb_release(
		'shutit.tk.sd.lsb_release.lsb_release', 158844782.0012135,
		description='lsb release',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.setup']
	)


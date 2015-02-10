"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class tcl(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/tcl')
		shutit.send('cd /tmp/build/tcl')
		shutit.get_url('tcl8.6.3-src.tar.gz',['ftp://ftp.tcl.tk/pub/tcl/tcl8_6','http://downloads.sourceforge.net/tcl'])
		shutit.send('tar -zxf tcl8.6.3-src.tar.gz')
		shutit.send('cd tcl8*')
		shutit.send('export SRCDIR=`pwd`')
		shutit.send('cd unix')
		shutit.send('./configure --prefix=/usr --without-tzdata --mandir=/usr/share/man $([ $(uname -m) = x86_64 ] && echo --enable-64bit)')
		shutit.send('make')
		shutit.send('sed -e "s#$SRCDIR/unix#/usr/lib#" -e "s#$SRCDIR#/usr/include#" -i tclConfig.sh')
		shutit.send('sed -e "s#$SRCDIR/unix/pkgs/tdbc1.0.2#/usr/lib/tdbc1.0.2#" -e "s#$SRCDIR/pkgs/tdbc1.0.2/generic#/usr/include#" -e "s#$SRCDIR/pkgs/tdbc1.0.2/library#/usr/lib/tcl8.6#" -e "s#$SRCDIR/pkgs/tdbc1.0.2#/usr/include#" -i pkgs/tdbc1.0.2/tdbcConfig.sh')
		shutit.send('sed -e "s#$SRCDIR/unix/pkgs/itcl4.0.2#/usr/lib/itcl4.0.2#" -e "s#$SRCDIR/pkgs/itcl4.0.2/generic#/usr/include#" -e "s#$SRCDIR/pkgs/itcl4.0.2#/usr/include#" -i pkgs/itcl4.0.2/itclConfig.sh')
		shutit.send('unset SRCDIR')
		shutit.send('make install')
		shutit.send('make install-private-headers')
		shutit.send('ln -v -sf tclsh8.6 /usr/bin/tclsh')
		shutit.send('chmod -v 755 /usr/lib/libtcl8.6.so')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/tcl')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return tcl(
		'shutit.tk.sd.tcl.tcl', 158844782.002,
		description='',
		maintainer='',
		depends=['shutit.tk.setup']
	)


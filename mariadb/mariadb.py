"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class mariadb(ShutItModule):


	def is_installed(self, shutit):
		return False


	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/mariadb')
		shutit.send('cd /tmp/build/mariadb')
		shutit.send('wget -qO- https://downloads.mariadb.org/interstitial/mariadb-10.0.15/source/mariadb-10.0.15.tar.gz | tar -zxf -')
		shutit.send('cd mariadb*')
		shutit.send('groupadd -g 40 mysql')
		shutit.send('useradd -c "MySQL Server" -d /srv/mysql -g mysql -s /bin/false -u 40 mysql')
		shutit.send('sed -i "s@data/test@\${INSTALL_MYSQLTESTDIR}@g" sql/CMakeLists.txt')
		shutit.send('sed -i "s/srv_buf_size/srv_sort_buf_size/" storage/innobase/row/row0log.cc')
		shutit.send('mkdir build')
		shutit.send('cd build')
		shutit.send('cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr -DINSTALL_DOCDIR=share/doc/mariadb-10.0.15 -DINSTALL_DOCREADMEDIR=share/doc/mariadb-10.0.15 -DINSTALL_MANDIR=share/man -DINSTALL_MYSQLSHAREDIR=share/mysql -DINSTALL_MYSQLTESTDIR=share/mysql/test -DINSTALL_PLUGINDIR=lib/mysql/plugin -DINSTALL_SBINDIR=sbin -DINSTALL_SCRIPTDIR=bin -DINSTALL_SQLBENCHDIR=share/mysql/bench -DINSTALL_SUPPORTFILESDIR=share/mysql -DMYSQL_DATADIR=/srv/mysql -DMYSQL_UNIX_ADDR=/run/mysqld/mysqld.sock -DWITH_EXTRA_CHARSETS=complex -DWITH_EMBEDDED_SERVER=ON -DTOKUDB_OK=0 ..')
		shutit.send('make')
		shutit.send('make install')
		shutit.send('install -v -dm 755 /etc/mysql')
		shutit.send_host_file('/etc/mysql/my.cnf','context/etc/mysql/my.cnf')
		shutit.send('mysql_install_db --basedir=/usr --datadir=/srv/mysql --user=mysql')
		shutit.send('chown -R mysql:mysql /srv/mysql')
		shutit.send('install -v -m755 -o mysql -g mysql -d /run/mysqld')
		shutit.send('mysqld_safe --user=mysql 2>&1 >/dev/null &')
		shutit.send('mysqladmin -u root password',expect='assword')
		shutit.send('mysqlpass')
		shutit.send('mysqladmin -p shutdown')
		return True

	#def get_config(self, shutit):
	#	return True

	#def check_ready(self, shutit):
	#	return True
	
	#def start(self, shutit):
	#	return True

	#def stop(self, shutit):
	#    return True
	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/mariadb')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return mariadb(
		'shutit.tk.sd.mariadb.mariadb', 158844782.0284,
		description='',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.cmake.cmake','shutit.tk.sd.libevent.libevent','shutit.tk.sd.make_certs.make_certs'],
		conflicts=['shutit.tk.sd.mysql.mysql']
	)


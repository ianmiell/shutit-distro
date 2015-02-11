"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class eatmydata(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')


	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/eatmydata')
		shutit.send('cd /tmp/build/eatmydata')
		shutit.send('wget -qO- https://www.flamingspork.com/projects/libeatmydata/libeatmydata-105.tar.gz | tar -zxf -')
		shutit.send('cd lib*')
		shutit.send('./configure --prefix=/usr')
		shutit.send('make')
		shutit.send('make install')
		return True

	def get_config(self, shutit):
		return True

	#def start(self, shutit):
	#	return True

	#def stop(self, shutit):
	#    return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/eatmydata')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return eatmydata(
		'shutit.tk.sd.eatmydata.eatmydata', 158844782.0313,
		description='eatmydata',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.sd.make_certs.make_certs']
	)


"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class linuxbrew(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('cd /opt')
		shutit.send('git clone https://github.com/Homebrew/linuxbrew.git ~/.linuxbrew')
		shutit.add_to_bashrc('export PATH="$HOME/.linuxbrew/bin:$PATH"',match_regexp='^export PATH=..HOME..linuxbrew.*$')
		shutit.add_to_bashrc('export LD_LIBRARY_PATH="$HOME/.linuxbrew/lib:$LD_LIBRARY_PATH"',match_regexp='^export LD_LIBRARY_PATH=..HOME..linuxbrew.*$')
		return True

	#def get_config(self, shutit):
	#	shutit.get_config(self.module_id,'item','default')
	#	return True

	def finalize(self, shutit):
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

# TODO: depends on ruby
def module():
	return linuxbrew(
		'shutit.tk.sd.linuxbrew.linuxbrew', 158844782.010725,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.git.git','shutit.tk.sd.ruby.ruby']
	)


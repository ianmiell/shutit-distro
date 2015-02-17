"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class libxml2(ShutItModule):

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/libxml2')
		shutit.send('cd /tmp/build/libxml2')
		shutit.send('wget -qO- http://xmlsoft.org/sources/libxml2-2.9.2.tar.gz | tar -zxf -')
		shutit.send('cd libxml2*')
		shutit.send('''sed -e /xmlInitializeCatalog/d -e 's/((ent->checked =.*&&/(((ent->checked == 0) || ((ent->children == NULL) \&\& (ctxt->options \& XML_PARSE_NOENT))) \&\&/' -i parser.c''')
		shutit.send('./configure --prefix=/usr --disable-static --with-history')
		shutit.send('make')
		shutit.send('make install')
		return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/libxml2')
		return True

def module():
	return libxml2(
		'shutit.tk.sd.libxml2.libxml2', 158844782.030445,
		description='libxml2',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.setup']
	)


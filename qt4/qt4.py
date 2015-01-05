"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class qt4(ShutItModule):


	def is_installed(self, shutit):
		return shutit.file_exists('/root/shutit_build/module_record/' + self.module_id + '/built')

	def build(self, shutit):
		shutit.send('mkdir -p /tmp/build/qt4')
		shutit.send('cd /tmp/build/qt4')
		shutit.send('wget -qO- http://download.qt-project.org/official_releases/qt/4.8/4.8.6/qt-everywhere-opensource-src-4.8.6.tar.gz | tar -zxf -')
		shutit.send('cd qt*')
		shutit.send('''sed -i -e '631a if (image->isNull()) { state = Error; return -1; }' src/gui/image/qgifhandler.cpp''')
		shutit.send('export QT4LINK=/usr')
		shutit.send('''sed -i -e "/#if/d" -e "/#error/d" -e "/#endif/d" config.tests/unix/libmng/libmng.cpp''')
		shutit.send('''sed -i '/CONFIG -/ a\isEmpty(OUTPUT_DIR): OUTPUT_DIR = ../..' src/3rdparty/webkit/Source/WebKit2/DerivedSources.pro''')
		shutit.send('./configure -prefix /usr -bindir /usr/bin -plugindir /usr/lib/qt4/plugins -importdir /usr/lib/qt4/imports -headerdir /usr/include/qt4 -datadir /usr/share/qt4 -sysconfdir /etc/xdg -docdir /usr/share/doc/qt4 -demosdir /usr/share/doc/qt4/demos -examplesdir /usr/share/doc/qt4/examples -translationdir /usr/share/qt4/translations -confirm-license -opensource -release -dbus-linked -openssl-linked -system-sqlite -no-phonon -no-phonon-backend -no-nis -no-openvg -nomake demos -nomake examples -optimized-qmake')
		shutit.send('make -j8',timeout=99999)
		shutit.send(r'''find . -name "*.pc" -exec perl -pi -e "s, -L$PWD/?\S+,,g" {} \;''')
		shutit.send('make install')
		shutit.send('rm -rf /usr/tests')
		shutit.login(command='bash -e')
		shutit.run_script(r'''for file in 3Support CLucene Core DBus Declarative DesignerComponents Designer Gui Help Multimedia Network OpenGL Script ScriptTools Sql Svg Test UiTools WebKit XmlPatterns Xml phonon; do
			[ -e /usr/lib/libQt${file}.prl ] &&
			sed -r '/^QMAKE_PRL_BUILD_DIR/d;s/(QMAKE_PRL_LIBS =).*/\1/' \
				-i /usr/lib/libQt${file}.prl
		done
		''')
		shutit.send('unset file')
		shutit.logout()
		shutit.send('install -v -Dm644 src/gui/dialogs/images/qtlogo-64.png /usr/share/pixmaps/qt4logo.png')
		shutit.send('install -v -Dm644 tools/assistant/tools/assistant/images/assistant-128.png /usr/share/pixmaps/assistant-qt4.png')
		shutit.send('install -v -Dm644 tools/designer/src/designer/images/designer.png /usr/share/pixmaps/designer-qt4.png')
		shutit.send('install -v -Dm644 tools/linguist/linguist/images/icons/linguist-128-32.png /usr/share/pixmaps/linguist-qt4.png')
		shutit.send('install -v -Dm644 tools/qdbus/qdbusviewer/images/qdbusviewer-128.png /usr/share/pixmaps/qdbusviewer-qt4.png')
		shutit.send('install -dm755 /usr/share/applications')
		shutit.send_host_file('/usr/share/applications/assistant-qt4.desktop','context/usr/share/applications/assistant-qt4.desktop')
		shutit.send_host_file('/usr/share/applications/designer-qt4.desktop','context/usr/share/applications/designer-qt4.desktop')
		shutit.send_host_file('/usr/share/applications/linguist-qt4.desktop','context/usr/share/applications/linguist-qt4.desktop')
		shutit.send_host_file('/usr/share/applications/qdbusviewer-qt4.desktop','context/usr/share/applications/qdbusviewer-qt4.desktop')
		shutit.send_host_file('/usr/share/applications/qtconfig-qt4.desktop','context/usr/share/applications/qtconfig-qt4.desktop')
		return True

	def get_config(self, shutit):
		return True

	def finalize(self, shutit):
		shutit.send('rm -rf /tmp/build/qt4')
		return True

	#def remove(self, shutit):
	#	return True

	#def test(self, shutit):
	#	return True

def module():
	return qt4(
		'shutit.tk.sd.qt4.qt4', 158844782.0263,
		description='',
		maintainer='',
		depends=['shutit.tk.sd.alsa_lib.alsa_lib','shutit.tk.sd.mesalib.mesalib','shutit.tk.sd.make_certs.make_certs','shutit.tk.sd.glib.glib','shutit.tk.sd.icu.icu','shutit.tk.sd.libjpeg.libjpeg','shutit.tk.sd.libpng.libpng','shutit.tk.sd.libtiff.libtiff','shutit.tk.sd.sqlite.sqlite','shutit.tk.sd.libmng.libmng','shutit.tk.sd.libdbus.libdbus'],
		conflicts=['shutit.tk.sd.qt5.qt5']
	)


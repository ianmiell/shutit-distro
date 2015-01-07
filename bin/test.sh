#!/bin/bash
if [[ $1 = '' ]]
then
	start="setup"
	started="1"
else
	start="$1"
	started="0"
fi
pushd ..
find . | grep .cnf$ | xargs chmod 0600
popd

export SHUTIT_OPTIONS="$SHUTIT_OPTIONS --image_tag imiell/sd_base"
for d in make_certs lzo curl sharutils libgpg_error libgcrypt cpio which libffi libidn util_macros tcl check ruby procps_ng sqlite pcre python2 libgoogle_glog onigurama rsync icu sgml_common llvm apache_portable_runtime apache_portable_runtime_util libxslt xmlto less giflib asciidoc libarchive cmake alsa_lib python_pip scons serf apache go subversion nettle libtasn1 tls zip x7proto xcb_proto libxau libpng libxcb glib gobject freetype2_pre_harfbuzz harfbuzz freetype2 desktop_file_utils fontconfig opensp docbook_dsssl docbook_sgml_dtd openjade docbook_utils xorg_libs git atk linuxbrew jq tk cups nasm libjpeg libtiff pixman cairo pango gdk_pixbuf gtk2 lcms libmng libdbus java_binary ant junit nspr nss attr kona haproxy node boost libtirpc lsof sthttpd screen time tree openjdk expect berkeleydb linux_pam cyrus_sasl xinetd open_ldap mit_kerberos_v5 postgresql libdrm elfutils mesalib xbitmaps xcb_util xorg_apps xterm spector qt4 gflags rocksdb libevent libsnappy libpopt rpm fastcomp emscripten doxygen dpkg thrift mariadb emacs osquery erlang
do
	if [[ $started = "0" ]]
	then
		if [[ $start = $d ]]
		then
			started="1"
		else
			continue
		fi
	fi
	pushd ../$d/bin
	if [[ -a ../STOPTEST ]]
	then
		echo "STOPTEST found in $d"
		continue
	fi
	echo "BEGIN $d $(date)"
	./build_and_push.sh
	if [[ $? != 0 ]]
	then
		echo "FAILED $d"
		exit 1
	fi
	echo "DONE $d $(date)"
	popd
done


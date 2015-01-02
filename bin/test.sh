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

for d in make_certs zip check curl apache_portable_runtime cpio which tcl sqlite icu libffi libgpg_error libidn lzo nasm nspr onigurama pixman rsync sgml_common sharutils go expect xmlto util_macros less python2 llvm libpng fontconfig freetype2_pre_harfbuzz libjpeg x7proto xcb_proto libxau libxcb pcre glib desktop_file_utils python_pip xorg_libs libxslt procps_ng libarchive cmake attr apache_portable_runtime_util gobject scons asciidoc harfbuzz alsa_lib git freetype2 cairo docbook_dsssl docbook_utils atk opensp openjade giflib nss erlang nettle docbook_sgml_dtd jq kona lcms libgcrypt libtiff pango serf sthttpd subversion gtk2 gdk_pixbuf berkeleydb libtasn1 ant junit tls ruby linuxbrew apache tk cups cyrus_sasl java_binary haproxy node openjdk boost libtirpc lsof screen time tree linux_pam
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


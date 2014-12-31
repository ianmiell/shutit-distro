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

#cat test.sh | grep git | tr ' ' '\n' | sort | grep -vw for | grep -vw d | grep -vw in > ../sortedtest
#ls -1 | grep -vw bin | grep -vw [A-Z] | sort > sorteddirs
#meld sorteddirs sortedtest

for d in pkg_config apache_portable_runtime cpio which tcl sqlite icu libffi libgpg_error libidn lzo nasm nspr onigurama pixman rsync sgml_common sharutils go expect xmlto util_macros less python2 llvm libpng fontconfig freetype2_pre_harfbuzz libjpeg x7proto xcb_proto libxau libxcb glib
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
	echo "BEGIN $d $(date)" >> /tmp/shutitdistout
	./build_and_push.sh >> /tmp/shutitdistout
	if [[ $? != 0 ]]
	then
		echo "FAILED $d" >> /tmp/shutitdistout
		exit 1
	fi
	echo "DONE $d $(date)" >> /tmp/shutitdistout
	popd
done


#!/bin/bash
pushd ..
../../shutit/shutit build --shutit_module_path .. "$@"
if [[ $? != 0 ]]
then
	popd
	exit 1
fi
popd

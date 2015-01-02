#!/bin/bash
set -e
cd ../base
cat ../base_files/x* > lfs.tar.xz
docker build --no-cache -t imiell/sd_base .
docker push imiell/sd_base

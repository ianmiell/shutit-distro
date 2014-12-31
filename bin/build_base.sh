#!/bin/bash
set -e
cd ../base
docker build --no-cache -t imiell/sd_base .
docker push imiell/sd_base

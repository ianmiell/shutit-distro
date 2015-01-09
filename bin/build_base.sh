#!/bin/bash
set -e
docker build --no-cache -t imiell/sd_base .
docker push imiell/sd_base

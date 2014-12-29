shutit-distro
=============

ShutIt Distribution based on Linux From Scratch

1) An automated Linux From Scratch tar file is built using this shutit module:

https://github.com/ianmiell/shutit/blob/master/library/alfs/alfs.py

viz: /artifacts/lfs.tar.xz

2) This tar file is then used as the basis for this Dockerfile:

https://github.com/ianmiell/shutit-distro/blob/master/base/Dockerfile

which is then tagged and pushed as imiell/sd_base

3) This base image is used as a base for the ShutIt modules in this repo.

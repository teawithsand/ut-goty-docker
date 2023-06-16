#!/bin/bash

# NOTE: below does not work
# since installer requires some tricky hacking with mountpoints
# ###################################################
# ###################################################
# using xorriso(sudo apt install xorriso) like
# osirrox -indev UT_GOTY_CD1.iso -extract / ./img1
# osirrox -indev UT_GOTY_CD2.iso -extract / ./img2
# is also fair game
echo "Mounting $1 at $2"

mkdir -p "$2" && \
sudo mount -o loop --read-only "$1" "$2"

# to unmount just do umount
# sudo umount "$MP1"
# sudo umount "$MP2"
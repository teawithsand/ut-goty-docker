#!/bin/bash

export DEBIAN_FRONTEND=noninteractive

dpkg --add-architecture i386
apt update
apt install python3 sudo libx11-6:i386 libxext6:i386 libc6:i386 -y

./mount-img.sh /images/UT_GOTY_CD1.iso /media/cdrom0
./mount-img.sh /images/UT_GOTY_CD2.iso /media/cdrom1

./ut-install-436-goty.run --keep
./path-installer.py
cd ./ut-436-GOTY && ./setup.sh
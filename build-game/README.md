## Building

In order to build Unreal Tournament GOTY:
- Download loki installer and call it `ut-install-436-goty.run`. This can be done using `curl -O https://princessleia.com/tools/ut/ut-install-436-goty.run`
- Download two CD images/get iso files in any other way and store them in `./images`. The first one must be called `UT_GOTY_CD1.iso` and second one must be called `UT_GOTY_CD2.iso`. These can be downloaded from https://archive.org/details/ut-goty
- Run `./run-installer.sh` script making sure you do not call it from any other directory than `.` In other words, make sure you've cd-ed into this build-image directory before you did anything.
- Answer yes/no to all questions, but leave installation directory set to `/usr/local/games/ut`
- After installation finishes, working game files are stored in `./ut-data` These can be used in next step - building docker image. Please note that root is the owner of all data in this dir, so appropriate chown/chmod is required.
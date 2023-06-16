#!/bin/bash

# img1 and img2 can be replaced with paths to mounted iso images obviously or real cdrom
# note that --privileged is required
# since installer does some weird mountpoint listing
# and it can't be easily patched afaik

mkdir ut-data
mkdir images

docker run -it \
    --privileged \
    -v ./scripts:/base-data:ro \
    -v ./ut-data:/usr/local/games/ut:rw \
    -v ./images:/images:ro,shared \
    ubuntu:latest /bin/bash -c "cp -r /base-data /tmp/op-data && cd /tmp/op-data && ./install.sh"
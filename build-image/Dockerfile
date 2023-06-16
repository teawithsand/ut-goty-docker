FROM ubuntu:latest

RUN dpkg --add-architecture i386
RUN apt update && apt install libx11-6:i386 libxext6:i386 libc6:i386 xauth apulse osspd python3 -y -qq

ARG user=utuser
ARG group=utuser
ARG uid=1000
ARG gid=1000
RUN groupadd -g ${gid} ${group}
RUN useradd -u ${uid} -g ${group} -s /bin/sh -m utuser
USER ${uid}:${gid}

COPY ./ut-data /app
COPY /init.py /init.py
CMD /init.py && /app/ut
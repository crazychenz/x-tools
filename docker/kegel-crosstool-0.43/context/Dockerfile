FROM lpenz/ubuntu-dapper-amd64

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    gcc-3.3 g++-3.3 libc6-dev make dpkg-dev \
    libncurses5-dev bison flex python \
    lynx wget sed patch vim binutils texinfo rsync

RUN ln -s /usr/bin/gcc-3.3 /usr/bin/gcc
RUN ln -s /usr/bin/g++-3.3 /usr/bin/g++

# Allow sudoers to sudo without passwords.
# Note: Recommended to use `sudo -E` in dockerfiles.
RUN apt-get install -y sudo
RUN sed -i 's/ALL=(ALL:ALL) ALL/ALL=(ALL:ALL) NOPASSWD: ALL/' /etc/sudoers

# User defaults, ideally setup to match existing user's info with `whoami` and `id`.
ARG uid=1000
ARG gid=1000
ARG username=user
ARG groupname=user
ARG groups=user

# Create and change ownership of /opt to user.
WORKDIR /opt
RUN chown -R ${uid}:${gid} /opt

RUN addgroup --gid ${gid} ${groupname}
RUN adduser --home /opt --system --disabled-password --uid ${uid} --gid ${gid} ${username}
RUN adduser ${username} sudo

ADD --chown=${uid}:${gid} crosstool-0.43.tar.gz /opt/
RUN chown -R ${uid}:${gid} /opt/crosstool-0.43

USER ${uid}:${gid}

RUN mkdir build && ln -s /opt/build /opt/crosstool-0.43/build
RUN mkdir x-tools && ln -s /opt/x-tools /opt/crosstool

#ENTRYPOINT /opt/build.sh

# docker run -ti --rm \
#   -v $(pwd)/downloads:/opt/downloads \
#   -v $(pwd)/build:/opt/build \
#   -v $(pwd)/x-tools:/opt/x-tools \
#   crazychenz/lpenz-ubuntu-dapper-6.06 

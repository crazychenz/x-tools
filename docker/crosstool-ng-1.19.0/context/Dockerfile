FROM lpenz/ubuntu-hardy-amd64

# Most things (e.g. bash) are better than /bin/sh.
# Note: This tricks `docker build` into using bash instead of
#       the dorked /bin/sh that is part of ubuntu base image.
# Note: This should be done first so all subsequent environment
#       settings are part of this new shell environment.
#RUN rm /bin/sh && ln -s /bin/bash /bin/sh

ARG DEBIAN_FRONTEND=noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN=true
RUN { echo 'tzdata tzdata/Areas select Etc'; echo 'tzdata tzdata/Zones/Etc select UTC'; } | debconf-set-selections

# Provide shell a namespace it's running in.
#ARG image_name
#ENV DOCKER_IMAGE_NAME=${image_name}

# Prompts without color should be the edge case.
#ENV TERM=screen-256color

# Break that absurd bell!
RUN echo "set bell-style none" >> /etc/inputrc

# Update repository list and install baseline dependencies.
RUN apt-get update && apt-get install -y \
    net-tools iputils-ping \
    curl wget \
    python \
    vim vim-common \
    rsync \    
    openssh-client telnet \
    && apt-get -y autoclean

# Allow sudoers to sudo without passwords.
# Note: Recommended to use `sudo -E` in dockerfiles.
RUN apt-get install -y sudo
RUN sed -i 's/ALL=(ALL:ALL) ALL/ALL=(ALL:ALL) NOPASSWD: ALL/' /etc/sudoers

# Crosstool-NG 1.24.0 Dependencies
RUN apt-get update && apt-get install -y \
    gcc g++ gperf bison flex texinfo help2man make libncurses5-dev \
    autoconf automake libtool subversion gawk wget bzip2 \
    unzip patch libstdc++6 rsync gettext bc libexpat1-dev

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

# Create and change ownership of /opt to user.
WORKDIR /opt
RUN chown -R ${uid}:${gid} /opt

ADD --chown=${uid}:${gid} crosstool-ng-1.19.0.tar.bz2 /opt/
RUN chown -R ${uid}:${gid} /opt/crosstool-ng-1.19.0

USER ${uid}:${gid}

WORKDIR /opt/crosstool-ng-1.19.0
RUN /opt/crosstool-ng-1.19.0/configure --prefix=/usr
USER root
RUN make install
USER ${uid}:${gid}
#RUN /opt/crosstool-ng-1.19.0/configure --enable-local && make

WORKDIR /opt


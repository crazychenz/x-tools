# X-Tools

## Overview

When building various toolchains using crosstools-ng and crosstool, there are a number of expected environmental conditions that need to be met for clean execution of the build system. To facilitate this, I've partially containerized the builds so that I can quickly, cleanly, and painlessly locate, configure, and build a particular toolchain for a particular need.

Personally, I always build my toolchains to be static (when possible). This prevents any coupling between the container and the toolchain itself, allowing me to archive and transfer the toolchain to an appropriate environment.

## Layout

This X-Tools suite is composed a directory structure convention:
- **builds** - The root for all of the toolchain build working directories.
- **\*-scripts** - The primary script folders for interacting with this suite.
- **docker** - The docker image builds.
- **downloads** - The primary cache of archives used to build the toolchains.
- **x-tools** - The primary output of the toolchain builds.

### Downloads

While the containerization of the builds has stabalized the runtime of the toolchain compilation, there are a number of archive URLs that are no longer valid in the various build systems. I believe that supporting automatic retrieval of archives across unwitting repositories is an anti-pattern and fragile. Instead, I've personally started collecting all of the downloads (manually or automatically) in the `downloads` folder. For repeatability, I've also started tracking files I've downloaded and used in a sha1sum index.

Sometimes the build fails to find or retrieve an archive. If for example its a version of the `mpfr` library, I'd suggest googling "Index of mpfr". This query will usually net you the mother load of whatever open source libraries you are looking for. Otherwise, throwing in the library and version into the google search never hurts. I just find that you'll get more documentation and forum noise going that route.

### Builds

This is the folder where the builds are performed. The folder that your build uses is dependent on the _alias_ you choose when staging a build.

Note: Build folders can get quite large (3GB - 15GB). I recommend cleaning this folder out frequently. Remember, the point of containerizing the builds is for repeatability. There is no reason to hold onto the build artifacts once a build has completed successfully.

### Docker

Each environment has its own docker build folder. Within each of these are a `build.sh` script, which can typically be executed without any parameters. The `context` folder contains the Dockerfile and any other artifacts that are required to build the Docker image (e.g. the build system orchestrators themselves.)

Note: When building a docker image for x-tools, the image will create itself as the user running the `build.sh` script. This means that its expected that each user with a unique uid and gid will have to create their own set of docker images.

### X-Tools

This is the primary output for the toolchains being built. If you've opted to build a toolchain that isn't static, you may be forced to always use the toolchain with a compatible libc environment, like the base image distribution of the docker environment used to build the toolchain. By opting to always build a static toolchain (when possible), you avoid this and make the toolchains significantly more portable (within their respective architectures).

## Selecting An Environment

When you decide that a new toolchain is the correct decision, you'll need to identify which environment is best suited to your needs.

### ct-ng-1.24.0

- Core
  - Linux: 4.20.8 thru 3.2.101
  - Binutils: 2.32 thru 2.26.1
  - Glibc: 2.28 thru 2.12.1
  - Gcc: 8.3.0 thru 4.9.4
- Debug
  - duma: 2_5_15
  - gdb: 8.2.1 thru 7.11.1 (cross & native)
  - ltrace: 0.7.3
  - strace: 4.26 thru 4.15
- Libs
  - cloog: 0.18.4
  - expat: 2.2.6
  - gettext: 0.19.8.1
  - gmp: 6.1.2
  - isl: 0.20 thru 0.15
  - libelf: 0.8.13
  - libiconv: 1.5
  - mpc: 1.1.0 thru 1.0.3
  - mpfr: 4.0.2 thru 3.1.6
  - ncurses: 6.1 thru 6.0
  - zlib: 1.2.11
- Tools
  - autoconf: 2.69 thru 2.65
  - automake: 1.16.1 thru 1.15.1
  - bison: 3.3.2 thru 3.0.5
  - dtc: 1.4.7
  - libtool: 2.4.6
  - m4: 1.4.18
  - make: 4.2.1

## ct-ng-1.19.0

- Core
  - Linux: 3.10.2 thru 2.6.27.62
  - Binutils: 2.22 thru 2.18a
  - Gcc: 4.8.1 thru 4.2.2
  - Libc
    - Glibc: 2.17 thru 2.8
    - Eglibc: 2_17 thru 2_9 (or trunk)
    - Uclibc: 0.9.33.2 thru 0.9.30
- Debug
  - dmalloc: 5.5.2
  - duma: 2.5.15
  - gdb: 7.4.1 thru 6.8a (native & cross)
  - ltrace: 0.5.3 thru 0.5.2
  - strace: 4.5.20 thru 4.5.18
- Libs
  - gmp: 5.1.1 thru 4.3.0
  - mpfr: 3.1.2 thru 2.4.0
  - ppl: 0.11.2 thru 0.10.2
  - cloog: 0.15.11 thru 0.15.6
  - libelf: 0.8.13 thru 0.8.12

# kegel-ct-0.43

- Core
  - Linux: 2.6.15.4 thru 2.6.8 / 2.4.26 / historically 2.2.X
  - Binutils: 2.15 thru 2.16
  - Gcc: 2.95.3 thru 4.1.1
  - Glibc: 2.1.3 thru 2.3.6 (linuxthreads: 2.1.3 thru 2.3.6)
- Misc
  - gcrypt: 2.1
  - gdb: 6.5

## Usage

Once you've identified the correct environment for your needs, enter the appropriate `*-scripts` folder. In the folder there are several operations:

- list.sh - Lists the possible starting points for builds.
- stage.sh - Initialize a folder from a starting point with a given name (or alias).
- config.sh - Allows you to make adjustments to the configuration before building.
- build.sh - Builds the toolchain.

### ct-ng Example

```sh
$ cd ct-ng-1.24.0-scripts

$ ./list | grep mips
# Lists starter tuples for mips (e.g. mips-malta-linux-gnu)

$ ./stage.sh mips-malta-linux-gnu my-build-alias
# configuration written to .config

$ ./config.sh my-build-alias
# Perform configuration

$ ./build.sh my-build-alias
# Builds toolchain.

$ ../x-tools/binutils-2.32-gcc-4.9.4-linux-3.2.101-glibc-2.28/mips-static-linux-gnu/bin/mips-static-linux-gnu-gcc --version
mips-static-linux-gnu-gcc (crosstool-NG 1.24.0) 4.9.4
Copyright (C) 2015 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```

### Kegel Crosstool Example

```sh
$ cd kegel-ct-0.43-scripts

$ ./list.sh | grep mips
# Lists starter tuples for mips (e.g. mips_gcc-3.4.5-glibc-2.3.6_crosstool.sh)

$ ./stage.sh mips_gcc-3.4.5-glibc-2.3.6_crosstool.sh my-build-alias
# configuration written to .config

$ ./config.sh my-build-alias
# Perform configuration

$ ./build.sh my-build-alias
# Builds toolchain.

$ ../x-tools/binutils-2.15-gcc-3.4.5-linux-2.6.8-glibc-2.3.6/mips-static-linux-gnu/bin/mips-static-linux-gnu-gcc --version

```
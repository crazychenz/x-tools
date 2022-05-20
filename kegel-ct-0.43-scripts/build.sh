#!/bin/sh

: ${WD_PREFIX:=$(pwd)/../}
STAGER_TARGET_ALIAS=$1

# Import the configuration settings into our environment.
grep ^export ${WD_PREFIX}builds/$STAGER_TARGET_ALIAS/staged-config.sh > ${WD_PREFIX}builds/$STAGER_TARGET_ALIAS/env.sh
. ${WD_PREFIX}builds/$STAGER_TARGET_ALIAS/env.sh

# Construct the expected crosstool builds folder
mkdir -p ${WD_PREFIX}builds/$STAGER_TARGET_ALIAS/${GCC_DIR}-${GLIBC_DIR}

# Construct our conventional output folder
mkdir -p ${WD_PREFIX}x-tools/${BINUTILS_DIR}-${GCC_DIR}-${LINUX_DIR}-${GLIBC_DIR}

# Trick crosstool into building into our output folder
ln -s ${BINUTILS_DIR}-${GCC_DIR}-${LINUX_DIR}-${GLIBC_DIR} ${WD_PREFIX}x-tools/${GCC_DIR}-${GLIBC_DIR} 

# Do the build
docker run -ti --rm \
    -v ${WD_PREFIX}downloads:/opt/downloads \
    -v ${WD_PREFIX}x-tools:/opt/x-tools \
    -v ${WD_PREFIX}builds/$STAGER_TARGET_ALIAS:/opt/crosstool-0.43/build/$TARGET \
    -v ${WD_PREFIX}builds/$STAGER_TARGET_ALIAS:/opt/build \
    -w /opt/build \
    crazychenz/kegel-crosstool-0.43 ./staged-config.sh

# Remove symlink
rm -f ${WD_PREFIX}x-tools/${GCC_DIR}-${GLIBC_DIR} 
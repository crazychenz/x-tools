#!/bin/sh

# List pre-configured toolchains:
#
#   ./run-ct-ng-1.24.0.sh ct-ng list-samples
#
# Stage a configuration:
#
#   export STAGE_CFG_DIR=builds/stage ; mkdir -p ${STAGE_CFG_DIR} && ./run-ct-ng-1.24.0.sh ct-ng -C /opt/${STAGE_CFG_DIR} mipsel-unknown-linux-gnu && ./run-ct-ng-1.24.0.sh ct-ng -C /opt/${STAGE_CFG_DIR} menuconfig
#
# Position stage:
#
#   CT_Mirrors () { echo; } ; source builds/stage/.config ; mv builds/stage builds/binutils-${CT_BINUTILS_VERSION}-gcc-${CT_GCC_VERSION}-linux-${CT_LINUX_VERSION}-glibc-${CT_GLIBC_VERSION}
#
# Build configuration:
#
#   ./run-ct-ng-1.24.0.sh ct-ng -C /opt/builds/binutils-${CT_BINUTILS_VERSION}-gcc-${CT_GCC_VERSION}-linux-${CT_LINUX_VERSION}-glibc-${CT_GLIBC_VERSION}/mipsel-unknown-linux-gnu CT_PREFIX=/opt/x-tools/binutils-${CT_BINUTILS_VERSION}-gcc-${CT_GCC_VERSION}-linux-${CT_LINUX_VERSION}-glibc-${CT_GLIBC_VERSION} build
#

# _IDEALLY_ SHOULD BE
# List pre-configured toolchains:
#
#   ./list-ct-ng-1.24.0.sh ct-ng list-samples
#
# Create a configuration:
#
#   ./config-ct-ng-1.24.0.sh <sample-target>
#
# Build configuration:
#
#   ./build-ct-ng-1.24.0.sh <config> <target>
#

: ${WD_PREFIX:=$(pwd)/../}

docker run -ti --rm \
    -v ${WD_PREFIX}downloads:/opt/src \
    -v ${WD_PREFIX}x-tools:/opt/x-tools \
    -v ${WD_PREFIX}scripts:/opt/scripts \
    -v ${WD_PREFIX}builds:/opt/builds \
    crazychenz/crosstool-ng-1.24.0 $@

# Example:
#
#   ./run-ct-ng-1.24.0.sh -C /opt/builds/mipsel-unknown-linux-gnu mipsel-unknown-linux-gnu
#   ./run-ct-ng-1.24.0.sh -C /opt/builds/mipsel-unknown-linux-gnu build
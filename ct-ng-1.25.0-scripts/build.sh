#!/bin/sh

: ${WD_PREFIX:=$(pwd)/../}
STAGER_TARGET_ALIAS=$1

CT_Mirrors () { echo; }
. ${WD_PREFIX}builds/${STAGER_TARGET_ALIAS}/.config && ./_run.sh ct-ng -C /opt/builds/${STAGER_TARGET_ALIAS} CT_PREFIX=/opt/x-tools/binutils-${CT_BINUTILS_VERSION}-gcc-${CT_GCC_VERSION}-linux-${CT_LINUX_VERSION}-glibc-${CT_GLIBC_VERSION} build


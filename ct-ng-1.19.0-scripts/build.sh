#!/bin/sh

: ${WD_PREFIX:=$(pwd)/../}
STAGER_TARGET_ALIAS=$1

CT_Mirrors () { echo; }

sed -i '/^CT_PREFIX_DIR/c CT_PREFIX_DIR="${CT_PREFIX}${CT_TARGET}"' ${WD_PREFIX}builds/${STAGER_TARGET_ALIAS}/.config && \
  . ${WD_PREFIX}builds/${STAGER_TARGET_ALIAS}/.config && \
  ./_run.sh ct-ng -C /opt/builds/${STAGER_TARGET_ALIAS} \
    CT_PREFIX=/opt/x-tools/binutils-${CT_BINUTILS_VERSION}-gcc-${CT_CC_VERSION}-linux-${CT_KERNEL_VERSION}-glibc-${CT_LIBC_VERSION}/ \
    build


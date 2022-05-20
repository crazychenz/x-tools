#!/bin/sh -x

: ${WD_PREFIX:=$(pwd)/../}
STAGER_STARTER_TARGET=$1
STAGER_TARGET_ALIAS=$2

mkdir -p ${WD_PREFIX}builds/$STAGER_TARGET_ALIAS
./_run.sh ct-ng -C /opt/builds/${STAGER_TARGET_ALIAS} ${STAGER_STARTER_TARGET}



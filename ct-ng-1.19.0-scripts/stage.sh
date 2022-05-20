#!/bin/sh

if [ $# -lt 2 -o $# -gt 2 ]; then echo "Usage: $0 <starter> <alias>\n"; exit 1; fi

: ${WD_PREFIX:=$(pwd)/../}
STAGER_STARTER_TARGET=$1
STAGER_TARGET_ALIAS=$2

mkdir -p ${WD_PREFIX}builds/$STAGER_TARGET_ALIAS
./_run.sh ct-ng -C /opt/builds/${STAGER_TARGET_ALIAS} ${STAGER_STARTER_TARGET}



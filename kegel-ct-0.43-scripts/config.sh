#!/bin/sh

: ${WD_PREFIX:=$(pwd)/../}
STAGER_TARGET_ALIAS=$1

${EDITOR:=vim} ${WD_PREFIX}builds/$STAGER_TARGET_ALIAS/staged-config.sh

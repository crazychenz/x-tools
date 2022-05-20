#!/bin/sh

STAGER_TARGET_ALIAS=$1

./_run.sh ct-ng -C /opt/builds/${STAGER_TARGET_ALIAS} menuconfig



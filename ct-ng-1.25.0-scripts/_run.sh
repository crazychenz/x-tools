#!/bin/sh

: ${WD_PREFIX:=$(pwd)/../}

docker run -ti --rm \
    -v ${WD_PREFIX}downloads:/opt/src \
    -v ${WD_PREFIX}x-tools:/opt/x-tools \
    -v ${WD_PREFIX}scripts:/opt/scripts \
    -v ${WD_PREFIX}builds:/opt/builds \
    crazychenz/crosstool-ng-1.25.0 $@


#!/bin/sh

# 

docker run -ti --rm \
    -v $(pwd)/opt/downloads:/opt/src \
    -v $(pwd)/opt/x-tools:/opt/x-tools \
    -v $(pwd)/opt/scripts:/opt/scripts \
    crazychenz/crosstool-ng-1.19.0
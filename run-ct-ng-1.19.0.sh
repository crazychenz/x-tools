#!/bin/sh

# Example:
#
#  
#  time ./run-ct-ng-1.24.0.sh ct-ng -C /opt/builds/binutils-2.32-gcc-4.9.4-linux-4.20.8-glibc-2.28/mipsel-static-linux-gnu CT_PREFIX=/opt/x-tools/binutils-2.32-gcc-4.9.4-linux-4.20.8-glibc-2.28 build 

docker run -ti --rm \
    -v $(pwd)/downloads:/opt/src \
    -v $(pwd)/x-tools:/opt/x-tools \
    -v $(pwd)/scripts:/opt/scripts \
    -v $(pwd)/builds:/opt/builds \
    crazychenz/crosstool-ng-1.19.0 $@

# Example:
#
#   ./run-ct-ng-1.24.0.sh -C /opt/builds/mipsel-unknown-linux-gnu mipsel-unknown-linux-gnu
#   ./run-ct-ng-1.24.0.sh -C /opt/builds/mipsel-unknown-linux-gnu build
#!/bin/sh

# Example:
#
#   ./run-ct-0.43.sh ls
#   ./run-ct-0.43.sh mipsel_gcc-3.4.5-glibc-2.3.6_crosstool.sh

docker run -ti --rm \
    -v $(pwd)/downloads:/opt/downloads \
    -v $(pwd)/x-tools:/opt/x-tools \
    -v $(pwd)/scripts:/opt/scripts \
    -v $(pwd)/builds/crosstool-0.43:/opt/crosstool-0.43/build \
    -w /opt/scripts \
    crazychenz/kegel-crosstool-0.43 $@


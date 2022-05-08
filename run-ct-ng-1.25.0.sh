#!/bin/sh

docker run -ti --rm \
    -v $(pwd)/downloads:/opt/src \
    -v $(pwd)/x-tools:/opt/x-tools \
    -v $(pwd)/scripts:/opt/scripts \
    -v $(pwd)/builds:/opt/builds \
    crazychenz/crosstool-ng-1.25.0 $@

# Example:
#
#   ./run-ct-ng-1.24.0.sh -C /opt/builds/mipsel-unknown-linux-gnu mipsel-unknown-linux-gnu
#   ./run-ct-ng-1.24.0.sh -C /opt/builds/mipsel-unknown-linux-gnu build
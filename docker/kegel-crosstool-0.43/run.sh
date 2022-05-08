#!/bin/sh
docker run -ti --rm \
    -v $(pwd)/opt/downloads:/opt/downloads \
    -v $(pwd)/opt/x-tools:/opt/x-tools \
    -v $(pwd)/opt/scripts:/opt/scripts \
    crazychenz/kegel-crosstool-0.43 /bin/bash
#!/bin/sh

STAGER_TARGET_ALIAS=$1

./_run.sh ct-ng -C /opt/builds/${STAGER_TARGET_ALIAS} menuconfig


# # Name parameter
# PRECONFIGURED_STARTER_TARGET=$1

# # Setup new configuration
# export TEMP_CONFIG_PATH=$(mktemp)
#   ./_run-ct-ng-1.24.0.sh ct-ng ${PRECONFIGURED_STARTER_TARGET} KCONFIG_CONFIG=${TEMP_CONFIG_PATH} && \
#   ._/run-ct-ng-1.24.0.sh ct-ng -C /opt/${STAGE_CFG_DIR} menuconfig 

# # Generate the toolchain name and move to appropriate folder.
# CT_Mirrors () { echo; }
# source builds/stage/.config
# mv builds/stage builds/binutils-${CT_BINUTILS_VERSION}-gcc-${CT_GCC_VERSION}-linux-${CT_LINUX_VERSION}-glibc-${CT_GLIBC_VERSION}

# echo ./build-ct-ng-1.24.0.sh binutils-${CT_BINUTILS_VERSION}-gcc-${CT_GCC_VERSION}-linux-${CT_LINUX_VERSION}-glibc-${CT_GLIBC_VERSION}
# KCONFIG_CONFIG
# # TODO: Output the toolchain path and tuple for input into build command.

# # Example:
# #
# #   ./run-ct-ng-1.24.0.sh -C /opt/builds/mipsel-unknown-linux-gnu mipsel-unknown-linux-gnu
# #   ./run-ct-ng-1.24.0.sh -C /opt/builds/mipsel-unknown-linux-gnu build


# # CT_TARGET_VENDOR="static_multilib"
# # CT_KERNEL="linux"
# # CT_ARCH="x86"
# # CT_ARCH_64=y

# # TODO: How to determine "gnu/musl/uclibc"?
# #CT_GLIBC_USE_GNU=y


# ./list.sh
# ./stage.sh <target> <alias>
# ./stage.sh x86_64-multilib-linux-gnu x86_64-multilib-linux-gnu
# ./config.sh <alias>
# ./config.sh x86_64-multilib-linux-gnu
# ./build <alias>

# #x86_64-multilib-linux-gnu
# STAGER_STARTER_TARGET=$1
# STAGER_TARGET_ALIAS=$2

# mkdir -p builds/$STAGER_TARGET_ALIAS
# ./_run-ct-ng-1.24.0.sh ct-ng -C /opt/builds/${STAGER_TARGET_ALIAS} ${STAGER_STARTER_TARGET}
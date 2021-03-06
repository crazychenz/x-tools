#!/usr/bin/env python3

import os
import stat

def main():
    for arch in cross_tool_dats:
      for toolset in cross_tool_dats[arch]:
        with open('../crosstool-0.43/%s.dat' % arch, 'r') as arch_fobj:
          arch_dat = arch_fobj.read()
          lines = []
          for line in arch_dat.splitlines():
            lines.append('export %s' % line)
          arch_dat = '\n'.join(lines)
        with open('../crosstool-0.43/%s.dat' % toolset, 'r') as toolset_fobj:
          toolset_dat = toolset_fobj.read()
          lines = []
          for line in toolset_dat.splitlines():
            lines.append('export %s' % line)
          toolset_dat = '\n'.join(lines)

        script_fname = '%s_%s_crosstool.sh' % (arch.replace('_', '-'), toolset)
        with open(script_fname, 'w') as script_fobj:
          script_fobj.write('\n'.join([
            '#!/bin/bash',
            '# %s_%s_crosstool.sh' % (arch.replace('_', '-'), toolset),
            'set -ex',
            'export CROSSTOOL_PREFIX=/opt/crosstool-0.43/',
            arch_dat,
            toolset_dat,
            script_config,
            'pushd ../crosstool-0.43 ; ./all.sh --notest ; popd',
          ]))
        os.chmod(script_fname, stat.S_IXOTH | stat.S_IROTH | stat.S_IRWXG | stat.S_IRWXU)
        


script_config = '''
export TARBALLS_DIR=/opt/downloads
export RESULT_TOP=/opt/x-tools
export GCC_LANGUAGES="c,c++"
mkdir -p $RESULT_TOP
'''


#gcc-3.4.2-glibc-20040827',
#gcc-3.4.2-glibc-20040827',
#gcc-3.4.2-glibc-20040827',
cross_tool_dats = {
  'alpha': [
    'gcc-2.95.3-glibc-2.2.5',
    'gcc-3.2.3-glibc-2.2.5',
    'gcc-3.2.3-glibc-2.3.2',
    'gcc-3.3.6-glibc-2.2.5',
    'gcc-3.3.6-glibc-2.3.2',
    'gcc-3.3.6-glibc-2.3.2-tls',
    'gcc-3.3.6-glibc-2.3.5-tls',
    'gcc-3.3.6-glibc-2.3.6-tls',
    'gcc-3.4.5-glibc-2.2.5',
    'gcc-3.4.5-glibc-2.3.2',
    'gcc-3.4.5-glibc-2.3.2-tls',
    'gcc-3.4.5-glibc-2.3.5',
    'gcc-3.4.5-glibc-2.3.5-tls',
    'gcc-3.4.5-glibc-2.3.6',
    'gcc-3.4.5-glibc-2.3.6-tls',
    'gcc-4.0.2-glibc-2.3.2',
    'gcc-4.0.2-glibc-2.3.5',
    'gcc-4.0.2-glibc-2.3.6',
    'gcc-4.1.0-glibc-2.3.2',
    'gcc-4.1.0-glibc-2.3.5',
    'gcc-4.1.0-glibc-2.3.5-tls',
    'gcc-4.1.0-glibc-2.3.6',
    'gcc-4.1.0-glibc-2.3.6-tls',
  ],
  'arm9tdmi': [
    'gcc-3.2.3-glibc-2.2.5',
    'gcc-3.2.3-glibc-2.3.2',
    'gcc-3.2.3-glibc-2.3.2-tls',
    'gcc-3.3.6-glibc-2.2.5',
    'gcc-3.3.6-glibc-2.3.2',
    'gcc-3.3.6-glibc-2.3.2-tls',
    'gcc-3.4.5-glibc-2.2.5',
    'gcc-3.4.5-glibc-2.3.2',
    'gcc-3.4.5-glibc-2.3.2-tls',
    'gcc-3.4.5-glibc-2.3.5',
    'gcc-3.4.5-glibc-2.3.5-tls',
    'gcc-3.4.5-glibc-2.3.6',
    'gcc-3.4.5-glibc-2.3.6-tls',
    'gcc-4.0.2-glibc-2.3.2',
    'gcc-4.0.2-glibc-2.3.2-tls',
    'gcc-4.0.2-glibc-2.3.5',
    'gcc-4.0.2-glibc-2.3.5-tls',
    'gcc-4.0.2-glibc-2.3.6',
    'gcc-4.0.2-glibc-2.3.6-tls',
    'gcc-4.1.0-glibc-2.3.2',
    'gcc-4.1.0-glibc-2.3.2-tls',
  ],
  'armeb': [
    'gcc-3.3.6-glibc-2.2.5',
    'gcc-3.3.6-glibc-2.3.2',
    'gcc-3.3.6-glibc-2.3.2-tls',
    'gcc-3.4.5-glibc-2.2.5',
    'gcc-3.4.5-glibc-2.3.2',
    'gcc-3.4.5-glibc-2.3.2-tls',
    'gcc-3.4.5-glibc-2.3.5',
    'gcc-3.4.5-glibc-2.3.5-tls',
    'gcc-3.4.5-glibc-2.3.6',
    'gcc-3.4.5-glibc-2.3.6-tls',
  ],
  'arm': [
    'gcc-2.95.3-glibc-2.1.3',
    'gcc-2.95.3-glibc-2.2.2',
    'gcc-2.95.3-glibc-2.2.5',
    'gcc-3.2.3-glibc-2.2.5',
    'gcc-3.2.3-glibc-2.3.2',
    'gcc-3.2.3-glibc-2.3.2-tls',
    'gcc-3.3.6-glibc-2.2.2',
    'gcc-3.3.6-glibc-2.2.5',
    'gcc-3.3.6-glibc-2.3.2',
    'gcc-3.3.6-glibc-2.3.2-tls',
    'gcc-3.4.5-glibc-2.2.2',
    'gcc-3.4.5-glibc-2.2.5',
    'gcc-3.4.5-glibc-2.3.2',
    'gcc-3.4.5-glibc-2.3.2-tls',
    'gcc-3.4.5-glibc-2.3.5',
    'gcc-3.4.5-glibc-2.3.5-tls',
    'gcc-3.4.5-glibc-2.3.6',
    'gcc-3.4.5-glibc-2.3.6-tls',
    'gcc-4.0.2-glibc-2.2.2',
    'gcc-4.0.2-glibc-2.3.2',
    'gcc-4.0.2-glibc-2.3.2-tls',
    'gcc-4.0.2-glibc-2.3.5',
    'gcc-4.0.2-glibc-2.3.5-tls',
    'gcc-4.0.2-glibc-2.3.6',
    'gcc-4.0.2-glibc-2.3.6-tls',
    'gcc-4.1.0-glibc-2.2.2',
    'gcc-4.1.0-glibc-2.3.2',
    'gcc-4.1.0-glibc-2.3.2-tls',
  ],
  'arm-iwmmxt': [
    'gcc-3.4.2-glibc-2.3.3',
    'gcc-3.4.5-glibc-2.2.5',
    'gcc-3.4.5-glibc-2.3.5',
    'gcc-3.4.5-glibc-2.3.5-tls',
    'gcc-3.4.5-glibc-2.3.6',
    'gcc-3.4.5-glibc-2.3.6-tls',
  ],
  'arm-softfloat': [
    'gcc-2.95.3-glibc-2.1.3',
    'gcc-2.95.3-glibc-2.2.2',
    'gcc-2.95.3-glibc-2.2.5',
    'gcc-3.2.3-glibc-2.2.5',
    'gcc-3.2.3-glibc-2.3.2',
    'gcc-3.2.3-glibc-2.3.2-tls',
    'gcc-3.3.6-glibc-2.2.2',
    'gcc-3.3.6-glibc-2.2.5',
    'gcc-3.3.6-glibc-2.3.2',
    'gcc-3.3.6-glibc-2.3.2-tls',
    'gcc-3.4.5-glibc-2.2.5',
    'gcc-3.4.5-glibc-2.3.5',
    'gcc-3.4.5-glibc-2.3.6',
  ],
  'armv5b-softfloat': [
    'gcc-3.3.6-glibc-2.2.5',
    'gcc-3.3.6-glibc-2.3.2',
    'gcc-3.3.6-glibc-2.3.2-tls',
    'gcc-3.4.2-glibc-2.2.5',
    'gcc-3.4.5-glibc-2.2.5',
    'gcc-3.4.5-glibc-2.3.5',
    'gcc-3.4.5-glibc-2.3.6',
  ],
  'arm-xscale': [
    'gcc-3.2.3-glibc-2.2.5',
    'gcc-3.2.3-glibc-2.3.2',
    'gcc-3.2.3-glibc-2.3.2-tls',
    'gcc-3.3.6-glibc-2.2.5',
    'gcc-3.3.6-glibc-2.3.2',
    'gcc-3.3.6-glibc-2.3.2-tls',
    'gcc-3.4.5-glibc-2.2.5',
    'gcc-3.4.5-glibc-2.3.2',
    'gcc-3.4.5-glibc-2.3.2-tls',
    'gcc-3.4.5-glibc-2.3.5',
    'gcc-3.4.5-glibc-2.3.5-tls',
    'gcc-3.4.5-glibc-2.3.6',
    'gcc-3.4.5-glibc-2.3.6-tls',
    'gcc-4.0.2-glibc-2.3.2',
    'gcc-4.0.2-glibc-2.3.2-tls',
    'gcc-4.0.2-glibc-2.3.5',
    'gcc-4.0.2-glibc-2.3.5-tls',
    'gcc-4.0.2-glibc-2.3.6',
    'gcc-4.0.2-glibc-2.3.6-tls',
    'gcc-4.1.0-glibc-2.3.2',
    'gcc-4.1.0-glibc-2.3.2-tls',
  ],
  'i686': [
    'gcc-2.95.3-glibc-2.1.3',
    'gcc-2.95.3-glibc-2.1.3',
    'gcc-2.95.3-glibc-2.2.2',
    'gcc-2.95.3-glibc-2.2.5',
    'gcc-3.2.3-glibc-2.2.5',
    'gcc-3.2.3-glibc-2.3.2',
    'gcc-3.3.3-glibc-2.1.3',
    'gcc-3.3.6-glibc-2.1.3',
    'gcc-3.3.6-glibc-2.2.2',
    'gcc-3.3.6-glibc-2.2.5',
    'gcc-3.3.6-glibc-2.3.2',
    'gcc-3.3.6-glibc-2.3.5',
    'gcc-3.3.6-glibc-2.3.5-tls',
    'gcc-3.3.6-glibc-2.3.6',
    'gcc-3.3.6-glibc-2.3.6-tls',
    'gcc-3.4.0-glibc-2.1.3',
    'gcc-3.4.5-glibc-2.2.2',
    'gcc-3.4.5-glibc-2.2.5',
    'gcc-3.4.5-glibc-2.3.2',
    'gcc-3.4.5-glibc-2.3.5',
    'gcc-3.4.5-glibc-2.3.5-tls',
    'gcc-3.4.5-glibc-2.3.6',
    'gcc-3.4.5-glibc-2.3.6-tls',
    'gcc-4.0.2-glibc-2.2.2',
    'gcc-4.0.2-glibc-2.3.2',
    'gcc-4.0.2-glibc-2.3.5',
    'gcc-4.0.2-glibc-2.3.5-tls',
    'gcc-4.0.2-glibc-2.3.6',
    'gcc-4.0.2-glibc-2.3.6-tls',
    'gcc-4.1.0-glibc-2.2.2',
    'gcc-4.1.0-glibc-2.3.2',
    'gcc-4.1.0-glibc-2.3.5',
    'gcc-4.1.0-glibc-2.3.5-tls',
    'gcc-4.1.0-glibc-2.3.6',
    'gcc-4.1.0-glibc-2.3.6-tls',
  ],
  'ia64': [
    'gcc-3.2.3-glibc-2.3.2',
    'gcc-3.2.3-glibc-2.3.2-tls',
    'gcc-3.3.6-glibc-2.3.2',
    'gcc-3.3.6-glibc-2.3.5',
    'gcc-3.3.6-glibc-2.3.5-tls',
    'gcc-3.3.6-glibc-2.3.6',
    'gcc-3.3.6-glibc-2.3.6-tls',
    'gcc-3.4.5-glibc-2.3.2',
    'gcc-3.4.5-glibc-2.3.5',
    'gcc-3.4.5-glibc-2.3.5-tls',
    'gcc-3.4.5-glibc-2.3.6',
    'gcc-3.4.5-glibc-2.3.6-tls',
  ],
  'm68k': [
    'gcc-2.95.3-glibc-2.1.3',
    'gcc-2.95.3-glibc-2.2.2',
    'gcc-3.2.3-glibc-2.3.2',
    'gcc-3.3.6-glibc-2.2.2',
    'gcc-3.3.6-glibc-2.3.2',
    'gcc-3.3.6-glibc-2.3.2-tls',
    'gcc-3.3.6-glibc-2.3.5',
    'gcc-3.3.6-glibc-2.3.6',
    'gcc-3.4.5-glibc-2.2.2',
    'gcc-3.4.5-glibc-2.3.2',
    'gcc-3.4.5-glibc-2.3.2-tls',
    'gcc-3.4.5-glibc-2.3.5',
    'gcc-3.4.5-glibc-2.3.5-tls',
    'gcc-3.4.5-glibc-2.3.6',
    'gcc-3.4.5-glibc-2.3.6-tls',
    'gcc-4.0.2-glibc-2.2.2',
    'gcc-4.0.2-glibc-2.3.2',
    'gcc-4.0.2-glibc-2.3.2-tls',
    'gcc-4.1.0-glibc-2.2.2',
    'gcc-4.1.0-glibc-2.3.2',
    'gcc-4.1.0-glibc-2.3.2-tls',
    'gcc-4.1.0-glibc-2.3.5',
    'gcc-4.1.0-glibc-2.3.5-tls',
    'gcc-4.1.0-glibc-2.3.6',
    'gcc-4.1.0-glibc-2.3.6-tls',
  ],
  'mipsel': [
    'gcc-3.2.3-glibc-2.2.5',
    'gcc-3.2.3-glibc-2.3.2',
    'gcc-3.3.6-glibc-2.2.5',
    'gcc-3.3.6-glibc-2.3.2',
    'gcc-3.3.6-glibc-2.3.2-tls',
    'gcc-3.3.6-glibc-2.3.5',
    'gcc-3.3.6-glibc-2.3.6',
    'gcc-3.4.5-glibc-2.3.2',
    'gcc-3.4.5-glibc-2.3.2-tls',
    'gcc-3.4.5-glibc-2.3.5',
    'gcc-3.4.5-glibc-2.3.5-tls',
    'gcc-3.4.5-glibc-2.3.6',
    'gcc-3.4.5-glibc-2.3.6-tls',
  ],
  'mips': [
    'gcc-3.2.3-glibc-2.2.5',
    'gcc-3.2.3-glibc-2.3.2',
    'gcc-3.3.6-glibc-2.2.5',
    'gcc-3.3.6-glibc-2.3.2',
    'gcc-3.3.6-glibc-2.3.2-tls',
    'gcc-3.3.6-glibc-2.3.5',
    'gcc-3.3.6-glibc-2.3.6',
    'gcc-3.4.5-glibc-2.3.2',
    'gcc-3.4.5-glibc-2.3.2-tls',
    'gcc-3.4.5-glibc-2.3.5',
    'gcc-3.4.5-glibc-2.3.5-tls',
    'gcc-3.4.5-glibc-2.3.6',
    'gcc-3.4.5-glibc-2.3.6-tls',
  ],
  'powerpc-405': [
    'gcc-3.2.3-glibc-2.2.5',
    'gcc-3.2.3-glibc-2.3.2',
    'gcc-3.3.6-glibc-2.2.5',
    'gcc-3.3.6-glibc-2.3.2',
    'gcc-3.3.6-glibc-2.3.5',
    'gcc-3.3.6-glibc-2.3.6',
    'gcc-3.4.5-glibc-2.2.5',
    'gcc-3.4.5-glibc-2.3.2',
    'gcc-3.4.5-glibc-2.3.5',
    'gcc-3.4.5-glibc-2.3.6',
    'gcc-4.0.2-glibc-2.3.2',
    'gcc-4.0.2-glibc-2.3.5',
    'gcc-4.0.2-glibc-2.3.6',
    'gcc-4.1.0-glibc-2.3.2',
    'gcc-4.1.0-glibc-2.3.5',
    'gcc-4.1.0-glibc-2.3.6',
  ],
  'powerpc-603': [
    'gcc-2.95.3-glibc-2.1.3',
    'gcc-2.95.3-glibc-2.2.2',
    'gcc-2.95.3-glibc-2.2.5',
    'gcc-3.2.3-glibc-2.2.5',
    'gcc-3.2.3-glibc-2.3.2',
    'gcc-3.2.3-glibc-2.3.2-tls',
    'gcc-3.3.6-glibc-2.2.2',
    'gcc-3.3.6-glibc-2.2.5',
    'gcc-3.3.6-glibc-2.3.2',
    'gcc-3.3.6-glibc-2.3.2-tls',
    'gcc-3.3.6-glibc-2.3.5',
    'gcc-3.3.6-glibc-2.3.5-tls',
    'gcc-3.3.6-glibc-2.3.6',
    'gcc-3.3.6-glibc-2.3.6-tls',
    'gcc-3.4.5-glibc-2.2.2',
    'gcc-3.4.5-glibc-2.2.5',
    'gcc-3.4.5-glibc-2.3.2',
    'gcc-3.4.5-glibc-2.3.2-tls',
    'gcc-3.4.5-glibc-2.3.5',
    'gcc-3.4.5-glibc-2.3.5-tls',
    'gcc-3.4.5-glibc-2.3.6',
    'gcc-3.4.5-glibc-2.3.6-tls',
    'gcc-4.0.2-glibc-2.2.2',
    'gcc-4.0.2-glibc-2.3.2',
    'gcc-4.0.2-glibc-2.3.2-tls',
    'gcc-4.0.2-glibc-2.3.5',
    'gcc-4.0.2-glibc-2.3.6',
    'gcc-4.0.2-glibc-2.3.6-tls',
    'gcc-4.1.0-glibc-2.2.2',
    'gcc-4.1.0-glibc-2.3.2',
    'gcc-4.1.0-glibc-2.3.2-tls',
    'gcc-4.1.0-glibc-2.3.5',
    'gcc-4.1.0-glibc-2.3.5-tls',
    'gcc-4.1.0-glibc-2.3.6',
    'gcc-4.1.0-glibc-2.3.6-tls',
  ],
  'powerpc-750': [
    'gcc-2.95.3-glibc-2.1.3',
    'gcc-2.95.3-glibc-2.2.2',
    'gcc-2.95.3-glibc-2.2.5',
    'gcc-3.2.3-glibc-2.2.5',
    'gcc-3.2.3-glibc-2.3.2',
    'gcc-3.2.3-glibc-2.3.2-tls',
    'gcc-3.3.6-glibc-2.2.2',
    'gcc-3.3.6-glibc-2.2.5',
    'gcc-3.3.6-glibc-2.3.2',
    'gcc-3.3.6-glibc-2.3.2-tls',
    'gcc-3.3.6-glibc-2.3.5',
    'gcc-3.3.6-glibc-2.3.5-tls',
    'gcc-3.3.6-glibc-2.3.6',
    'gcc-3.3.6-glibc-2.3.6-tls',
    'gcc-3.4.5-glibc-2.2.2',
    'gcc-3.4.5-glibc-2.2.5',
    'gcc-3.4.5-glibc-2.3.2',
    'gcc-3.4.5-glibc-2.3.2-tls',
    'gcc-3.4.5-glibc-2.3.5',
    'gcc-3.4.5-glibc-2.3.5-tls',
    'gcc-3.4.5-glibc-2.3.6',
    'gcc-3.4.5-glibc-2.3.6-tls',
    'gcc-4.0.2-glibc-2.2.2',
    'gcc-4.0.2-glibc-2.3.2',
    'gcc-4.0.2-glibc-2.3.2-tls',
    'gcc-4.0.2-glibc-2.3.5',
    'gcc-4.0.2-glibc-2.3.6',
    'gcc-4.0.2-glibc-2.3.6-tls',
    'gcc-4.1.0-glibc-2.2.2',
    'gcc-4.1.0-glibc-2.3.2',
    'gcc-4.1.0-glibc-2.3.2-tls',
    'gcc-4.1.0-glibc-2.3.5',
    'gcc-4.1.0-glibc-2.3.5-tls',
    'gcc-4.1.0-glibc-2.3.6',
    'gcc-4.1.0-glibc-2.3.6-tls',
  ],
  'powerpc-860': [
    'gcc-2.95.3-glibc-2.2.5',
    'gcc-3.2.3-glibc-2.2.5',
    'gcc-3.2.3-glibc-2.3.2',
    'gcc-3.3.6-glibc-2.2.5',
    'gcc-3.3.6-glibc-2.3.2',
    'gcc-3.3.6-glibc-2.3.5',
    'gcc-3.3.6-glibc-2.3.6',
    'gcc-3.4.5-glibc-2.2.5',
    'gcc-3.4.5-glibc-2.3.2',
    'gcc-3.4.5-glibc-2.3.5',
    'gcc-3.4.5-glibc-2.3.6',
    'gcc-4.0.2-glibc-2.3.2',
    'gcc-4.0.2-glibc-2.3.5',
    'gcc-4.0.2-glibc-2.3.6',
    'gcc-4.1.0-glibc-2.3.2',
    'gcc-4.1.0-glibc-2.3.5',
    'gcc-4.1.0-glibc-2.3.6',
  ],
  'powerpc-970': [
    'gcc-3.4.5-glibc-2.3.2',
    'gcc-3.4.5-glibc-2.3.5',
    'gcc-3.4.5-glibc-2.3.5-tls',
    'gcc-3.4.5-glibc-2.3.6',
    'gcc-3.4.5-glibc-2.3.6-tls',
    'gcc-4.0.2-glibc-2.3.2',
    'gcc-4.0.2-glibc-2.3.5',
    'gcc-4.0.2-glibc-2.3.6',
    'gcc-4.0.2-glibc-2.3.6-tls',
    'gcc-4.1.0-glibc-2.3.2',
    'gcc-4.1.0-glibc-2.3.5',
    'gcc-4.1.0-glibc-2.3.5-tls',
    'gcc-4.1.0-glibc-2.3.6',
    'gcc-4.1.0-glibc-2.3.6-tls',
  ],
  's390': [
    'gcc-3.2.3-glibc-2.3.2',
    'gcc-3.3.6-glibc-2.3.2',
    'gcc-3.3.6-glibc-2.3.2-tls',
    'gcc-3.3.6-glibc-2.3.5',
    'gcc-3.3.6-glibc-2.3.6',
    'gcc-3.4.5-glibc-2.3.2',
    'gcc-3.4.5-glibc-2.3.2-tls',
    'gcc-3.4.5-glibc-2.3.5',
    'gcc-3.4.5-glibc-2.3.5-tls',
    'gcc-3.4.5-glibc-2.3.6',
    'gcc-3.4.5-glibc-2.3.6-tls',
    'gcc-4.0.2-glibc-2.3.2',
    'gcc-4.0.2-glibc-2.3.6',
    'gcc-4.0.2-glibc-2.3.6-tls',
    'gcc-4.1.0-glibc-2.3.2',
    'gcc-4.1.0-glibc-2.3.5',
    'gcc-4.1.0-glibc-2.3.5-tls',
    'gcc-4.1.0-glibc-2.3.6',
    'gcc-4.1.0-glibc-2.3.6-tls',
  ],
  'sh3': [
    'gcc-3.4.5-glibc-2.3.2',
    'gcc-3.4.5-glibc-2.3.2-tls',
    'gcc-3.4.5-glibc-2.3.5',
    'gcc-3.4.5-glibc-2.3.6',
    'gcc-4.0.2-glibc-2.3.2',
    'gcc-4.0.2-glibc-2.3.2-tls',
    'gcc-4.0.2-glibc-2.3.5',
    'gcc-4.0.2-glibc-2.3.6',
    'gcc-4.1.0-glibc-2.3.2',
    'gcc-4.1.0-glibc-2.3.2-tls',
    'gcc-4.1.0-glibc-2.3.5',
    'gcc-4.1.0-glibc-2.3.6',
  ],
  'sh4': [
    'gcc-3.3.6-glibc-2.2.5',
    'gcc-3.3.6-glibc-2.3.2',
    'gcc-3.3.6-glibc-2.3.2-tls',
    'gcc-3.3.6-glibc-2.3.5',
    'gcc-3.3.6-glibc-2.3.6',
    'gcc-3.4.5-glibc-2.3.2',
    'gcc-3.4.5-glibc-2.3.2-tls',
    'gcc-3.4.5-glibc-2.3.5',
    'gcc-3.4.5-glibc-2.3.6',
    'gcc-4.0.2-glibc-2.3.2',
    'gcc-4.0.2-glibc-2.3.2-tls',
    'gcc-4.0.2-glibc-2.3.5',
    'gcc-4.0.2-glibc-2.3.6',
    'gcc-4.1.0-glibc-2.3.2',
    'gcc-4.1.0-glibc-2.3.2-tls',
    'gcc-4.1.0-glibc-2.3.5',
    'gcc-4.1.0-glibc-2.3.6',
  ],
  'sparc64': [
    'gcc-3.4.5-glibc-2.3.5',
    'gcc-3.4.5-glibc-2.3.5-tls',
    'gcc-3.4.5-glibc-2.3.6',
    'gcc-3.4.5-glibc-2.3.6-tls',
  ],
  'sparc': [
    'gcc-2.95.3-glibc-2.2.5',
    'gcc-3.2.3-glibc-2.3.2',
    'gcc-3.2.3-glibc-2.3.2-tls',
    'gcc-3.3.6-glibc-2.2.5',
    'gcc-3.3.6-glibc-2.3.2',
    'gcc-3.3.6-glibc-2.3.2-tls',
    'gcc-3.3.6-glibc-2.3.5',
    'gcc-3.3.6-glibc-2.3.5-tls',
    'gcc-3.3.6-glibc-2.3.6',
    'gcc-3.3.6-glibc-2.3.6-tls',
    'gcc-3.4.5-glibc-2.3.2',
    'gcc-3.4.5-glibc-2.3.2-tls',
    'gcc-3.4.5-glibc-2.3.5',
    'gcc-3.4.5-glibc-2.3.5-tls',
    'gcc-3.4.5-glibc-2.3.6',
    'gcc-3.4.5-glibc-2.3.6-tls',
    'gcc-4.0.2-glibc-2.3.2',
    'gcc-4.0.2-glibc-2.3.2-tls',
    'gcc-4.1.0-glibc-2.3.2',
    'gcc-4.1.0-glibc-2.3.2-tls',
    'gcc-4.1.0-glibc-2.3.5',
    'gcc-4.1.0-glibc-2.3.5-tls',
    'gcc-4.1.0-glibc-2.3.6',
    'gcc-4.1.0-glibc-2.3.6-tls',
  ],
  'x86_64': [
    'gcc-3.3.3-glibc-2.3.2',
    'gcc-3.3.6-glibc-2.3.2',
    'gcc-3.3.6-glibc-2.3.2-tls',
    'gcc-3.3.6-glibc-2.3.5',
    'gcc-3.3.6-glibc-2.3.5-tls',
    'gcc-3.3.6-glibc-2.3.6',
    'gcc-3.3.6-glibc-2.3.6-tls',
    'gcc-3.4.0-glibc-2.3.2',
    'gcc-3.4.5-glibc-2.3.2',
    'gcc-3.4.5-glibc-2.3.2-tls',
    'gcc-3.4.5-glibc-2.3.5',
    'gcc-3.4.5-glibc-2.3.5-tls',
    'gcc-3.4.5-glibc-2.3.6',
    'gcc-3.4.5-glibc-2.3.6-tls',
    'gcc-4.0.2-glibc-2.3.2',
    'gcc-4.0.2-glibc-2.3.5',
    'gcc-4.0.2-glibc-2.3.5-tls',
    'gcc-4.0.2-glibc-2.3.6',
    'gcc-4.0.2-glibc-2.3.6-tls',
    'gcc-4.1.0-glibc-2.3.2',
    'gcc-4.1.0-glibc-2.3.5',
    'gcc-4.1.0-glibc-2.3.5-tls',
    'gcc-4.1.0-glibc-2.3.6',
    'gcc-4.1.0-glibc-2.3.6-tls',
  ]
}

if __name__ == '__main__':
    main()

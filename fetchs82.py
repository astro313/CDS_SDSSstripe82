#!/usr/bin/env python

import sys
import os

#- Template rsync command to run:
# --dry-run
cmd_template = """rsync -aLvz --prune-empty-dirs --progress \
    --include "%s/" --include "?/" --include "frame*.fits.bz2" \
    --exclude "*" \
    rsync://data.sdss3.org/dr12/env/BOSS_PHOTOOBJ/frames/%s/ ./%s/"""

#- Loop over CSV file from CAS
fx = open(sys.argv[1])
fx.readline()  # - clear "rerun,run" header
for line in fx:
    rerun, run = line.strip().split(',')
    cmd = cmd_template % (run, rerun, rerun)
    print cmd
    err = os.system(cmd)
    if err != 0:
        print "ERROR downloading RERUN %s RUN %s" % (rerun, run)

fx.close()

"""Deploys a named file into the MAC shared-phone dropbox account"""

import os
import shutil

def main(fp):
    shutil.copy(fp, os.path.expanduser('~/Dropbox/shared-phone/main.py'))


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print 'Usage: deploy <directory containing main.py>'
        sys.exit(1)
    adir = sys.argv[1]
    if not os.path.isdir(adir):
        print 'Invalid directory %s' % adir
        sys.exit(1)
    fp = os.path.join(adir, 'main.py')
    if not os.path.isfile(fp):
        print "Failed to find 'main.py' in (existing) '%s'" % adir
        sys.exit(1)

    main(fp)

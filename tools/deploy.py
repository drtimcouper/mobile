"""Deploys a named file into the MAC shared-phone dropbox account"""

import os
import shutil

IGNORE_STARTSWITHS = ('.', 'build.', 'README.', 'test_')
IGNORE_ENDSWITHS = ('.pyc',)

def main(adir):
    basedir = os.path.basename(adir)
    tgt_dir = os.path.expanduser('~/Dropbox/shared-phone/%s' % basedir)
    shutil.rmtree(tgt_dir, ignore_errors=True)
    try:
        os.makedirs(tgt_dir)
    except OSError:
        pass

    for fn in sorted(os.listdir(adir)):
        if fn.startswith(IGNORE_STARTSWITHS):
            continue
        if fn.endswith(IGNORE_ENDSWITHS):
            continue
        #print 'copying %s' % fn
        src = os.path.join(adir, fn)
        tgt = os.path.join(tgt_dir,fn)
        if os.path.isfile(src):
            func = shutil.copy
        else:
            func = shutil.copytree
        func(src,tgt)


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

    main(adir)

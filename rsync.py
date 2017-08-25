from subprocess import Popen, PIPE
import sys

def sync(src, dest):
    cmd = ['rsync', '-avz', '--progress', src, dest]
    p = Popen(cmd, stdout=PIPE)
    line = ''
    while True:
        c = p.stdout.read(1)
        if not c:
            break
        if c in ['\n', '\r']:
            sys.stdout.write('rsync progress: %s\r' % line)
            sys.stdout.flush()
            line = ''
        else:
            line += c
    sys.stdout.write('\n')
    sys.stdout.flush()

sync(sys.argv[1], sys.argv[2])

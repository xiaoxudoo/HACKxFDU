import os, sys, select, subprocess

args = ['mode2', '-d', '/dev/lirc0']
p1 = subprocess.Popen(args, stdout=subprocess.PIPE)
p2 = subprocess.Popen(args, stdout=subprocess.PIPE)

while True:
    rlist, wlist, xlist = select.select([p1.stdout, p2.stdout], [], [])
    for stdout in rlist:
        output = os.read(stdout.fileno(), 1024).decode('utf-8')
        if output:
            sys.stdout.write('indicator: ' + output)
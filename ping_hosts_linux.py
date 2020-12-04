#!/usr/bin/env python3
import os
import time
from subprocess import Popen, DEVNULL
				  
print('Loading the contents of "hosts.txt" file...')

f = open ("hosts.txt")

p = {} # ip -> process
for line in f:
    HOST = line.strip()										  												
    p[HOST] = Popen(['ping', '-n', '-w5', '-c3', HOST], stdout=DEVNULL)								

while p:
    for HOST, proc in p.items():
        if proc.poll() is not None: # ping finished
            del p[HOST] # remove from the process list
            if proc.returncode == 0:
                print('%s alive' % HOST)
            elif proc.returncode == 1:
                print('%s down' % HOST)
            else:
                print('%s error' % HOST)
            break

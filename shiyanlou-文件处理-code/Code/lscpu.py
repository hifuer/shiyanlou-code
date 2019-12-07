#!/usr/bin/env python3
with open('/proc/cpuinfo') as cpu:
    for c in cpu:
        print(c,end='')
    print()

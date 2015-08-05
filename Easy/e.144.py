#!/usr/bin/env python

with open('file.txt') as f:
    n = int(f.readline())
    data = [line.strip('\n').split() for line in f.readlines()]
    oldist, newlist = data[: n], data[n:]

for k1, v1 in oldist:
    for k2, v2 in newlist:
        if k1 == k2 and v1 != v2:
            print "{} {:+}".format(k1, int(v2) - int(v1))
#!/usr/bin/env python

import sys, math
n, b = map(float, sys.argv[1:])
print "{:.3f}".format(2 * n * b * math.sin(math.pi / n))

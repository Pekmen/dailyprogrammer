#!/usr/bin/env python

prompt = raw_input().split()
base = int(prompt[0])
tsymb, lsymb = prompt[1:]

lvl = 1
while lvl <= base:
    print(base - lvl) / 2 * " ", lvl * lsymb
    lvl += 2
print(base - 3) / 2 * " ", 3 * tsymb
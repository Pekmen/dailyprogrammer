#!/usr/bin/env python

import string

def isPangram(sentence):
    d = dict.fromkeys(string.ascii_lowercase, 0)
    aftermath = ''
    for ch in sentence:
        if ch.lower() in d:
            d[ch.lower()] += 1
    for ch in string.ascii_lowercase:
        aftermath += "%s: %d, " %(ch, d[ch])
    return all(v > 0 for v in d.values()), aftermath[:-2]


def main():
    n = int(raw_input())
    results = [isPangram(raw_input()) for i in range(n)]
    print ""
    for i in results:
        print i[0], i[1]
main()



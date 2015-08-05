#!/usr/bin/env python3

##
#  [Easy] #224
#
#  Shuffling a List
#
#  https://www.reddit.com/r/dailyprogrammer/comments/3e0hmh/20150720_challenge_224_easy_shuffling_a_list/
##

import time

def myrandom(minn, maxn):
    import time
    return int(minn + ((time.time()*123%1)*(maxn-minn)))

def main():
    values = input("Enter space separated values:\n").split()
    for i in range(len(values)-1, 0, -1):
        randn = myrandom(0, i)
        values[i], values[randn] = values[randn], values[i]
    print(" ".join(values))

main()



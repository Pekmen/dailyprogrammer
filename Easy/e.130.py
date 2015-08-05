#!/usr/bin/env python

from random import randint

def dice_roll(NdM):
        results = []
	n,m = NdM.split('d')
	for i in range(0,int(n)):
            results.append(str(randint(1,int(m))))
        for item in results:
            print item,
        

dice_roll('0d0')

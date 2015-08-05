#!/usr/bin/env python

def eucl_alg(a,b):
	rem = a % b
	if rem == 0:
		return b
	else:
		return eucl_alg(b, rem)

def gcd(x,y):
	if x > y:
		return eucl_alg(x,y)
	return eucl_alg(y,x)

print gcd (142341 ,512345)
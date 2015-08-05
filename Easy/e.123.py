#!/usr/bin/env python
	
def dig_root (n):
	if n < 10:
		return n
	result = 0
	while n>0:
		result += n % 10
		n = (n - (n % 10)) / 10
	return dig_root(result)



print dig_root(31337)

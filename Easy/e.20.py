#!/usr/bin/env python3

def is_prime(n):
	if n == 1:
		return False
	for i in range(2, n):
		if n % i == 0:
			return False
	return True

print(", ".join([str(i) for i in range(1, 2000) if is_prime(i)]))


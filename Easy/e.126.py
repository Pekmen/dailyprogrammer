#!/usr/bin/env python

def merge_sort(a,b):
	for num in a:
		if num not in b:
			b.append(num)
	while b[0] == 0:
		del(b[0])
	print sorted(b)

merge_sort([692,1,32], [0,0,0,14,15,123,2431])
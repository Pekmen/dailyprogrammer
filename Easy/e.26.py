#!/usr/bin/env python3

mystring = "aabbccddeded"
cleaned=""
remainder=""
for i in range(len(mystring)-1):
	if mystring[i] != mystring[i+1]:
		cleaned+=mystring[i]
	else:
		remainder+=mystring[i]
cleaned+=mystring[len(mystring)-1]

print(cleaned)
print(remainder)

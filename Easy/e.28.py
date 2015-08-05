#!/usr/bin/env python3

from random import randint

def populate(size):
	return [randint(1, size*100) for i in range(size)]

def get_duplicates(array):
	duparray= []
	array2 = array[:]
	array2.sort()
	for i in range(len(array2)):
		if array2[i] == array[i]:
			duparray.append(array2[i])
	return (len(duparray), duparray)

def main():
    size = int(input("What size array should be? "))
    print("Populating...")
    mylist = populate(size)

    print("Searching for duplicates...")
    duplicates = get_duplicates(mylist)
    
    print("{} duplicates found".format(duplicates[0]))
    print(duplicates[1])


main()
#!/usr/bin/env python3

from random import randint

def generate_array(size):
	return[randint(1, size*100) for _ in range(size)]

def partition(array):
    i = 0
    j = len(array) - 1
    while i < j:
        while array[i] %2 == 0 and i < j:
            i += 1
        while array[j] %2 != 0 and i < j:
            j -= 1
        if i < j:
            array[i], array[j] = array[j], array[i]

    print(array)


        


def main():
	size = 10
	mylist = generate_array(10)
	partition(mylist)

main()

#!/usr/bin/env python3

list1 = ["a","b","c",1,4]
list2 = ["a", "x", 34, "4"]
list1 += [x for x in list2 if x not in list1]

print(list1)
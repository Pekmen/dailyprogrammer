mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
separator = int(len(mylist) / 2)

list1, list2 = mylist[:separator], mylist[separator:]

print (list1, list2)
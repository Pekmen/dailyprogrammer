# fast as hell

from random import randint
from bisect import bisect

def populate(size, maxn):
	return [randint(0, maxn) for _ in range(size)]

def get_sums(array, K):
    arr = sorted(array[:])
    first_greater = bisect(arr, K)
    arr = arr[:first_greater]
    hashtbl = {arr[i]: i for i in range(len(arr))}
    sum_pairs = []
    for i in range(0, len(arr)-1):
        if K - arr[i] in hashtbl and hashtbl[K - arr[i]] != i:
            sum_pairs.append((K - arr[i], arr[i]))
    return(set([tuple(sorted(l)) for l in sum_pairs]))
	
def main():
    maxn = 50
    size = 1000000
    target = 69

    print("Populating list...")
    mylist = populate(size, maxn)

    print("Finding sum pairs")
    sum_pairs = get_sums(mylist, target)

    if sum_pairs:
        for pair in sum_pairs:
            print("{} + {} = {}".format(pair[0], pair[1], target))

main()
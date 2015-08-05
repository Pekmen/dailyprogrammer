#!/usr/bin/env python3

from itertools import permutations

target = input("enter number: ")
larger_perms = [int("".join(n)) for n in permutations(str(target)) if int("".join(n)) > int(target)]
print(min(larger_perms))

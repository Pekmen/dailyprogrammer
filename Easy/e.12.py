#!/usr/bin/env python3

import itertools

permutations = itertools.permutations(input("Your string:\n"))
for permutation in permutations:
	print("".join(permutation))
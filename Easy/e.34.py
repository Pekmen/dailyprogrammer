#!/usr/bin/env python3

from math import sqrt

nums = sorted([int(x) for x in input("Enter 3 numbers: ").split()])
print(sqrt(nums[1])+ sqrt(nums[2]))
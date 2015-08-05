#!/usr/bin/env python3

message = input("Enter a sentence: ")
print("*" * (len(message) + 4))
print("* {} *".format(" "*len(message)))
print("* {} *".format(message))
print("* {} *".format(" "*len(message)))
print("*" * (len(message) + 4))
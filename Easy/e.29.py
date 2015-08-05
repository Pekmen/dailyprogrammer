#!/usr/bin/env python3

mystring = "hannah"

def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome(mystring))
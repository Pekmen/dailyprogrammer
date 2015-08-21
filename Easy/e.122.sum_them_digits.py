#!/usr/bin/env python3

##
#  [Easy] #122
#
#  Sum Them Digits
#
#  https://www.reddit.com/r/dailyprogrammer/comments/1berjh/040113_challenge_122_easy_sum_them_digits/
##


def sum_digits(n):
    return (1 + (n-1) % 9)


def main():
    print(sum_digits(31337))


if __name__ == "__main__":
    main()
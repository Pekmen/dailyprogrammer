##
#  [Easy] #218
#
#  Making Numbers Palindromic
#
#  https://www.reddit.com/r/dailyprogrammer/comments/38yy9s/20150608_challenge_218_easy_making_numbers/
##

from sys import argv


def palindromize(n):
    return n + int(str(n)[::-1])

def is_palindrome(n):
    n = str(n)
    return n == n[::-1]

def main():
    seed = int(argv[1])
    n = seed
    steps = 0;
    while (not is_palindrome(n)) and steps <= 10000:
        n = palindromize(n)
        steps += 1
    if steps >= 10000:
       print("Could not palindromize {} in 10000 steps\n".format(seed))
    else:
       print("{} gets palindromic after {} steps: {}".format(seed, steps, n))

main()

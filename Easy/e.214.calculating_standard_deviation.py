##
#  [Easy] #214
#
#  Calciulating the standard deviation
#
#  http://www.reddit.com/r/dailyprogrammer/comments/35l5eo/20150511_challenge_214_easy_calculating_the/
##

from sys import argv
from math import sqrt, pow

popul = [int(a) for a in argv[1:]];
std_dev = sqrt(sum([pow(n - (sum(popul) / len(popul)), 2) for n in popul], ) / len(popul));
print("{0:.4f}".format(std_dev));
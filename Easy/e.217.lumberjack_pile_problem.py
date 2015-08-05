#!/usr/bin/env python3

##
#  [Easy] #217
#
#  Texas Hold 'Em 1 of 3 - Let's deal.
#
#  http://www.reddit.com/r/dailyprogrammer/comments/378h44/20150525_challenge_216_easy_texas_hold_em_1_of_3/
##

n = 3;
logs = 7;
piles = [1, 1, 1, 2, 1, 3, 1, 4, 1];

for i in range(logs):
	piles[piles.index(min(piles))] += 1;

for i in range(0, n*n, n):
	print(' '.join(str(p) for  p in piles[i:i + n]));
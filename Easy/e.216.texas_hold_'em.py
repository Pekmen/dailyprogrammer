#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##
#  [Easy] #216
#
#  Texas Hold 'Em 1 of 3 - Let's deal.
#
#  http://www.reddit.com/r/dailyprogrammer/comments/378h44/20150525_challenge_216_easy_texas_hold_em_1_of_3/
##

import itertools
import random


suits = u'♠♥♦♣';
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'A', 'J', 'Q', 'K'];
deck = [''.join(card) for card in itertools.product(values, suits)];
random.shuffle(deck);

pnum = int(input("How many players? [2 - 8]: "));
hands = [["Your hand"]] + [["CPU {} hand".format(i)] for i in range(1, pnum)];

# deal one card to each players for two turns, like it should be done
for i in range(2):
    for j in range(len(hands)):
    	hands[j].append(deck.pop());
        
for hand in hands:
	print('{}: {}, {}'.format(*hand));
print();

flop = [deck.pop() for i in range(3)];

# card argument should be 'Burn', 'Turn' or 'River'
show_next = lambda card: print('{}: {}'.format(card, deck.pop()));

show_next('Burn');
print("Flop: {}, {}, {}".format(*flop));
show_next('Burn');
show_next('Turn');
show_next('Burn');
show_next('River');
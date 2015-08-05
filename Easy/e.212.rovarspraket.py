#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##
#  [Easy] #212
#
#  Rövarspråket
#
#  http://www.reddit.com/r/dailyprogrammer/comments/341c03/20150427_challenge_212_easy_r%C3%B6varspr%C3%A5ket/
##


sentence = "I'm speaking Robber's language!";
vowels = u'AEIOUYÅÄÖ';
consonants = 'BCDFGHJKLMNPQRSTVXZW'
rovar = '';

for letter in sentence:
	if str.upper(letter) in consonants:
		rovar += '{}o{}'.format(letter, str.lower(letter));
	else:
		rovar += letter;

print(rovar);
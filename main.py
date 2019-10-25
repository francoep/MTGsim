'''
Main script to run a simulation of a game set-up

Currently working on simulating (from a Deck)
	0) implement War for 2 players
	1) how likely a given 7-card hand will result in a t2 Hogaak.
	2) How many turns does it take for a burn list to GoldFish?

TODO -- implement the thing LOL
'''

from class_defs import Card
#from class_defs import Player
from class_defs import Deck
from class_defs import card_parser

#making the initial decklist -- standard 52 card deck
with open('decklist.txt','w') as outfile:
	for suit in ['Diamonds','Hearts','Clubs','Spades']:
		for val in ['Ace','2','3','4','5','6','7','8','9','Jack','Queen','King']:
			outfile.write(suit+' '+val+'\n')

discard=Deck()
library=Deck('decklist.txt')

print(discard)
print(library)

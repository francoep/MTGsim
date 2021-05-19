#/usr/bin/env python3

'''
Main script to run a simulation of a game set-up

This script defines a Player -- and plays a simulated game of MTGburn
'''

from class_defs import Card
from class_defs import Deck
from class_defs import card_parser
import argparse
import numpy as np 

def parse_args(argv=None):
	parser=argparse.ArgumentParser(description='Play a Goldfish game of MTG -- Burn')
	parser.add_argument('-n','--num_to_play',type=int,help='Number of games to play. Defaults to 1',default=1)
	parser.add_argument('-d','--deckfile',type=str,help='File with the decklist. Defaults to burn.decklist',default='burn.decklist')
	parser.add_argument('-q','--quiet',action='store_true',help='Flag to suppress output.',default=False)
	parser.add_argument('-e','--end_life',type=int,default=20,help='Amount of damage needed to deal to end the game. Defaults to 20')
	args=parser.parse_args(argv)
	return args

class Player:
	'''
	Class to hold 1 players library, discard pile, lands, and creatures
		Discard -- initially an empty deck
		library -- initially an enitre MTG decklist
		lands -- a deck with the played lands in it
		creatures -- a deck with the played creatures in it
	'''

	def __init__(self,library,discard,lands,creatures):
		self.library=library #player deck -- class Deck
		self.discard=discard #player dicard -- class Deck
		self.lands=lands #player lands -- class Deck
		self.creatures=creatures #player creatures -- class Deck

	def draw(self):
		'''
		Function to draw a card from the library.
		'''

		if self.decksize() == 0:
			pass
		else:
			return self.library.draw()

	def decksize(self):
		return self.library.size()

	def discsize(self):
		return self.discard.size()

	def add2discard(self,card):
		self.discard.add(card)

	def add2lands(self,card):
		self.lands.add(card)

	def add2creatures(self,card):
		self.creatures.add(card)

def play_game(p1,end_life):
	'''
	Function that takes in a player & plays MTG burn until end_life damage has been dealt

	i) If not turn 0, the player will draw a card
	ii) if possible, the player will play a land from their hand
		a) Fetch & crack
		b) dual
		c) mountain
	iii) if possible, the player will play as many non-spectacle, non-suspend cards from their hand
		a) creatures
		b) spells
	iv) the player will attack with all of their creatures
	v) if possible, the player will play as many spectacle cards from their hand
	vi) if possible, the player will play as many suspend cards from their hand
	
	TODO -- Start the implementation & modification of the classes as needed.
			& make a better heuristic for ending the game...
	'''

	damage_dealt=0

	hand=Deck()
	lands_inplay=Deck()
	creatures_inplay=Deck()
	grave=Deck()

	for i in range(7):
		hand.add(p1.draw())

	#tracker for how many turns it takes
	turn_counter=1
	#main loop
	while damage_dealt<end_life:
		if turn_counter>1:
			hand.add(p1.draw())

		#step 1 play a land:
		hand_contents=hand.get_card_list()

		if 'Fetch' in hand_contents:
			grave.add(hand_contents.get_card('Fetch'))
			
	
if __name__=='__main__':
	args=parse_args()

	#testing the decklist making function
	p1=Player(Deck(args.deckfile),Deck(),Deck(),Deck())
	print(p1)
	print(p1.decksize())
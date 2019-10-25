'''
Class Definitions for the simulator.

Player -- Thing to hold Decks & drive playing the game.
		i) Deck -- Hand
		ii) Deck -- Board
		iii) Deck -- Library
		iv) Deck -- Graveyard
		v) Play card function
		vi) A checker function to report list of card properties given a deck

Deck -- container to hold cards.
		i) Need way to report what is in play --test
		ii) A way to shuffle --test
		iii) A way to remove cards
		iv) A way to add cards

Card -- The workhorse of the game.
		i) Need cost
			a. total
			b. colors
		ii) Type
		iii) Play effects
		iv) graveyard effects.
		v) ??

Parser -- engine to Parse Cards & their effects from a text file with a given formatting.
'''

import random

def card_parser(fname):
	'''
	Function to read in a text file that contains the information to make a card

	TODO -- Make this work for Magic
	'''

	card_list=[]

	with open(fname) as infile:
		for line in infile:
			items=line.rstrip().split()
			suit=items[0]
			value=items[1]

			card=Card(suit,value)
			card_list.append(card)

	return card_list


class Card:
	def __init__(self,suit,value):
		self.suit=suit
		self.value=value

	def __str__(self):
		return "%s of %s" % (self.value,self.suit)


class Deck:
	def __init__(self,fname=None):
		if fname:
			self.card_list=card_parser(fname) #TODO -- build parser
			self.shuffle()

		else:
			self.card_list=[]

	def shuffle(self):
		'''
		Function to shuffle the deck
		'''
		new_list=random.sample(self.card_list,len(self.card_list))
		self.card_list=new_list

	def __str__(self):
		'''
		Function to print the card names in a given zone.

		TODO instead have it return a list of tuples of Name:State for the cards.
		'''
		if self.card_list:
			for card in self.card_list:
				print(card)
			return ''
		else:
			return 'I am empty\n'

	def add_and_shuf(self,card):
		self.card_list.append(card)
		self.shuffle()

	def add(self,card):
		self.card_list.append(card)

	def draw(self):
		'''
		Function that pops the top card of the deck and returns it

		**NOTE THIS FUNCTION REMOVES IT FROM CARD_LIST!!
		'''

		return self.card_list.pop()
		
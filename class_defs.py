'''
Class Definitions for the simulator.

Deck -- container to hold cards.
		i) Need way to report what is in play --test
		ii) A way to shuffle --test
		iii) A way to remove cards
		iv) A way to add cards

StdCard

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

def std_card_parser(fname):
	'''
	Function to read in a text file that contains the information to make a card
	'''

	card_list=[]

	with open(fname) as infile:
		for line in infile:
			items=line.rstrip().split()
			suit=items[0]
			value=items[1]

			card=StdCard(suit,value)
			card_list.append(card)

	return card_list


class StdCard:
	def __init__(self,suit,value):
		self.suit=suit
		self.value=value

	def __str__(self):
		return "%s of %s" % (self.value,self.suit)

	def get_comparison(self):
		'''
		Function to determine the value of the card. Aces are the highest
		'''
		if len(self.value)==1:
			return int(self.value)
		elif self.value=='10':
			return 10
		elif self.value=='Jack':
			return 11
		elif self.value=='Queen':
			return 12
		elif self.value=='King':
			return 13
		else:
			return 14


class StdDeck:
	def __init__(self,fname=None):
		if fname:
			self.card_list=std_card_parser(fname) #TODO -- build parser
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
		'''
		Functino to add a card to the current deck -- puts it on the bottom.
		'''
		self.card_list.append(card)

	def draw(self):
		'''
		Function that pops the top card of the deck and returns it

		**NOTE THIS FUNCTION REMOVES IT FROM CARD_LIST!!
		'''

		return self.card_list.pop()

	def size(self):
		'''
		Function that returns the number of cards present in the Deck.
		'''

		return len(self.card_list)

	def get_card_list(self):
		return self.card_list

###############################################################
##Below Here is where the MTG simulation type things are done##
###############################################################
def card_parser(fname):
	'''
	Function to read in a text file that contains the information to make a card
	'''

	card_list=[]

	with open(fname) as infile:
		for line in infile:
			name,amount,cost,cardtype,pt,abilities=line.rstrip().split(',')
			for i in range(int(amount)):
				card=Card(name,cost,cardtype,pt,abilities)
				card_list.append(card)

	return card_list

class Card:
	def __init__(self,name,cost,cardtype,pt,abilities):
		self.name=name
		self.cost=cost
		self.cardtype=cardtype
		self.pt=pt
		self.abilities=abilities

	def __str__(self):
		return "Played %s" % (self.name)

	def get_cost(self):
		'''
		Function to determine the manacost of the card
		'''
		return self.cost

	def get_cardtype(self):
		return self.cardtype

	def get_pt(self):
		return self.pt

	def get_abilities(self):
		return self.abilities

	def get_name(self):
		return self.name

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
		'''
		Functino to add a card to the current deck -- puts it on the bottom.
		'''
		self.card_list.append(card)

	def draw(self):
		'''
		Function that pops the top card of the deck and returns it

		**NOTE THIS FUNCTION REMOVES IT FROM CARD_LIST!!
		'''

		return self.card_list.pop()

	def size(self):
		'''
		Function that returns the number of cards present in the Deck.
		'''

		return len(self.card_list)

	def get_card_list(self):
		return self.card_list

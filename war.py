#/usr/bin/env python3

'''
Main script to run a simulation of a game set-up

This script defines a Player -- and plays a game of War.
'''

from class_defs import StdCard as Card
from class_defs import StdDeck as Deck
from class_defs import std_card_parser as card_parser
import argparse
import numpy as np

class Player:
	'''
	Class to hold 1 Players library & discard pile.
		Discard -- initially an empty deck
		library -- initially a split of a 52-card deck

	This is a class to manipulate the results of the game.
	'''
	def __init__(self, library, discard, name):
		self.library=library #Player deck -- class Deck
		self.discard=discard #Player discard pile -- class Deck
		self.name=name #Player name

	def add2Library(self,card):
		self.library.add(card)

	def add2Discard(self,card):
		self.discard.add(card)

	def draw(self):
		'''
		Function to draw a card from the library.
			Checks if library is empty, and if it is,
			will shuffle the discard into the library before drawing.
		'''
		if self.decksize() == 0:
			self.combine_discard_library()
		return self.library.draw()

	def combine_discard_library(self):
		for card in self.discard.get_card_list():
			self.library.add(card)
		self.library.shuffle()
		self.discard=Deck()

	def decksize(self):
		return self.library.size()

	def discsize(self):
		return self.discard.size()

	def getName(self):
		return self.name

	def __str__(self):
		print(self.getName())
		print('--library: ',self.decksize(),'--')
		print(self.library)
		print('--discard: ',self.discsize(),'--')
		print(self.discard)
		print('--------------------------------')
		return ''


def parse_args(argv=None):
	parser=argparse.ArgumentParser(description='Play a game of WAR between two named players.')
	parser.add_argument('-n','--num_to_play',type=int,help='Number of games to play. Defaults to 1',default=1)
	parser.add_argument('-d','--deckfile',help='File to store card information. Defaults to decklist.txt',default='decklist.txt')
	parser.add_argument('--p1name',help='Name for Player 1. Defaults to Alice.',default='Alice')
	parser.add_argument('--p2name',help='Name for Plauer 2. Defaults to Bob.',default='Bob')
	parser.add_argument('-s','--stats', action='store_true',help='Flag to track stats of the game (mean # hands, percent to win).',default=False)
	args=parser.parse_args(argv)
	return args


def play_hand(p1, p2):
	'''
	Function that takes in 2 players & determines a hand of war

	i) Each player will draw a card into the "field".
	ii) Compare the drawn cards to determine who wins the hand.
	iii) if war -- draw an extra card into field, then go to i)
		else: add field to discard of winning player.
	'''
	field=Deck()
	unresolved=True
	while unresolved:
		#first get the cards.
		#we need to draw a card from each pile
		#first, check if player can draw a card
		if p1.decksize() > 0:
			p1_card=p1.draw()
		else:
			p1.combine_discard_library()
			p1_card=p1.draw()
		print(p1.getName(),'plays',p1_card)

		if p2.decksize() > 0:
			p2_card=p2.draw()
		else:
			p2.combine_discard_library()
			p2_card=p2.draw()
		print(p2.getName(),'plays',p2_card)

		#add the cards drawn to the field.
		field.add(p1_card)
		field.add(p2_card)
		#print(field)
		#check if there is a winner
		if p1_card.get_comparison() > p2_card.get_comparison():
			#p1 wins
			print(p1.getName(),'wins the hand and obtains:')
			for card in field.get_card_list():
				p1.add2Discard(card)
			unresolved=False
		elif p2_card.get_comparison() > p1_card.get_comparison():
			print(p2.getName(),'wins the hand and obtains:')
			for card in field.get_card_list():
				p2.add2Discard(card)
			unresolved=False
		else:
			print('WAR!')
			#add a second card to field
			# only iff a second card is possible
			if p1.decksize()+p1.discsize()>2:
				field.add(p1.draw())

			if p2.decksize()+p2.discsize()>2:
				field.add(p2.draw())

			if p1.decksize()+p1.discsize()==0:
				print(p1.getName(),'has no cards to wager!')
				print(p2.getName(),'wins the hand and obtains:')
				for card in field.get_card_list():
					p2.add2Discard(card)
				unresolved=False
			elif p2.decksize()+p2.discsize()==0:
				print(p2.getName(),'has no cards to wager!')
				print(p1.getName(),'wins the hand and obtains:')
				for card in field.get_card_list():
					p1.add2Discard(card)
				unresolved=False

	print(field)

def divvy_up(master_deck, player1, player2):
	#dividing up the cards
	counter=0
	while master_library.size() >0:
		if counter%2 == 0:
			p1.add2Library(master_library.draw())
		else:
			p2.add2Library(master_library.draw())
		counter+=1

if __name__=='__main__':
	args=parse_args()

	#making the initial decklist -- standard 52 card deck
	with open(args.deckfile,'w') as outfile:
		for suit in ['Diamonds','Hearts','Clubs','Spades']:
			for val in ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']:
				outfile.write(suit+' '+val+'\n')
	
	hand_count_list=[]
	p1_wins=0
	p2_wins=0
	for game in range(args.num_to_play):
		#initialize players & master deck
		master_library=Deck(args.deckfile)
		p1=Player(Deck(),Deck(),args.p1name)
		p2=Player(Deck(),Deck(),args.p2name)
		divvy_up(master_library, p1, p2)
		print(p1.decksize(),p1.discsize(),p2.decksize(),p2.discsize())
		counter=0
		winner=False
		while winner==False:
			counter+=1
			print('Hand:',counter)
			play_hand(p1,p2)
			if p1.decksize()+p1.discsize()==0:
				print(p2.getName(),'WINS THE GAME!')
				p2_wins+=1
				winner=True
			elif p2.decksize()+p2.discsize()==0:
				print(p1.getName(),'WINS THE GAME!')
				winner=True
				p1_wins+=1
			print('--------------------------')
		hand_count_list.append(counter)

	if args.stats:
		print('Mean Number of Hands:',np.mean(hand_count_list))
		print('Std Dev Number of Hands:',np.std(hand_count_list))
		print(p1.getName(),'Stats:',p1_wins,'/',args.num_to_play,'wins')
		print(p2.getName(),'Stats:',p2_wins,'/',args.num_to_play,'wins')
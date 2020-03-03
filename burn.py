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
	args=parser.parse_args(argv)
	return args

if __name__=='__main__':
	args=parse_args()

	#testing the decklist making function
	library=Deck(args.deckfile)
	print(library)
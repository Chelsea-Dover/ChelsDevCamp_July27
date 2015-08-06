from game import Game
from deck import Deck
from card import Card
from player import Player

def run_test_deck():
	test_deck = Deck()
	print(test_deck.deal())
	print(test_deck.deal(2))


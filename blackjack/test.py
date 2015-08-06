from game import Game
from deck import Deck
from card import Card
from player import Player

def run_test_deck():
	test_deck = Deck()
	print(test_deck.deal())
	print(test_deck.deal(2))

def run_test_player():
	test_player = Player("John")
	print(test_player)

def run_test_game():
	new_game = Game()
	return new_game


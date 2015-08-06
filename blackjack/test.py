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
	players_for_test = []
	players_for_test.append(Player("John"))
	players_for_test.append(Player("Sherlock"))
	new_game.players = players_for_test
	new_game.start_game()

def run_ui():
	new_game = Game()
	players_for_test = []
	players_for_test.append(Player("John"))
	players_for_test.append(Player("Sherlock"))
	new_game.players = players_for_test
	return new_game





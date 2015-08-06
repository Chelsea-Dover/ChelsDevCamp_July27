from player import Player
from deck import Deck

class Game:

	def __init__(self):
		self.players = []
#		self.define_players()
		self.game_deck = Deck()
		self.start_game()


	def winner(self, players):
		"""
		imput = player
		prints the hight score and winning player
		"""
		pass

	def define_players(self):
		"""
		imput num_players makes players
		returns player list
		"""

	
		num_players = int(input("How many players are you playing with? "))
		if num_players >= 2 and num_players <= 5:
			for player in range(num_players):
				player_name = input("Please enter player {}'s name: ".format(player+1))
				self.players.append(Player(player_name))
		else:
			print("You need between 2-5 players")
			exit()


	def start_game(self):
		"""
		Takes a deck of cards(AKA a list of card objects) and takes a list of player objects
		"""
		for player in self.players:
			cards = self.game_deck.deal(2)
			print(cards)
		



	def turn(self, player):
		"""
		promts user for hit or stay
		"""
		pass

	# def main(self):
	# 	"""
	# 	kicks off game
	# 	loops through the players and plays game
	# 	"""

	# 	self.define_players()
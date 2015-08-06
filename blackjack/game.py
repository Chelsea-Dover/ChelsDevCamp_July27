from player import Player
from deck import Deck

class Game:

	def __init__(self):
		self.players = []
		self.define_players()
		self.game_deck = Deck()
		self.start_game()
		self.turn_control()
		self.winner()


	def winner(self):
		"""
		imput = player
		prints the hight score and winning player
		"""
		canadate = 0
		for player in self.players:
			if player.score > canadate and player.score <= 21:
				canadate = player.score
				winner = player
		# doesn't handle all players busted
		# doesn't handle a tie?
		print("Yay {} won! \(-u-)/".format(winner))

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
		self.players.append(Player("Dealer", True))

	def start_game(self):
		"""
		Takes a deck of cards(AKA a list of card objects) and takes a list of player objects
		"""
		for player in self.players:
			cards = self.game_deck.deal(2)
			if player.is_dealer:
				cards[0].is_hidden = True
			player.new_card(cards)
			#player.print_hand()
		

	def turn(self):
		"""
		promts user for hit or stay
		"""
		hit_stay = ""
		while hit_stay != "exit":
			hit_stay = input("Would you like to 'hit' or 'stay'? ").lower()
			if hit_stay == "hit" or hit_stay == "stay" or hit_stay == "exit":
				return hit_stay
			elif hit_stay != "exit":
				print("You must choose 'hit' or 'stay' or 'exit'")



	def turn_control(self):
		"""
		Player can choose between "stay", "hit" or "exit"
		"""
		
		for player in self.players:
			print("\n\n\nIt's now {}'s turn".format(player.name))
			player.print_hand()
			choice = ""
			while choice != "stay" or choice != "exit":

				if not player.is_dealer:
					choice = self.turn()
				else:
					choice = player.does_dealer_hit()

				if choice == "hit":
					card = self.game_deck.deal()
					busted = player.new_card(card)
					player.print_hand()
					if busted and not player.is_dealer and player.score > 21:
						print("CONGRATS YOU BUSTED!!!!!")
						break
					elif busted and player.score == 21:
						print("BLACKJACK!!")
						break
				elif choice == "exit":
					print("Shame on you!! ):<")
					exit()
				elif choice == "stay":
					break








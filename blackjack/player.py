class Player:

	def __init__(self, name, is_dealer=False):
		self.hand = []
		self.name = name
		self.is_dealer = is_dealer


	def __repr__(self):
		return str(self.name)

	def score(self):
		"""
		keeps track player score
		returns total points
		"""

		pass
		

	def hit_stay(self):
		"""
		Todo place holder for AI bot
		"""
		pass

	def ace_high_low(self, card):
		"""
		Sets card to low
		imput ace to change
		"""
		pass

	def new_card(self, new_card):
		"""
		Adds new card to hand
		imput new card
		return hand
		"""
		self.hand.append(new_card)
		return self.hand

#	def print_hand(self):
#		"""
#		Prints players hand
#		"""
#		pass
























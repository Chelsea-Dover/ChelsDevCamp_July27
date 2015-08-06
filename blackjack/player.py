class Player:

	def __init__(self, name, is_dealer=False):
		#self.hand = hand
		self.name = name
		self.is_dealer = is_dealer

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

	def new_card(self, new_card):
		"""
		Adds new card to hand
		imput new card
		return hand
		"""
		pass

	def print_hand(self):
		"""
		Prints players hand
		"""
		pass

	def __repr__(self):
		return self.name























from card import Card

class Player:

	def __init__(self, name, is_dealer=False):
		self.hand = []
		self.name = name
		self.is_dealer = is_dealer
		self.score = 0

	def calculate_score(self, cards):
		"""
		keeps track player score
		returns total points
		"""
		for card in cards:
			self.score += card.real_value
		if self.score >= 21:
			return True
		else:
			return False
		

	def hit_stay(self):
		"""
		Todo place holder for AI bot
		"""
		pass

	def new_card(self, new_cards):
		"""
		Adds new card to hand
		imput new card
		return hand
		"""
		self.hand += new_cards
		return self.calculate_score(new_cards)

	def print_hand(self):
		"""
		Prints players hand
		"""
		print("Your hand and your total score is {}:\n".format(self.score))
		for card in self.hand:
			print("\t - {}".format(card), sep="\n")

	def __repr__(self):
		return self.name























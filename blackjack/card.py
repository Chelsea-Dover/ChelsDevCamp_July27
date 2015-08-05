class Card:
	"""
	Class of cards
	"""

	def __init__(self, face_value, suit, color):
		self.face_value = face_value
#		self.real_value = real_value
		self.suit = suit
		self.color = color

	def cheat(self, face_value):
		"""
		TODO cheats and changes value.
		"""
		pass

	def face_up(self):
		"""
		returns True cards is face up
		"""

	def print_card(self):
		"""
		pretty prints the card.
		"""
		pass
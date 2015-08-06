class Card:
	"""
	Class of cards
	"""

	def __init__(self, face_value, suit, color, is_hidden=True):
		self.face_value = face_value
		#self.real_value = real_value
		self.suit = suit
		self.color = color
		self.is_hidden = is_hidden

	def __repr__(self):
		if self.is_hidden:
			pretty_card = "This card is hidden"
		else:
			pretty_card = str(self.face_value) + " of " + str(self.suit)
		return pretty_card


	def cheat(self, face_value):
		"""
		TODO cheats and changes value.
		"""
		pass

	def _real_value(self):
		pass

from itertools import product
from card import Card
from random import shuffle

class Deck:
	"""
	Class for handling a deck of cards.
	
	"""

	def __init__(self, num_decks=4, face_cards=[], special_suit_values=[]):
		self.num_decks = num_decks
		self.cards_in_deck = self._build_deck(face_cards, special_suit_values)

		# self._build_deck()


	def deal(self, num_cards=1):
		"""
		input: num_cards
		returns: list of card(s)
		"""

		if num_cards > 0 and num_cards <= 2:
			cards_dealt = []
			for i in range(num_cards):
				cards_dealt.append(self.cards_in_deck[i])
			return cards_dealt
		else:
			return "You must ask for one or two cards only. "

	def _build_deck(self, face_cards=[], special_suit_values=[]):
		"""
		input: calls rand.shuffle on cards
		returns: a list of cards
		"""
		self.num_decks
		face_values = ["Two", 
					   "Three",
					   "Four",
				  	   "Five",
					   "Six",
					   "Seven",
					   "Eight",
					   "Nine",
					   "Ten"]

		suit_values = []

		#there'll be no error comment if they passed an incorrect num of list
		#Untested
		final_deck = []
		if len(special_suit_values) == 4:
			suit_values += special_suit_values
		else:
			suit_values += ["Clubs", "Hearts", "Spades", "Diamonds"]
		#Let's people custumize their decks
		if len(face_cards) == 4:
			face_values += face_cards
		else:
			ace_cards = ["Jack",
						 "Queen",
						 "King",
						 "Ace"]
			face_values += face_cards 

		for deck in range(self.num_decks):
			# Builds a single deck based on face_values and suit_values
			for card in product(face_values, suit_values):
				suit_value, face_value = card
				color = ""
				if suit_value == "Hearts" or suit_value == "Diamonds":
					color == "Red"
				else:
					color == "Black"
				final_deck.append(Card(face_value, suit_value, face_cards))
				
		shuffle(final_deck)
		return final_deck











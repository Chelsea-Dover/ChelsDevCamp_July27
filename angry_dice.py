
class Angry_dice:

	def __init__(self):

		pass

	def main(self):
		start.lower = input("Hello! Welcome to Angry Dice! type 'start' to start: ")

		if start.lower == "start":
			print_fun()


	def calculate_score(self):
		pass

	def  no_cheat(self):
		pass

	def print_fun(self):
		die = ""
		for x in die.keys():
			die += x + ""

		print("you have " + die)

		next_move.lower = input("what dice would you like to roll? If you want to quit write 'Quit' and press enter: ")

		if nexy_move.lower in die:
			die[next_move]()
		elif next_move != "Quit":
			exit()


			

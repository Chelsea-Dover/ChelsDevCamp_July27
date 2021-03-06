#This is a program that works as a dice
from random import randint 
def roll(max):
	r = randint(1, max)
	return(r)

def roll_a_bunch(max, numOfDice=4):
	rolls = []
	for i in range(numOfDice):
		rolls.append(roll(max))

	return rolls

def roll_distribution(max, numOfDice=4):

	distribution = {}
	#distribution[<key>] = <value>
	
	rolls = roll_a_bunch(max, numOfDice)
	#Count what's rolled
	for each in rolls:
		currentCount = distribution.get(each, 0)
		print("Current count of", each, ":", currentCount)
		currentCount += 1
		distribution[each] = currentCount

	output = ""
	for roll in distribution:
		output += "Number" + str(roll) + " was rolled " + str(distribution[roll]) + "times\n"

	print(output)
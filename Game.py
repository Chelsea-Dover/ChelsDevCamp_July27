def start():
	#Start Discription
#	print("Welcom to the A-maz")
	#Calling the first room
	currentRoom = room0()


def proces_user_movement(description, doors):

	#Making a string of whatever the doors names are
	doorsname = ""
	# Puts key in dict into string
	for x in doors.keys():	
		doorsname += x + " "
	#Printing The discription + the exits are and the exits names
	print(description, "The exits are " + doorsname)
	#prints and lets you choose where to move
	move = input("What direction do you want to go? If you want to quit write 'Quit' and press enter: ")
	#making it either loop or quit
	if move.lower() in doors:
		return doors[move.lower()]()
	elif move.lower() != "quit":
		return exit
	#Calls funtion
		proces_user_movement(description, doors)



def room0():
	#This variable defines the description of the room
	description = """You wake up in your dorm ready for your first day at Hogwarts! 
	You look around for your map of the school but OH NO! It seams that you've lost it!
	 You guess you'll just have to go around the school and hope for the best."""
	#This is the dict that holds the direction of the room and where to go
	doors = {"north":room2, "west":room1}
	#Calling funtion
	return proces_user_movement(description, doors)


def room00():
	#This variable defines the description of the room
	description = """You're in your dorm."""
	#This is the dict that holds the direction of the room and where to go
	doors = {"north":room2, "west":room1}
	#Calling funtion
	return proces_user_movement(description, doors)



def room1():

	description = "It looks like the room you enterd is a clost! There's nothing in here but clothes."

	doors = {"east":room00, "east":room00}

	return proces_user_movement(description, doors)



def room2():

	description = "You go into the schools hall. It's full of kids rushing to and from class. There's a few promising looking doors in here!"

	doors = {"south":room00, "west":room3, "north":room4}

	return proces_user_movement(description, doors)



def room3():

	description = "You walk into a Divination! The lecture sounds intresting but sadly this isnt a class for first years."

	doors = {"east":room2}

	return proces_user_movement(description, doors)



def room4():

	description = "You walk into another part of the hallway. There's more doors to go though over here."

	doors = {"east":room5, "south":room2, "south":room6}

	return proces_user_movement(description, doors)



def room5():

	description = "You've found your class!! You quickly go over to sit with your friends right before the bell rings"

	doors = {"start over":room0}

	return proces_user_movement(description, doors)


def room6():

	description = "You walk right outside Hogwarts into the ccourtyard! You don't think your class is going to be out here."

	doors = {"east":room4}

	return proces_user_movement(description, doors)

#def cla1():
#	description = "Today in class you're lerning how to duel for the first time! Try to win againt your enemy Mraco Dalfoy!"

#	from random import randint 

#WHAT I WANT TO HAPPEN: You and your en start off with 100 HP 
#I want there to be a list of spells and every time you pick a spell it rolls two random numbers.
# It prints he take's x amount of damage and you take y amount of damage. When you get to zero. It will say you lose. If your 



start()




#def room1():
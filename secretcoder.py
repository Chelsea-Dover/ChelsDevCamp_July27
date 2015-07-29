#Ask for imput and put that imput into a funtion
#Encoder will look up the letter?(Maybe word?) in a dict and put out the matching thing in a file(???????)
#h



#Take secret.txt and convert to a string. 
import random
def main(message = None):
	if message == None:
		message = input("What do you want to write? ")

	transformin = transform(message)

	makesecret(transformin)

def transform(message):

	mystring = ""

	for letter in message:
		mystring += random.randint + str(ord(letter)) + " " + random.randint

	return mystring

def makesecret(secret):


	with open('secret.txt', 'w') as f:
		f.write(secret)



import random

# making a user
class User:
	# variables:
	# self = self
	# self.user_name = username of the User
	# self.password = password of the User
	# self.connections = connections of the User (starts off empty)
	# connection_id = id of a User connection

    # constructor method
    def __init__ (self, user_name, password):
    	self.user_name = user_name
    	self.password = password
    	self.connections = []

    # other methods
    # user finds their username
    def getUserName(self):
    	return self.user_name

    def getPassword(self):
    	return self.password

    # user finds their connections
    def getConnections(self):
    	return self.connections

    # user adds a connection
    def addConnection(self, connection_id):
    	self.connections.append(connection_id)
    	print(self.user_name + "**Added " + connection_id.getUserName() + "**")

    # user removes a connection!!1!1!11!
    # ditch that hoe!!
    def removeConnection (self, connection_id):
    	self.connections.remove(connection_id)
    	print("**Removed " + connection_id.getUserName() + "**")

    # the one who responds uses this method
    def message (self):
    	responses = ["I'm hungry. Are you?", "Pika pika!", "Have you seen the DNA Pokemon yet? It's pretty cool.", 
    	"Always watching", "No eyes.", "Go to sleep", "Yare yare daze.", "Yare yare daza.", "He is the Rake.", "*blinks*", 
    	"We should grab lunch together sometimes.", "go to SLEEP it's too early", ". . .", "but that's none of my business",
    	"I got power, poison, pain and joy inside my DNA\nI got hustle though, ambition, flow, inside my DNA"]
    	return random.choice(responses)

# network of users who are connected to a certain user!!!!!!
class Network:
	# variables:
	# self.user = list of users

	# constructor method
	def __init__ (self):
		self.user = []

	def addUser(self, username, password):
    	# create new user with given username and password
		# append that user in the list of total people
		myUser = User(username, password)
		self.user.append(myUser)
		print("**Made " + username + "**")

	def removeUser(self, myUser):
		self.user.remove(self)
		print("**Removed user**")

# running the code
def tutorial():
	# makes your user
	# starter
	user_input = input("\nLet's make a new user! Press 'n' to make a new user! ")
	shortcuts_tutorial('n', user_input)
	username = input('What is your username? ')
	password = input("What is your password? ")
	user1 = User(username, password)
	print('Congrats! Your username is ' + username + ' and your password is ' + password + '.')
	network = Network()
	network.addUser(username, password)

	# makes felicia
	print("\nLet's make another new user for our friend, Felicia! But first we have to log out.")
	user_input = input("Press 'o' to log out: ")
	shortcuts_tutorial('o', user_input)

	user_input = input("\nNow let's make a Felicia an account. Press 'n' to make a new user: ")
	shortcuts_tutorial('n', user_input)

	username = input('What is her username? ')
	password = input("What is her password? ")
	user2 = User(username, password)
	print("Congrats! Felicia's username is " + username + " and her password is " + password + '.')
	network.addUser(username, password)

	# logging in
	print("\nLet's log into our old account, " + user1.getUserName() + ".")
	user_input = input("First, we have to log out. Press 'o' to log out: ")
	shortcuts_tutorial('o', user_input)

	user_input = input("Let's log in! Press 'l' to log in: ")
	shortcuts_tutorial('l', user_input)

	user_input = input("What is your password? ")
	while (user_input != user1.getPassword()):
		user_input = input("Try again: ")
	print("Good job! You remembered your password!")

	# connection
	print("\nHey! Why don't we make a connection!")
	user_input = input("Would you like to add " + user2.getUserName() + "? Type 'yes' or 'no': ")
	if (user_input == 'yes'):
		user1.addConnection(user2)
		user2.addConnection(user1)
		print("\nCongrats! We added " + user2.getUserName() + ".")
	elif (user_input == 'no'):
		print("\nToo bad, we're adding her.")

	# messaging
	print("\nLet's message " + user2.getUserName() + "!")
	user_input = input("Say something to Felicia!\n" + user1.getUserName() + ": ")
	print(user2.getUserName() + ": " + user2.message())
	print("\nThat's not very nice! Let's remove Felicia from our connections.")
	user1.removeConnection(user2)
	user2.removeConnection(user1)

	# end
	print('''
		That's the end of the tutorial! You learned a lot, right? 
		The users and connections you made in this tutorial will 
		not continue to exist. Thanks for going through this!''')
	network.removeUser(user1)
	network.removeUser(user2)

def shortcuts_tutorial(key, user_input):
	tf = True
	cp_message = ''
	message = ''
	if (key == 'l'):
		cp_message = '**Logging in**'
		message = "Press 'l' to log in: "
	elif (key == 'o'):
		cp_message = '**Logging out**'
		message = "Press 'o' to log out: "
	elif (key == 'n'):
		cp_message = "**Making new account**"
		message = "Press 'n' to make a new user: "

	while(tf):
		if(user_input == key):
			print(cp_message)
			tf = False
		else:
			user_input = input(message)

def main():

	main_screen = input('''
	Press 't' to go through the tutorial.
	Press 'n' to make a new user.
	Press 'l' to login in.
	Press 'o' to log out.\n\n''')

	if(main_screen == 't'):
		tutorial()

# Runs your program.
if __name__ == '__main__':
    main()

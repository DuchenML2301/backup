# Mackenzie Duchen
# Rock Paper Scissors
#added a comment
#VARIABLES
import random

pScore = 0
cScore = 0
ties = 0
computerChoices = ["r", "p", "s"]

# Welcome Message
# print message 
print("Welcome to Rock Paper scissors")
# prompt for player name
pName = input("What is Your Name? ")

# Finall Score
def printScore():
	#Write message
	print("The Score is: ")
	#Write player score
	print(pName + ":" + str(pScore))
	# WRITE COMPUTER SCORE
	print("Computer: " + str(cScore))
	# write how many ties
	print("Ties: " + str(ties))
# Game Loop
# make a forever loop
while True:
	#print the score
	printScore()
	# prompt for a choice r= rock p=paper s=scissors q=quit
	pChoice = input("Enter r (Rock), p (paper), s(scissors), or q (to quit): ")
	# deal with player entering q
	if pChoice == "q":
		break
	# get comoputers choice (random)
	cChoice = random.choice(computerChoices)
	# compaire for player entering r
	if pChoice == "r":
		print(pName +" Picked Rock")
		# if computer is r
		if cChoice == "r":
			print("Computer picked Rock")
			print("This is a tie")
			ties = ties + 1
		# if computer is p
	    elif cChoice == "p":
	    	print("Computer picked paper")
	    	print("Paper covers rock")
	    	cScore = cScore + 1
		# if computer is s
		else:
			print("Computer picked scissors")
			print("Rock breaks scissors")
			pScore = pScore + 1
	#compaire for player entering s
	elif pChoice == "s":
		print(pName +" Picked Rock")
		# if computer is r
		if cChoice == "r":
			print("Computer picked Rock")
			print("rock crushes scissors ")
			cScore = cScore + 1
		# if computer is p
	    elif cChoice == "p":
	    	print("Computer picked paper")
	    	print("siccors breaks/ cuts paper")
	    	pScore = pScore + 1
		# if computer is s
		else:
			print("Computer picked scissors")
			print("This is a tie")
			ties = ties + 1
	#compaire for player entering p
	elif pChoice == "p":
		print(pName +" Picked Rock")
		# if computer is r
		if cChoice == "r":
			print("Computer picked Rock")
			print("paper covers rock")
			pScore = pScore + 1
		# if computer is p
	    elif cChoice == "p":
	    	print("Computer picked paper")
	    	print("This is a tie")
	    	ties = ties + 1
		# if computer is s
		else:
			print("Computer picked scissors")
			print("scissors cuts paper")
			cScore = cScore + 1
	# deal with player entering something else
elif pChoice == "random":
	print("Listen to directions")
print("Have a nice day!")
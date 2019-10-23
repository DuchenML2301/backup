# conditional
print("Welcome to Movie bot")
age =int(input("How Old Are You?"))
if age > 17:
	print("You Can See an R rated Movie")
else:
	print("You Can NOT see an R rated movie")

print("Have a great day")

myNumber = 4
choice = int(input("Pick a number between 1 and 10:"))
if myNumber == choice:
	print("You Guessed it")
elif choice < myNumber:
	print("Too Low")
else:
	print("Too High")

# == (equal to), <, >, <=, >=, (not equal too)

bday= input("is today your birthday: (yes/ no):")
if bday == "yes":
	print("happy birthday")
elif (bday == "no"):
	print("Have a nice day anyway")
else:
	print("Learn how to read directions")
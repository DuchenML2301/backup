# Mackenzie Duchen
#period 4

#Variable decloration and assignment
#Examples
myNum = 12 # integer type
myString = "12" # string type
myNum + 3
print(myString + "3") # not okay

#make a variable and assign it the value of your favorite movie
# then print my favorite movie is followed by the variable

variable = "ponyo"
print("my favoriite movie is:" + variable)

x =1
while x <=10:
	print(x)
	x = x + 1

#count down from 100 using a while loop
x = 100
while (x >=100):
	print(x)
	x = x - 1
	break
	
# string concatenation 
#means putting two strings together
myName = "Mackenzie"
print("Hello," + myName)
 #imput
#example
yourName = input("What is your name?:")
print("Hello," + yourName + ",have a nice day")


#number = input("Enter number")
#number = int(number) + 10
#print("The Number is" + str(number))
# ask for two numbers, add them and print the sum

number = input("Enter number:")
numbers = input("Enter number:")
number = int(number) + int(numbers)
print("The Number is" + str(number))

# if / else statements 
#example
num = int(input("Enter a number: "))
if num > 100:
	print("Your number is more than a 100")
elif num == 100:
	print("Your number is equal to 100")
else:
	print("Your number is less than 100")

#ask if today is your birtyhday
bir = input("Is today your birthday? ")
if bir == "yes":
	print("Happy Birthday")
elif bir == "no":
	print("aw")
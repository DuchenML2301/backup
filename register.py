import time
import os
import randomimport time
import os
import random

particular = input("Enter the total of the particular item you have: ")

print("The particular item is: " + str(particular))

buck = input("How much money would you like to pay with?:")

thecents = 0
thecents = float(particular) * 100
pencen = 0
together = 0
dimesprinted = 0
printingthecents = 0
dimesprintedses  = 0
printthenickels = 0
printpenn = 0
printhalfs = 0

print("You have paid:" + str(buck))

pencen += int(buck) * int(100)





finalbucks = pencen - thecents
together = finalbucks / 100



print("You got:" + str(together) + " back.")
print("")

while finalbucks > 100:
	dimesprinted += 1
	finalbucks -= 100
print("You got " + str(dimesprinted) + " dollar bills.")
print("")

while finalbucks > 50:
	printhalfs +=1
	finalbucks -= 50
print("You got " + str(printhalfs) + " half buck.")
print("")


while finalbucks > 25:
	printingthecents += 1
	finalbucks -= 25
print("You got " + str(printingthecents) + " quarters.")
print("")


if finalbucks < 25:
	while finalbucks > 10:
		dimesprintedses  += 1
		finalbucks -=10
	print("You got " + str(dimesprintedses ) + " dimes.")
	print("")

	while finalbucks > 5:
		printthenickels += 1
		finalbucks -=5
	print("You got " + str(printthenickels) + " nickels.")
	print("")

	while finalbucks > 0:
		printpenn += 1
		finalbucks -=1
	print("You got " + str(printpenn) + " pennies.")
	print("")




particular = input("Enter the cost of the particular item: ")

print("The particular item is:" + str(particular))

buck = input("How much money would you like to pay with?:")

thecents = 0
thecents = float(particular) * 100
pencen = 0
together = 0
dimesprinted = 0
printingthecents = 0
dimesprintedses  = 0
printthenickels = 0
printpenn = 0
printhalfs = 0

print("You paid:" + str(buck))

pencen += int(buck) * int(100)



 

finalbucks = pencen - thecents
together = finalbucks / 100


print("You got:" + str(together) + " back.")
print("")

while finalbucks > 100:
	dimesprinted += 1
	finalbucks -= 100
print("You got " + str(dimesprinted) + " dollar bills.")
print("")

while finalbucks > 50:
	printhalfs +=1
	finalbucks -= 50
print("You got " + str(printhalfs) + " half buck.")
print("")


while finalbucks > 25:
	printingthecents += 1
	finalbucks -= 25
print("You got " + str(printingthecents) + " quarters.")
print("")


if finalbucks < 25:
	while finalbucks > 10:
		dimesprintedses  += 1
		finalbucks -=10
	print("You got " + str(dimesprintedses ) + " dimes.")
	print("")

	while finalbucks > 5:
		printthenickels += 1
		finalbucks -=5
	print("You got " + str(printthenickels) + " nickels.")
	print("")

	while finalbucks > 0:
		printpenn += 1
		finalbucks -=1
	print("You got " + str(printpenn) + " pennies.")
	print("")

#the end

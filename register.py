import time
import os
import randomimport time
import os
import random

item = input("Enter the cost of the item: ")

print("The item is $ " + str(item))

dollars = input("Enter the number of dollars you will pay:")

icents = 0
icents = float(item) * 100
pcents = 0
total = 0
finalprintd = 0
finalprintc = 0
finalprintdim = 0
finalprintn = 0
finalprintp = 0
finalprinth = 0

print("You payed $" + str(dollars))

pcents += int(dollars) * int(100)

#rint(icents)

#rint(pcents)  

finalc = pcents - icents

#rint(finalc)

total = finalc / 100

#rint(finald)

print("You got $" + str(total) + " back.")
print("")

while finalc > 100:
	finalprintd += 1
	finalc -= 100
print("You got " + str(finalprintd) + " dollar bills.")
print("")

while finalc > 50:
	finalprinth +=1
	finalc -= 50
print("You got " + str(finalprinth) + " half dollars.")
print("")


while finalc > 25:
	finalprintc += 1
	finalc -= 25
print("You got " + str(finalprintc) + " quarters.")
print("")


if finalc < 25:
	while finalc > 10:
		finalprintdim += 1
		finalc -=10
	print("You got " + str(finalprintdim) + " dimes.")
	print("")

	while finalc > 5:
		finalprintn += 1
		finalc -=5
	print("You got " + str(finalprintn) + " nickels.")
	print("")

	while finalc > 0:
		finalprintp += 1
		finalc -=1
	print("You got " + str(finalprintp) + " pennies.")
	print("")




item = input("Enter the cost of the item: ")

print("The item is $ " + str(item))

dollars = input("Enter the number of dollars you will pay:")

icents = 0
icents = float(item) * 100
pcents = 0
total = 0
finalprintd = 0
finalprintc = 0
finalprintdim = 0
finalprintn = 0
finalprintp = 0
finalprinth = 0

print("You payed $" + str(dollars))

pcents += int(dollars) * int(100)

#rint(icents)

#rint(pcents)  

finalc = pcents - icents

#rint(finalc)

total = finalc / 100

#rint(finald)

print("You got $" + str(total) + " back.")
print("")

while finalc > 100:
	finalprintd += 1
	finalc -= 100
print("You got " + str(finalprintd) + " dollar bills.")
print("")

while finalc > 50:
	finalprinth +=1
	finalc -= 50
print("You got " + str(finalprinth) + " half dollars.")
print("")


while finalc > 25:
	finalprintc += 1
	finalc -= 25
print("You got " + str(finalprintc) + " quarters.")
print("")


if finalc < 25:
	while finalc > 10:
		finalprintdim += 1
		finalc -=10
	print("You got " + str(finalprintdim) + " dimes.")
	print("")

	while finalc > 5:
		finalprintn += 1
		finalc -=5
	print("You got " + str(finalprintn) + " nickels.")
	print("")

	while finalc > 0:
		finalprintp += 1
		finalc -=1
	print("You got " + str(finalprintp) + " pennies.")
	print("")

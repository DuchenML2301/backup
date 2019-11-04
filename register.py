
pennys = 0
nickels = 0
dimes = 0
quarters = 0
half = 0
ones = 0

price = int(input("What is the price of the item?: "))
amount = int(input("How much was given?: "))

change = amount - price
print("Change:", (change))

pennys += nickels * 5
nickels += dimes * 2
dimes += quarters * 2.5
quarters += half * 2
half += ones * 2

pennys = 0
nickels = 0
dimes = 0
quarters = 0
half = 0
ones = 0
while ones >= change:
	pennys = 0
	nickels = 0
	dimes = 0
	quarters = 0
	half = 0
	ones = 0
	
	ones = int(half / 2)
	half = half % 2
	half = int(quarters / 2)
	quarters = quarters % 2
	quarters = int(dimes / 2.5)
	dimes = dimes % 2.5
	dimes = int(nickels / 2)
	nickels = nickels % 2
	nickels = int(pennys / 5)
	pennys = pennys % 5

	print(str(ones) + "ones")
	print(str(half) + "half")
	print(str(quarters) + "quarters")
	print(str(dimes) + "dimes") 
	print(str(nickels) + "nickels")
	print(str(pennys) + "pennys")

	pennys += nickels * 5
	nickels += dimes * 2
	dimes += quarters * 2.5
	quarters += half * 2
	half += ones * 2
print(ones)
for num in range(1, 101):
	if num % 3 == 0:
		print("Fizz", end="")
		print(num)
	if num % 5 == 0:
		print("Buzz", end="")
		print(num)
	if (num % 5 == 0 or num % 3 == 0):
		print("fizz", end="")
		print("buzz", end="")
		print(num)
	else:
		print(num)
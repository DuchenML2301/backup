print("Welcome to the To Do List")
todolist = []
while True:
	print("Enter a to add an iteam")
	print("Enter r to remove an item")
	print("Enter p to print the list")
	print("Enter q to quit ")

	choice = input("Make your choice: ")
	if choice == "q":
		break
	elif choice == "a":
		Add = input("what would you like to add? ")
		todolist.append(Add)
		print("todolist")
		# add an item to the list
		# take this out
	elif choice == "r":
		remove= input("what would you like to remove? ")
		todolist.remove(remove)
		print("todolist")
	elif choice == "p":
		print("todolist: " + str(len(todolist)) + " items")
		print(todolist)
		print(todolist[len(todolist)- 1])
		# print the list
	else:
		print("That is not a choice")

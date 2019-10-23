#how to make a list
favMovies = ["Star wars", "ponyo", "your name"]
#print the wole list
print(favMovies)
#print individualls
print(favMovies[0])
# to add you can use append or insert
# append adds to the end
favMovies.append("Kill Bill")
print(favMovies)
#insert will put iteam whereever you want 
favMovies.insert(1, "Harry potter")
print(favMovies)
#how to remove iteams
#remove by name or index
#remove my name use remove
favMovies.remove("Kill Bill")
print(favMovies)
#favMovies.remove("Endgame") this is a error
#pop will remove the last iteamunless an index is givin
favMovies.pop()
print(favMovies)
favMovies.pop(1)#would remove what ever is in the index one
print(favMovies)

# get the length of a list
#this is a function
# the function name is len
print("My list has: " + str(len(favMovies)) + "items")
favMovie = input("What is your favorite movie?")
favMovies.append(favMovie)
print(favMovies)
print(favMovies[len(favMovies)- 1])

# loop through a list
count = 1

for movie in favMovies:
	print("My Number " + str(count) + "movie is " + movie)
	count = count + 1

numList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# challenge: loop throuugh the list add numbers together then print

total = 0
for numbers in numList:
	total = total + numbers

print("The sum is" + str(total))

if "Star wars" in favMovies:
	favMovies.remove("Star wars")
	print("Removed")
else:
	print("Not on list")
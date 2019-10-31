import time
import os
frameList = [''' 
 
     +---+
     0   |
         |
         |
         === ''', '''
      +---+
      0   |
      |   |
          |
          === ''', '''
      +---+
      0   |
      |   |
       \  |
          === ''', '''
      +---+ 
      0   |
      |   |
     / \  |
           === ''', '''
      +---+ 
      0   |
      |\  |
     / \  |
         === ''', '''
      +---+
      0   |
     /|\  |
     / \  |
         === ''' ]

while True:
	for frame in frameList:
		os.system("cls")
		print(frame)
		time.sleep(.3)
num = 0 
While num <=100:
Print(num)
num = num + 1
if num % 3 + num % 5 == 0:
Print("FizzBuzz", end="")
elif num % 3 == 0:
Print("Fizz", end="")
elif num % 5 == 0:
Print("Buzz", end"")

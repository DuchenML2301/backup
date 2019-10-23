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
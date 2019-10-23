from turtle import *
myTurtle = Turtle()
screen = myTurtle.getscreen()
myTurtle.forward(20)

def writeName():
	name = screen.textinput("name box", "what is your name?")
	myTurtle.write(name, move=True, align="left", font=("Arial",38,"normal"))
	screen.listen()

screen.onkey(writeName, "w")

screen.listen()
screen.mainloop()
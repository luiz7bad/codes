import turtle
#the import abvove moves and draw lines

def drawSquare():
	#captures a screen to draw on it
	window = turtle.Screen()
	window.bgcolor('red')

	#captures the turtle, or cursor to start to draw
	brad = turtle.Turtle()
	#moves forward 100 times.
	brad.forward(100)
	#turns right 90 degrees
	brad.right(90)
	brad.forward(100)
	brad.right(90)
	brad.forward(100)
	brad.right(90)
	brad.forward(100)
	brad.right(90)

	#closes the window when clicked on
	window.exitonclick()

drawSquare()
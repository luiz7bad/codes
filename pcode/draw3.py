import turtle
#the import abvove moves and draw lines
def drawSquare():
	#captures the turtle, or cursor to start to draw
	brad = turtle.Turtle()
	for i in range(4):
		#moves forward 100 times.
		brad.forward(100)
		#turns right 90 degrees
		brad.right(90)
	
	
def drawCircle():
	angie = turtle.Turtle()
	angie.shape('turtle')
	angie.color('blue')
	angie.circle(100)

def drawTriangle():
	theo = turtle.Turtle()
	theo.color('yellow')
	for i in range(3):
		theo.right(120)
		theo.forward(80)
	

def draw():
	#captures a screen to draw on it
	window = turtle.Screen()
	window.bgcolor('red')
	drawSquare()
	drawCircle()
	drawTriangle()
	#closes the window when clicked on
	window.exitonclick()

draw()


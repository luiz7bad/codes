import turtle

brad = turtle.Turtle()
def square():
	global brad
	for i in range(4):
		brad.forward(100)
		brad.right(90)

def circleOfSquares():
	for i in range(36):
		brad.right(10)
		square()
def draw():
	window = turtle.Screen()
	window.bgcolor('blue')
	circleOfSquares()
	window.exitonclick()
draw()

import turtle

def draw_square():
	screen = turtle.Screen()
	screen.bgcolor("green")

	brad = turtle.Turtle()
	
	for angle in range(0,360):
		brad.right(angle)
		brad.forward(100)
		brad.right(90)
		brad.forward(100)
		brad.right(90)
		brad.forward(100)
		brad.right(90)
		brad.forward(100)
		brad.right(90)
	
	screen.exitonclick()
draw_square()
		

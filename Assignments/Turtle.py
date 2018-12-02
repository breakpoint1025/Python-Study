import turtle

def draw_square():
	screen = turtle.Screen()
	screen.bgcolor("black")

	brad = turtle.Turtle()
	brad.shape("arrow")
	brad.color("pink")
	brad.speed(50)
	turn_angle = 5

	for i in range(0, 360, turn_angle):		
		
		brad.forward(100)
		brad.right(90)
		brad.forward(100)
		brad.right(90)
		brad.forward(100)
		brad.right(90)
		brad.forward(100)
		brad.right(90)

		brad.right(turn_angle)
	
	screen.exitonclick()
draw_square()
		

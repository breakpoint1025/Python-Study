import turtle

def draw_square(brad):
	brad.color("pink")
	for i in range(4) :	
		brad.forward(100)
		brad.right(90)

def draw_circle(brad):
	brad.color("red")
	brad.circle(100)

def draw_triangle(brad):
	brad.color("blue")
	i = 0
	while i < 3 :	
		brad.forward(100)
		brad.right(120)
		i=i+1


def draw_square_sunflower(brad, turn_angle):
	brad.speed(50)
	for i in range(0, 360, turn_angle):
		draw_square(brad)
		brad.right(turn_angle)


def draw_circle_sunflower(brad, turn_angle):
	brad.speed(50)	
	for i in range(0, 360, turn_angle):
		draw_circle(brad)
		brad.right(turn_angle)

def draw_triangle_sunflower(brad, turn_angle):
	brad.speed(50)	
	for i in range(0, 360, turn_angle):
		draw_triangle(brad)
		brad.right(turn_angle)

if __name__ == '__main__':
	
	screen = turtle.Screen()
	screen.bgcolor("black")

	brad = turtle.Turtle()
	brad.shape("arrow")
	brad.speed(10)
	
	draw_square(brad)	
	draw_circle(brad)
	draw_triangle(brad)
	
	brad.reset()
	draw_square_sunflower(brad, 1)

	brad.reset()
	draw_circle_sunflower(brad, 1)

	brad.reset()
	draw_triangle_sunflower(brad, 1)	

	screen.exitonclick()
		

import turtle

def draw_square(brad):
	brad.color("pink")
	i = 0
	while i < 4 :	
		brad.forward(100)
		brad.right(90)
		i = i+1

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


def draw_square_sunflower(brad):	
	
	brad.speed(50)
	
	angle = 0
	turn_angle = 1

	while angle < 360:
		draw_square(brad)
		angle=angle+turn_angle
		brad.right(turn_angle)

def draw_circle_sunflower(brad):	
	
	brad.speed(50)
	
	angle = 0
	turn_angle = 1

	while angle < 360:
		draw_circle(brad)
		angle=angle+turn_angle
		brad.right(turn_angle)

def draw_triangle_sunflower(brad):	
	
	brad.speed(50)
	
	angle = 0
	turn_angle = 1

	while angle < 360:
		draw_triangle(brad)
		angle=angle+turn_angle
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
	draw_square_sunflower(brad)

	brad.reset()
	draw_circle_sunflower(brad)

	brad.reset()
	draw_triangle_sunflower(brad)	

	screen.exitonclick()
		

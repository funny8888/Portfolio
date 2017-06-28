from turtle import *
import math
import random

# Name your Turtle.
serina = Turtle()

# Set Up your screen and starting position.
penup()
speed(100000000000)
x_pos = -300
y_pos = -300
goto(x_pos, y_pos)
my_num = 30
colors = ["blue", "dark blue", "LemonChiffon", "MediumOrchid", "LightCyan", "SeaGreen", "VioletRed", "magenta", "MintCream"]

# Write your code below:
def shape_pattern(num, x_pos, y_pos):
	goto(x_pos, y_pos)
	for z in range (0,8): #making rows
		for y in range(0,7): #making columns
			for x in range(0,8): #making the shape
				pendown()
				forward(num)
				left(45)
			penup()
			pencolor(random.choice(colors))
			left(90)
			forward(80)
			right(90)
		x_pos += 80
		goto(x_pos, y_pos)

pencolor(random.choice(colors))
shape_pattern(my_num, x_pos, y_pos)
my_num += -10
x_pos += 5.5
y_pos += 12

shape_pattern(my_num, x_pos, y_pos)




# Close window on click.
exitonclick()

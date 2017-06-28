from turtle import *
import random

serina = Turtle

penup()
speed(0)
x_pos = -300
y_pos = -300
goto(x_pos, y_pos)
my_num = 30
colors = ["blue", "dark blue", "MediumOrchid", "SeaGreen", "VioletRed", "magenta"]

user_input = input()

def shape_pattern(num, x_pos, y_pos, user_input):
	goto(x_pos, y_pos)
	for z in range (0,8): #making rows
		for y in range(0,7): #making columns
			for x in range(0,user_input): #making the shape
				pendown()
				forward(num)
				right(360/int(user_input))
				penup()
			pencolor(random.choice(colors))
			left(90)
			forward(80)
			right(90)
		x_pos += 80
		goto(x_pos, y_pos)

pencolor(random.choice(colors))
shape_pattern(my_num, x_pos, y_pos, user_input)
my_num += -10
x_pos += 5.5
y_pos += 12

# import colorgram

# rgb_colors = []
# colors = colorgram.extract('hirst-painting-start\image.jpg', 30)
# for color in colors:
#     red = color.rgb.r
#     green = color.rgb.g
#     blue = color.rgb.b
#     rgb_colors.append((red, green, blue))

# print(rgb_colors)

# find the most common color in the image
# most_common_color = max(set(rgb_colors), key=rgb_colors.count)
# print(most_common_color)

from turtle import *
import random


# chosen based on the most common color in the image
color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 
123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

timmy = Turtle()
screen = Screen()

def setup_timmy():
    screen.colormode(255)
    timmy.speed("fastest")
    timmy.hideturtle()

def draw_row(t, num_columns, dot_size):
    for i in range(num_columns):
        t.dot(dot_size, random.choice(color_list))
        t.up()
        t.forward(2 * dot_size)
        t.down()

def draw_grid(t, num_rows, num_columns, dot_size):
    timmy.up()
    timmy.goto(-num_columns * dot_size, -num_rows * dot_size)
    timmy.down()
    for i in range(num_rows):
        draw_row(t, num_columns, dot_size)
        t.up()
        t.setheading(90)
        x, y = t.position()
        t.goto(x - dot_size * num_columns * 2, y + dot_size * 2)
        t.setheading(0)
        t.down()

setup_timmy()

draw_grid(timmy, 10, 10, 20)


screen.exitonclick()
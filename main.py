# Bismillahirrahmanirrahim
# import colorgram as cg
# colors = cg.extract("image.jpg", 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     next_color = (r,g,b)
#     rgb_colors.append(next_color)
#
# print(rgb_colors)
import turtle
from turtle import Turtle, Screen, colormode
import random

color_list = [(26, 108, 164), (193, 38, 81), (237, 161, 50), (234, 215, 86), (227, 237, 229), (223, 137, 176),
              (143, 108, 57), (103, 197, 219), (21, 57, 132), (205, 166, 30), (213, 74, 91), (238, 89, 49),
              (142, 208, 227), (119, 191, 139), (5, 185, 177), (106, 108, 198), (137, 29, 72), (4, 162, 86),
              (98, 51, 36), (24, 155, 210), (229, 168, 185), (173, 185, 221), (29, 90, 95), (233, 173, 162),
              (156, 212, 190), (87, 46, 33), (37, 45, 83)]

tim = Turtle()
tim.shape("circle")
colormode(255)
tim.speed("fastest")
tim.penup()
tim.setposition(-303.55, -303.55)


def set_position():
    pn = tim.position()
    tim.sety(pn[1] + 50)


# 10X10 size board
for x in range(0, 10):
    set_position()
    for y in range(0, 10):
        tim.dot(20, random.choice(color_list))
        tim.fd(50)
        
    tim.bk(50 * 10)

screen = Screen()
screen.exitonclick()

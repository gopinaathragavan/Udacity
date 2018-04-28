"""
This program has a turtle on an orange background draw a square, circle and triangle
"""

import turtle


def draw_square(turtle):
    for i in range(4):
        turtle.forward(50)
        turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("orange")
    Gopi = turtle.Turtle()
    Gopi.shape("turtle")
    Gopi.color("red")
    Gopi.speed(2)
    draw_square(Gopi)
    Shama = turtle.Turtle()
    Shama.shape("arrow")
    Shama.color("blue")
    Shama.speed(2)
    Shama.circle(100)
    Sahana = turtle.Turtle()
    Sahana.shape("turtle")
    Sahana.color("purple")
    Sahana.speed(1)
    Sahana.right(45)
    Sahana.forward(100)
    Sahana.right(90)
    Sahana.forward(100)
    Sahana.right(135)
    Sahana.forward(135)
    window.exitonclick()

draw_art()




    





"""
This program has a turtle on an orange background draw a square, circle and triangle
"""

import turtle


def draw_square(turtle):
    for i in range(4):
        turtle.forward(50)
        turtle.right(90)

def draw_triangle(turtle):
    turtle.right(45)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(135)
    turtle.forward(135)


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
    draw_triangle(Sahana)
    window.exitonclick()

def draw_fractal(square_count):
    window = turtle.Screen()
    window.bgcolor("orange")
    Gopi = turtle.Turtle()
    Gopi.shape("turtle")
    Gopi.color("red")
    Gopi.speed(2)
    for i in range(square_count):
        Gopi.right(360/square_count)
        draw_square(Gopi)
    window.exitonclick()

square_count = input("Enter number of squares for circular fractal as a positive whole number: ")   
draw_fractal(int(square_count))
#draw_art()




    





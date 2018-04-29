"""
This program has a turtle that will ask you whether you would like to see a drawing or a fractal
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

def draw_fractal():
    fractal_type = int(input("This is a fractal drawing program \n Enter a number for drawing a fractal: 1 for using a square or 2 for using a triangle"))
    shape_count = int(input("Enter number of shapes for fractal as a positive whole number: "))
    window = turtle.Screen()
    window.bgcolor("orange")
    Gopi = turtle.Turtle()
    Gopi.shape("turtle")
    Gopi.color("red")
    Gopi.speed(2) 
    for i in range(shape_count):
        if fractal_type == 1:
            Gopi.right(360/shape_count)
            draw_square(Gopi)
        elif fractal_type == 2:
            Gopi.right(360/shape_count)
            draw_triangle(Gopi)
    window.exitonclick()

   
draw_fractal()




    





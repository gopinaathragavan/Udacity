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


def draw_fractal(shape_count):
    fractal_type = int(input("This is a fractal drawing program \n Enter a number for drawing a fractal: 1 for using a square or 2 for using a triangle"))
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


def turtle_draw():
    main_menu = int(input("Would you like to see my drawing or draw a circular fractal; Enter 1 for drawing or 2 for fractal: "))
    menu = main_menu
    if menu == 1:
        draw_art()
    elif menu == 2:
        shape_count = int(input("Enter number of shapes for fractal as a positive whole number: "))
        draw_fractal(shape_count)
    elif (menu <1) or (menu >2):
        print("Try again. Enter 1 for drawing or 2 for fractal: ")
        turtle_draw()

    
turtle_draw()




    





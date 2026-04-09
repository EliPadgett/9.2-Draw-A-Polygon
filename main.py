from turtle import *

def regular_polygon(turtle, sides):
    turtle.begin_fill()
    for i in range(sides):
        turtle.forward(100/sides)
        turtle.right(360/sides)
    turtle.end_fill()

name = Turtle()
name.ht()
name.speed(0)



screen = Screen()
screen.bgcolor("Teal")

pen = Turtle()
pen.speed(0)
pen.color("White")
pen.hideturtle()

regular_polygon(pen, 3)


while True:
    sides = int(input("How many sides does your shape have? "))
    if sides == 3:
        regular_polygon(pen, sides)
        name.write("TRIANGLE", font = ("Times New Roman", 20))
    if sides == 5:
        regular_polygon(pen, sides)
        name.write("Pentagon", font = ("Times NEw Roman", 20))
    pen.clear()
    regular_polygon(pen, sides)




screen.exitonclick()
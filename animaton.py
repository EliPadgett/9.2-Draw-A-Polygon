from turtle import *
import random

def generate_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"

def create_turtle():
    new_turtle = Turtle()
    new_turtle.shape("circle")
    new_turtle.pu()
    new_turtle.speed(0)
    new_turtle.setheading( random.randint(0, 360))
    new_turtle.color(generate_color())
    
    return new_turtle

def play_area():
    pen =Turtle()
    pen.speed(0)
    pen.hideturtle()
    pen.color(generate_color())
    pen.goto(-250,250)
    pen.begin_fill()
    
    for i in range(4):
        pen.forward(500)
        pen.right(90)

        
    pen.end_fill()

def move_forward(turtle, turtles):
    turtle.forward(5)

    if turtle.xcor() > 245 or turtle.xcor() < -245:
        turtle.speed(0)
        print(turtle.heading())
        turtle.setheading(180 - turtle.heading())
        turtle.forward(10)
        turtle.speed(1)
        t = create_turtle()
        turtles.append(t)
    if turtle.ycor() > 245 or turtle.ycor() < -245:
        turtle.speed(0)
        turtle.setheading(-turtle.heading() )
        turtle.forward(10)
        turtle.speed(1)
        t = create_turtle()
        turtles.append(t)
    
    return turtles

def move_xy(turtle, deltaX, deltaY):
    newX = turtle.xcor() + deltaX
    newY = turtle.ycor() + deltaY

    if newX > 250 or newX < -250:
        deltaX *= -1
        newX = turtle.xcor()
    if newY > 250 or newY < -250:
        deltaY *= -1
        newY = turtle.ycor()

    turtle.goto(newX, newY)
    return deltaX, deltaY

screen = Screen()
screen.bgcolor("Black")
play_area()

yertle = Turtle()
yertle.color(generate_color())
yertle.shape("circle")
yertle.pu()
yertle.setheading( random.randint(0,360) )
deltaX = random.randint(-5,5)
deltaY = random.randint(-5,5)

turtles = [yertle]


while True:
    for obj in turtles:
        turtles = move_forward(obj, turtles)













screen.exitonclick()
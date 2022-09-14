import turtle
import random

turtle.penup()
turtle.setheading(270)
turtle.forward(200)
i = 6
x = 0
y = -200
turtle.pendown()
turtle.setheading(0)
while(y<400):
    turtle.goto(500,y)
    y += 100
    turtle.penup()
    turtle.goto(x,-200)
    turtle.pendown()
    turtle.goto(x,300)
    x += 100
    turtle.penup()
    turtle.goto(0,y)
    turtle.pendown()
turtle.penup()
turtle.goto(500,300)

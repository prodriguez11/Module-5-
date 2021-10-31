#Problem 5
# background color
# turtle object
# define function
# for drawing rays of Sun
# Draw circle
# to make sun
# Use the defined
# function to draw rays
# To keep the
# output window active

import turtle

screen = turtle.Screen()
screen.bgcolor("lightpink")
y = turtle.Turtle()

def drawFourRays(t, length, radius):
    for i in range(4):
        t.penup()
        t.forward(radius)
        t.pendown()
        t.forward(length)
        t.penup()
        t.backward(length + radius)
        t.left(90)

y.penup()
y.goto(85, 110)
y.fillcolor("yellow")
y.pendown()
y.begin_fill()
y.circle(45)
y.end_fill()

y.penup()
y.goto(85, 169)
y.pendown()
drawFourRays(y, 85, 54)
y.right(45)
drawFourRays(y, 85, 54)
y.left(45)

turtle.done()

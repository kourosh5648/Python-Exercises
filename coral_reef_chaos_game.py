import turtle
import random

screen = turtle.Screen()
screen.setup(700, 700)
screen.bgcolor("black")
screen.tracer(0)

t = turtle.Turtle()
t.speed(0)
t.color("coral")
t.hideturtle()
t.penup()

x = 0.0
y = 0.0

for _ in range(100000):
    r = random.random()

    if r < 0.40:
        nx = 0.31 * x - 0.53 * y + 0.89
        ny = -0.46 * x - 0.29 * y + 1.04

    elif r < 0.55:
        nx = 0.31 * x - 0.08 * y + 0.22
        ny = 0.15 * x - 0.45 * y + 0.34

    else:
        nx = 0.55 * y + 0.01
        ny = 0.69 * x - 0.20 * y + 0.38

    x = nx
    y = ny

    t.goto(x * 500 - 250, y * 500 - 250)
    t.dot(2)

screen.update()
turtle.done()

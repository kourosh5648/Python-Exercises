import turtle
import random
turtle.speed(0)
points=[(0,0) , (500,0) , (250,433)]
turtle.color('blue')
for x , y in points:
    turtle.pendown()
    turtle.goto(x,y)
    turtle.dot(4,'red')
turtle.goto(0,0)
for _ in range(5000):
    gol=random.choice(points)
    now_x , now_y = turtle.pos()
    new_x=(now_x + gol[0])/2
    new_y=(now_y + gol[1])/2
    turtle.goto(new_x , new_y)
    turtle.dot(1,'red')
turtle.done()
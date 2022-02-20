import turtle
from random import randint


import turtle
loadWindow = turtle.Screen()
turtle.bgcolor("black")
turtle.color("white")
turtle.speed(11)

for i in range(200):
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)

    turtle.colormode(255)  
    turtle.pencolor(r,g,b)
    turtle.circle(0.5*i)
    turtle.left(45)

turtle.exitonclick()
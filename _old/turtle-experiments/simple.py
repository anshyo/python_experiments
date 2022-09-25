import turtle
from random import randint

turtle.bgcolor("black")
s = turtle.getscreen()
t = turtle.Turtle()
t.color("white")
t.speed("fastest")
n=10
x=-10
while n <= 150:
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)

    turtle.colormode(255)
    
    t.pencolor(r,g,b)
    t.circle(n)
    t.fd(2) 
    t.left(2)
    n = n+1

turtle.exitonclick()


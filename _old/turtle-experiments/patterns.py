from turtle import * 
from random import randint 

def sqr():
    bgcolor('black') 
    x = 1 
    speed(0) 
    while x < 500: 
        r = randint(0,255) 
        g = randint(0,255)  
        b = randint(0,255) 
        
        colormode(255)  
        pencolor(r,g,b) 
        fd(1 + x) 
        rt(90.991) 
        x = x+1 
    
    exitonclick() 
sqr()
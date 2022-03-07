from turtle import Screen 
import random
import turtle 

display = Screen ()
def box (turtl) :
    turtl.penup ()
    turtl.goto (-display.canvwidth/2,-display.canvheight/2)
    turtl.left (90)
    turtl.pendown ()
    for iterator in range (2) :
        turtl.forward (display.canvheight)
        turtl.right (90)
        turtl.forward (display.canvwidth)
        turtl.right (90)

    

turtle.colormode (255)
def random_color () :
    r = random.randint (0,255)
    g = random.randint (0,255)
    b = random.randint (0,255)
    return (r ,g ,b)
from turtle import *
def idi_dole(razmak):
    penup()
    right(90)
    forward(razmak)
    left(90)
    pendown()
def idi_centar():
    penup()
    goto(0,0)
    pendown()
color("green")
speed(200)
br_krugova = 10
pprecnik = 30
idi_dole(pprecnik)
for i in range(1,br_krugova+1):
    circle(pprecnik*i)
    idi_dole(pprecnik)
forward(300)
idi_centar()

exitonclick()
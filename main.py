from turtle import *
#this changes the line thickness of the flower
x = 1


speed(100)
for i in range(56):
    pensize(x)
    forward(i)
    right(55)

right(55)
forward(13)

backward(30)
left(170)



def skib(fan):
    left(45)
    forward(fan)

for i in range(3):
    skib(40)
    skib(40)
    left(90)
    skib(40)
    skib(40)

up()
goto(60,90)
down()

for i in range(56):
    pensize(x)
    forward(i)
    right(55)
right(55)
forward(13)
backward(30)
left(170)

up()
goto(85,-5)
down()

for i in range(42):
    pensize(x)
    forward(i)
    right(55)

up()
goto(-70,-50)
down()

setheading(0)

def po(gee, hh):
    nack = gee + hh
    
    forward(nack)
    right(120)
    forward(nack)
    right(120)
    forward(nack)
po(gee=100,hh = 90)
        

exitonclick()




import turtle

loop=200
turtle.speed(20000)
turtle.showturtle()

for i in range(0,65):
    for j in range(0, 3):
        turtle.forward(loop)
        turtle.left(60)
    turtle.forward(5)
    turtle.left(2)
    loop = loop-3

turtle.hideturtle()


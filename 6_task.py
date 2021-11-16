import turtle
turtle.shape('turtle')
x=40
for j in range(10):
    for i in range(4):
        turtle.forward(x)
        turtle.left(90)
    turtle.right(90)
    turtle.penup()
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.right(180)
    turtle.pendown()
    x+=20
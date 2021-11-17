import turtle as tr
tr.shape('turtle')
x = 10
y = 10
tr.color("black", "red")
for j in range(10):
    for i in range(4):
        tr.forward(x)
        tr.left(90)
    tr.penup()
    tr.right(90)
    tr.forward(y)
    tr.right(90)
    tr.forward(y)
    tr.right(180)
    tr.pendown()
    x += 2 * y
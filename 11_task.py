import turtle as tr


def circle(r):
    tr.left(90)
    for i in range(72):

        tr.shape('turtle')
        tr.speed(20)
        tr.forward(5)
        tr.left(5)
    return
r = 20
step = 15
number_of_circles_pair = 5
for i in range(number_of_circles_pair):
    circle(r)
    r += step



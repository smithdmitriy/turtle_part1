import turtle as tr


def star(a=300, n=5):
    tr.speed(5)
    angle = 1 / n * 180
    for i in range(n):
        tr.right(180 - angle)
        tr.forward(a)

    return


star()
tr.pu()
tr.forward(350)
tr.pd()
star(300, 11)

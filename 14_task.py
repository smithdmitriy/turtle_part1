import turtle as tr

def star(r:float,n: int):
    tr.speed(5)
    angle = 1 / n * 180
    for i in range(n):
        tr.right(180-angle)
        tr.forward(300)

    return

star(20,5)
tr.pu()
tr.forward(350)
tr.pd()
star(20,11)


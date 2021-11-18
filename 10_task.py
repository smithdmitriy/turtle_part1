import turtle as tr


def circle():
    for i in range(72):
        tr.shape('turtle')
        tr.speed(20)
        tr.forward(5)
        tr.left(5)
    return


number_of_petals = 5
for i in range(number_of_petals):
    circle()
    tr.left(360 / number_of_petals)

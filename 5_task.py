import turtle as tr
tr.shape('turtle')
tr.speed(10)
side_of_the_square = 10
distance_between_squares = 10
for j in range(10):
    for i in range(4):
        tr.forward(side_of_the_square)
        tr.left(90)
    tr.penup()
    tr.right(90)
    tr.forward(distance_between_squares)
    tr.right(90)
    tr.forward(distance_between_squares)
    tr.right(180)
    tr.pendown()
    side_of_the_square += 2 * distance_between_squares

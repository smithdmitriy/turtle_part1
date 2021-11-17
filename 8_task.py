import turtle as tr
tr.shape('turtle')
tr.speed(10)
lenght_of_line = 3
distance_between_lines = 3
for j in range(20):
    for i in range(4):
        tr.forward(lenght_of_line)
        tr.left(90)
        lenght_of_line += distance_between_lines


import turtle as tr
tr.shape('turtle')
tr.speed(10)
number_of_beams = 12
beam_length = 300
i = 1
while i <= number_of_beams:
    tr.forward(beam_length)
    tr.stamp()
    tr.backward(beam_length)
    tr.right(360 / number_of_beams)
    i += 1

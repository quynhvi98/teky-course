import turtle
gordon = turtle.Pen()
gordon.shape("turtle")
gordon.color("blue")
gordon.width(3)
for i in range(20):
    gordon.forward(10*i)
    gordon.left(90)
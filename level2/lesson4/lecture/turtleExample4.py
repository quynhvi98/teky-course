import turtle
# Di chuyển nhưng không vẽ
screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.shape("circle")
# bắt đầu vẽ hình vuông
t.penup() # chỉ cho di duyển nhưng không vẽ
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
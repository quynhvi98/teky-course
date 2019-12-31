import turtle
# Thiết lập màu vẽ với hàm color
screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.shape("circle")
# bắt đầu vẽ hình vuông
t.pendown() # chỉ cho di duyển và vẽ
# màu vẽ là blue
t.color("blue")
# thiết lập tốc độ vẽ: 0 là rất nhanh, 10 là
# nhanh, 6 là bình thường và 3 chậm, rất chậm là 1
t.speed(10)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
# Chèn thư viện đồ họa turtle
import turtle
import math
import random

# Khởi tạo màn hình đồ họa
screen = turtle.Screen()
# thiết lập độ rộng của màn hình đồ họa
screen.setup(400, 400)
# Thiết lập hình ảnh nền cho màn hình đồ họa
screen.bgcolor("red")
# Tựa đề
screen.title("Giải cứu không gian 3")


# ---Class siêu anh hùng
class SuperHero(turtle.Turtle):
    # Hàm khởi tạo các thuộc tính mỗi khi class được gọi
    def __init__(self):  # Chú ý: __init__ không phải là _init_ nhé
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.shape("triangle")  # thuộc tính hình dạng
        self.color("white")  # thuộc tính màu sắc
        self.spedd = 1  # thuộc tính tốc độ

    def move(self):
        self.forward(self.speed)

    def turn_left(self):
        self.left(30)
    def accelerate(self):
        self.speed += 1
    def decelerate(self):
        self.speed -=1
#Khởi tạo đối tượng của lớp siêu anh hùng


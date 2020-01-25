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
    def turn_right(self):
        self.left(30)
    def accelerate(self):
        self.speed += 1
    def decelerate(self):
        self.speed -=1
# Khởi tạo đối tượng của lớp siêu anh hùng
player = SuperHero()
# Thiết lập điều khiển nhân vật bằng bàn phím
turtle.listen()
turtle.onkey(player.turn_left(), "Left")
turtle.onkey(player.turn_right(), "Right")
turtle.onkey(player.accelerate(), "Up")
turtle.onkey(player.decelerate(), "Down")
#Class border
class BienVien(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.color("white") #thuộc tính màu sắc
        self.pensize(5) #màu biên
    def draw_border(self):
        self.penup()
        self.goto(-300, -300)
        self.pendown()
        self.goto(-300, 300)
        self.goto(300, 300)
        self.goto(300, -300)
        self.goto(-300, -300)
        self.hideturtle()

#Khởi tạo đối tượng biên viền
border = BienVien()
border.draw_border()



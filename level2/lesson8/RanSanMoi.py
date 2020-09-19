# Chèn thư viện đồ họa turtle
import math
import random
import turtle

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
class Monster(turtle.Turtle):
    def __init__(self): #chú ý
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.shape("circle") #thuộc tính hình dạng
        self.color("green") #thuộc tính màu sắc
        self.speed = 3 #thuộc tính màu sắc
        self.goto(random.randint(-250, 250), random.randint(-250, 250))
        self.setheading(random.randint(0, 360))

#Hàm thiết lập khi va cham với siêu anh hùng thì quái vật sẽ đặt ở 1 vị trí ngẫu nhiên
    def jump(self):
        self.goto(random.randint(-250, 250), random.randint(-250, 250))
        self.setheading(random.randint(0, 360))
    #Hàm di chuyển, khi quái vật chạm viền sẽ quay lại
    def move(self):
        self.forward(self.speed)
        if self.xcor() > 290:
            self.setx(290)
            self.right(60)
        if self.xcor() < -290:
            self.setx(-290)
            self.right(60)
        if self.ycor() > 290:
            self.sety(290)
            self.right(60)
        if self.ycor() < -290:
            self.sety(-290)
            self.right(60)
# Khai báo đối tượng quái vật
quaivat = Monster()
# Chương trình chính
white true:
    player.move()
    # Thiết lập 6 con quái vật di chuyển
    for qv in quaivat:
        qv.move()
        # Kiểm tra sự va chạm quái vật và siêu anh
    if ifCollision(player, qv)
        qv.jump()
    quaivat.move()
def isCollision(t1, t2):
    #khoảng cách giữa siêu anh hùng và quái vật
    d = math.sqrt(math.pow(t1.xcor() - t2.xcor(),2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if d<20:
        return True
    else:
        return False
quaivat= Monster()
quaivat = []
for i in range(6):
    quaivat.append(Monster())

class Score(turtle.Turtle):
    def __init__(self): # chú ý: __init__ không phải là: _init_ nhé
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.spedd(0)
        self.speed(0)
        self.color("white")
        self.goto(-290, 310)
        self.score = 0
    def update_score(self):
        self.clear()
        self.write("Score: {}".format(self.score), False, align = "left", font=("Arial", 14))
    def change_score(self, points):
        self.score += points
        self.update_score()
# Khởi tạo đối tượng của lớp Score()
score = Score()



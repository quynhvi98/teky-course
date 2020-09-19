import math
import random
import turtle

sc = turtle.Screen()
# Thiết lập hình ảnh nền cho màn hình đồ họa
sc.bgcolor("lightgreen")
# Vẽ vùng giới hạn di chuyển
mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-300, 300)
mypen.pendown()
mypen.pensize(3)
mypen.speed(0)
for i in range(4):
    mypen.forward(600)
    mypen.left(90)
# vẽ xong, ấn đối tượng vẽ
mypen.hideturtle()

# Tạo ra nhân vật siêu anh hùng
player = turtle.Turtle()
player.color("yellow")
player.shape("turtle")
player.penup()
# Thiết lập tốc độ siêu anh hùng
speed = 1
# Định nghĩa các phím di chuyển
def turnleft():
    player.left(30)
def turnright():
    player.right(30)
def increaseSpeed():
    global speed
    speed += 1
    if speed >= 5:
        speed = 5
def decreaseSpeed():
    global speed
    speed -= 1
    if speed <= -5:
        speed = -5
# khi nhấm phím

turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(increaseSpeed, "Up")
turtle.onkey(decreaseSpeed, "Down")

# Xử lý khi siêu anh hùng di chuyển va chạm vào bien
# while True:
# # thiết lập siêu anh hùng tiến về phía trước
#     player.forward(speed)
# #kiểm tra xem khi di chuyển có chạm biên không
#     if player.xcor() < -290 or player.xcor() > 290:
#         player.right(180)
#     if player.ycor() < -290 or player.ycor() > 290:
#         player.right(180)
# Tạo ra quái vật
goal = turtle.Turtle()
sc.addshape("circle")
goal.penup()
goal.speed(0)
# hàm setposition() đặt đối tượng ở vị trí (x, y)
goal.setposition(random.randint(-300, 300), random.randint(-300, 300))

# Kiểm tra va chạm giữa hai nhân vật
def isCollision(t1, t2):
    #khoảng cách giữa siêu anh hùng và quái vật
    d = math.sqrt(math.pow(t1.xcor() - t2.xcor(),2) + math.pow(t1.ycor() - t2.ycor(),2))
    if d<20:
        return True
    else:
        return False
# Tạo hàm kiểm tra các nhân vật khi chạm biên
def boundaryChecking(t):
    #hàm xcor(): lấy tọa độ X hiện tại của đối tượng, ycor(): lấy tọa độ y
    if t.xcor() < -300 or t.xcor() > 300:
        t.right(180)
        t.setposition(random.randint(-300, 300), random.randint(-300, 300))
    if t.ycor() < -300 or t.ycor() > 300:
        t.right(180)
        t.setposition(random.randint(-300, 300), random.randint(-300, 300))

# Viết lại phần while
while True:
    player.forward(speed)
    # kiểm tra siêu anh hùng có chạm biên hay không
    boundaryChecking(player)
    # kiểm tra va chạm
    if isCollision(player, goal):
        print("Ðã giải cứu được thế giới")
        break
    # thiết lập quái vật di chuyển
    goal.forward(10)
    goal.left(random.randint(10,180))
    # kiểm tra quái vật có chạm biên hay không
    boundaryChecking(goal)

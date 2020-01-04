# Chèn thư viện đồ họa turtle
import turtle
# Khỏi tạo màn hình đồ họa
screen = turtle.Screen()
# Thiết lập độ rộng của màn hình đồ họa
screen.setup(400, 400)
# Thiết lập hình ảnh nền cho màn hình đồ họa
screen.bgpic("space.gif")
# Thiết lập hình ảnh nền cho màn hình đồ họa
turtle.shape("triangle")
turtle.color("white")
# Thiết lập tốc độ di chuyển của nhân vật
move_speed = 10
turn_speed = 10

# Thiết lập các hàm
def forward():
    turtle.forward(move_speed)
def backward():
    turtle.backward(move_speed)
def left():
    turtle.left(turn_speed)
def right():
    turtle.right(turn_speed)
# Thiết lập không vẽ khi di chuyển
turtle.penup()
# Hàm onkey: sẽ gọi các hàm khi bạn nhấn vào các phím tương ứng
screen.onkey(forward, "Up")
screen.onkey(backward, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.listen()
# Chèn thư viện đồ họa turtle
import turtle
# Khởi tạo màn hình đồ họa
screen = turtle.Screen()
# Thiết lập độ rộng của màn hình đồ họa
screen.setup(400, 400)
# Thiết lập hình ảnh nền cho màn hình đồ họa
screen.bgpic("space.gif")
# Gán biến image
image = "tau.gif"
# Chèn đối tượng hình ảnh vào màn hình đồ họa
screen.addshape(image)
turtle.shape(image)
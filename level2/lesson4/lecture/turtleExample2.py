import turtle

screen = turtle.Screen()
screen.bgcolor("red")
# Khỏi tạo đối tượng đồ họa
t = turtle.Turtle()
#  'arrow', 'turtle', 'circle', 'square', 'triangle',
# 'classic'
t.shape("circle")

t.forward(100) # tiến về phía trước với tọa độ x = 100
t.goto(100,0) # di chuyển đối tượng tới vị trí tọa độ (100, 0)
t.right(90) # quay phải 90 độ
t.left(90) # quay phải 90 độ
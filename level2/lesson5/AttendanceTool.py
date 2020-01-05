from turtle import *

sc = Screen()
pen = Turtle()
pen.ht()
border = Turtle()
border.ht()
border.speed(0)


# mot so ham ho tro
def make_square(pen, x, y, width, color="white", text=""):
    pen.penup()
    pen.color('black')
    pen.setpos(x, y)
    pen.pendown()
    # pen.begin_fill()
    pen.setpos(x + width, y)
    pen.setpos(x + width, y + width)
    pen.setpos(x, y + width)
    pen.setpos(x, y)
    # pen.end_fill()
    pen.penup()
    pen.setpos(x + width / 2, y + width / 2)
    pen.color('white')
    pen.write(text, align='center')


# Du lieu su dung
ds = [
    ["HS 1 nguyen van x", 0],
    ["HS 2 nguyen van x", 0],
    ["HS 3 nguyen van y", 0],
    ["HS 4 nguyen van z", 0],
    ["HS 5 nguyen Kan x", 0],
    ["HS 6 nguyen van x", 0],
    ["HS 7 nguyen van x", 0]
]
ds_turtle = [
    Turtle(),
    Turtle(),
    Turtle(),
    Turtle(),
    Turtle(),
    Turtle(),
    Turtle(),
]
for t in ds_turtle:
    t.penup()
    t.ht()


# Hien thi danh sach hoc sinh
def show_list():
    pass


# Show content
def show_content():
    pen.write(" Start app , app run ok ", align='center')
    make_square(border, -150, -150, 300, )
    pen.clear()
    pen.penup()
    y = 120
    for index in range(len(ds_turtle)):
        t = ds_turtle[index]
        hs = ds[index]
        hs_name = hs[0]
        t.sety(y)
        y = y - 20
        t.write(hs_name, align='center')


# Nút bắt đầu
startBtn = Turtle()
startBtn.penup()
startBtn = Turtle()
startBtn = Turtle()
startBtn = Turtle()
startBtn = Turtle()
startBtn = Turtle()
startBtn.shape('square')
startBtn.color('green')
startBtn.write('    Start App ')


def start_app(x, y):
    startBtn.ht()
    startBtn.clear()
    show_content()
    print(pen.xcor())
    print(pen.ycor())


startBtn.onclick(start_app)

# Nút bắt đầu
exit = Turtle()
exit.penup()
exit.shape('square')
exit.color('red')
exit.setpos(-150, -150)
exit.write('    Exit App ')


def exit_app(x, y):
    exit.ht()
    exit.clear()
    sc.clear()


exit.onclick(exit_app)

# ds =   ["Trần Mai Ngô", 10, 8.56],
#     ["Lý Quốc Tuân", 11, 1.95],
#     ["Nguyễn Minh Phú", 1, 9.56],
#     ["Lê Nhân Tô", 6, 1.24],
#     ["Hồ Đức Trịnh", 4, 2.77],
#     ["Hà Vinh Khoa", 5, 0.98],
#     ["Đinh Thắm Tăng", 6, 6.65],
#     ["Lâm Dung Kha", 12, 3.21],
#     ["Lý Ngô Sa", 1, 9.44],
#     ["Đinh Tú Tăng", 4, 8.81],
#     ["Phan Thủy Tuân", 5, 6.24],
#     ["Hồ Tú Kim", 8, 9.70]]

# def show_ds ():
#   pass
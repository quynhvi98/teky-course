import time
import turtle

delay = 0.1

# set up the creen
win = turtle.Screen()
win.title("Snake game")
win.bgcolor("blue")
win.setup(width=600, height=600)
win.tracer(0)

# Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 100)
head.direction = "stop"


# Functions to move the snake
def move():
    if head.direction == "up":
        y = head.ycor()  # y coordinate of the turtle
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()  # y coordinate of the turtle
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()  # y coordinate of the turtle
        head.setx(x + 20)
    if head.direction == "left":
        x = head.xcor()  # y coordinate of the turtle
        head.setx(x - 20)


def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "right"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def go_left():
    if head.direction != "right":
        head.direction = "left"


# keyboard bindings
win.listen()
win.onkey(go_up, "w")
win.onkey(go_down, "s")
win.onkey(go_right, "d")
win.onkey(go_left, "a")

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.shapesize(0.50, 0.50)
food.goto(0, 0)

# Main Game loop
while True:
    win.update()
    move()
    time.sleep(delay)

import math
import random
import turtle

hoasc = turtle.Screen()
hoasc.bgcolor("black")
hoasc.title("Space Invasion II")

mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-300, -300)
mypen.pendown()
mypen.pensize(3)
mypen.speed(0)
for i in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()

pl_one = turtle.Turtle()
pl_one.shape("turtle")
pl_one.color("white")
pl_one.penup()
pl_one.setposition(0, -250)
pl_one.setheading(90)
pl_onespeed = 15

pl_two = turtle.Turtle()
pl_two.shape("turtle")
pl_two.color("green")
pl_two.penup()
pl_two.speed(0)
pl_two.setposition(random.randint(-300, 300), random.randint(-100, 300))
pl_twospeed = 2
pl_two.right(90)

bull_one = turtle.Turtle()
bull_one.shape("triangle")
bull_one.color("red")
bull_one.penup()
bull_one.speed(0)
bull_one.setheading(90)
bull_one.shapesize(0.5, 0.5)
bull_one.hideturtle
bull_onespeed = 20
bull_onestate = "ready"

bull_two = turtle.Turtle()
bull_two.shape("square")
bull_two.color("blue")
bull_two.penup()
bull_two.speed(0)
bull_two.setheading(90)
bull_two.shapesize(0.5, 0.5)
bull_two.hideturtle
bull_twostate = "ready"
bull_twospeed = 20


def fire_bull_one():
    global bull_onestate
    if bull_onestate == "ready":
        bull_onestate = "fire"
        x = pl_one.xcor()
        y = pl_one.ycor() + 10
        bull_one.setposition(x, y)
        bull_one.showturtle()


def fire_bull_two():
    global bull_twostate
    if bull_twostate == "ready":
        bull_twostate = "fire"
        x = pl_two.xcor()
        y = pl_two.ycor() + 10
        bull_two.setposition(x, y)
        bull_two.showturtle()


def move_left():
    x = pl_one.xcor()
    x -= pl_onespeed
    if x < -280:
        x = -280
    pl_one.setx(x)


def move_right():
    x = pl_one.xcor()
    x += pl_onespeed
    if x > 280:
        x = 280
    pl_one.setx(x)


turtle.onkey(move_left, "a")
turtle.onkey(move_right, "d")
turtle.onkey(fire_bull_one, "space")
turtle.listen()


def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if (distance < 20):
        return True
    else:
        return False


def boundaryChecking(t):
    if t.xcor() < -300 or t.xcor() > 300:
        t.right(180)
        t.setposition(random.randint(-300, 300), random.randint(-300, 300))
    if t.xcor() < -300 or t.xcor() > 300:
        t.right(180)
        t.setposition(random.randint(-300, 300), random.randint(-300, 300))
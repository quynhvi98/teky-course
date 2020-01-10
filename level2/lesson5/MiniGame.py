import turtle
import random
import time

screen = turtle.Screen()
#Thiet lap hinh nen
screen.setup(500,500)
screen.bgcolor('black')
#thiet lap nhan vat
nhan_vat = turtle.Turtle()
nhan_vat.shape('triangle')
nhan_vat.color('white')
nhan_vat.penup()
#Thiet lap enemies
enemy = turtle.Turtle()
enemy.shape('arrow')
enemy.color('red')
enemy.penup()
#Thiet lap toc do di chuyen cho nhan vat
move_speed = 10
turn_speed = 10
#Thiet lap cac ham
def forward():
	nhan_vat.forward(move_speed)
def backward():
	nhan_vat.backward(move_speed)
def left():
	nhan_vat.left(turn_speed)
def right():
	nhan_vat.right(turn_speed)
#Thiet lap dieu khien nhan vat bang ban phim
screen.onkey(forward,'Up')
screen.onkey(backward,'Down')
screen.onkey(left,'Left')
screen.onkey(right,'Right')
screen.listen()
#Enemies Setup
while True:
	x = random.randint(-200,200)
	y = random.randint(100,250)
	enemy.setposition(x,y)

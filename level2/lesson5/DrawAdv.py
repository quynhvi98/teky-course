import turtle
#Screen
screen = turtle.Screen()
screen.bgcolor('light green')
arrow1 = turtle.Turtle()
arrow2 = turtle.Turtle()
#Do_hoa
arrow1.shape('arrow')
arrow2.shape('arrow')
#BTVN
#Bai_8
	#Tam giac can
arrow2.left(180)
arrow1.forward(45)
arrow2.forward(45)
arrow1.left(135)
arrow2.right(135)
arrow1.forward(65)
arrow2.forward(65)
	#Reset part 1
arrow1.penup()
arrow2.penup()
arrow1.goto(0,200)
arrow2.goto(0,200)
arrow1.pendown()
arrow2.pendown()
arrow1.left(45)
arrow2.right(45)

	#Hinh chu nhat
arrow1.forward(45)
arrow2.forward(45)
arrow1.left(90)
arrow2.right(90)
arrow1.forward(60)
arrow2.forward(60)
arrow1.left(90)
arrow2.right(90)
arrow1.forward(45)
arrow2.forward(45)

	#Reset part 2
arrow1.penup()
arrow1.goto(200,0)
arrow1.pendown()

	#Hinh tron
t1 = 1
for t1 in range (360):
	arrow1.forward(1)
	arrow1.left(1)
	t1 += 1

	#Reset part 3
arrow2.penup()
arrow2.goto(200,200)
arrow2.right(90)
arrow2.pendown()

	#Me cung
motion1 = 90
t2 = 1
for t2 in range (18):
	arrow2.forward(motion1)
	arrow2.right(90)
	motion1 -= 5
	t2 += 1
#Bai_9
	#Hinh1
t3 = 1
		#Reset
arrow1.penup()
arrow1.goto(0,-200)
arrow1.left(60)
arrow1.pendown()
		#Ve Hinh
for t3 in range (5):
	arrow1.forward(100)
	arrow1.left(145)
	t3 += 1
	#Hinh2
arrow3 = turtle.Turtle()
arrow4 = turtle.Turtle()
arrow5 = turtle.Turtle()
 		#Reset
arrow3.shape('arrow')
arrow4.shape('arrow')
arrow5.shape('arrow')
arrow1.color('blue')
arrow2.color('black')
arrow3.color('red')
arrow4.color('yellow')
arrow5.color('green')
arrow1.penup()
arrow2.penup()
arrow3.penup()
arrow4.penup()
arrow5.penup()
arrow1.goto(200,-200)
arrow1.right(65)
arrow2.goto(330,-200)
arrow2.left(90)
arrow3.goto(460,-200)
arrow4.goto(265,-270)
arrow5.goto(395,-270)
arrow1.pendown()
arrow2.pendown()
arrow3.pendown()
arrow4.pendown()
arrow5.pendown()
		#Ve Hinh
t4 = 1
for t4 in range (360):
	arrow1.forward(1)
	arrow1.left(1)
	t4 += 1
t5 = 1
for t5 in range (360):
	arrow2.forward(1)
	arrow2.left(1)
	t5 += 1
t6 = 1
for t6 in range (360):
	arrow3.forward(1)
	arrow3.left(1)
	t6 += 1
t7 = 1
for t7 in range (360):
	arrow4.forward(1)
	arrow4.left(1)
	t7 += 1
t8 = 1
for t8 in range (360):
	arrow5.forward(1)
	arrow5.left(1)
	t8 += 1
	#Hinh3
		#Reset
arrow1.penup()
arrow2.penup()
arrow3.penup()
arrow4.penup()
arrow5.penup()
arrow1.goto(900,-200)
arrow2.goto(900,-200)
arrow2.left(180)
arrow3.goto(800,-100)
arrow3.left(45)
arrow4.goto(820,-180)
arrow5.goto(830,-180)
arrow5.left(90)
arrow1.pendown()
arrow2.pendown()
arrow3.pendown()
arrow4.pendown()
arrow5.pendown()
		#Ve Hinh
#Than Nha
arrow1.forward(100)
arrow2.forward(100)
arrow1.left(90)
arrow2.right(90)
arrow1.forward(100)
arrow2.forward(100)
arrow1.left(90)
arrow2.right(90)
arrow1.forward(100)
arrow2.forward(100)
#Mai Nha
arrow3.forward(145)
arrow3.right(90)
arrow3.forward(145)
#Cua Nha
arrow1.penup()
arrow2.penup()
arrow1.goto(900,-200)
arrow2.goto(900,-200)
arrow1.pendown()
arrow2.pendown()
arrow1.forward(10)
arrow2.forward(10)
arrow1.right(90)
arrow2.left(90)
arrow1.forward(35)
arrow2.forward(35)
arrow1.right(90)
arrow2.left(90)
arrow1.forward(10)
arrow2.forward(10)
#Cua So
	#Cua So 1
arrow4.forward(20)
arrow4.left(90)
arrow4.forward(20)
arrow4.left(90)
arrow4.forward(20)
arrow4.left(90)
arrow4.forward(20)
arrow4.left(90)
arrow5.forward(20)
arrow5.penup()
arrow5.goto(820,-170)
arrow5.right(90)
arrow5.pendown()
arrow5.forward(20)
	#Reset
arrow4.penup()
arrow4.goto(820,-130)
arrow4.pendown()
arrow5.penup()
arrow5.goto(820,-120)
arrow5.pendown()
	#Cua So 2
arrow4.forward(20)
arrow4.left(90)
arrow4.forward(20)
arrow4.left(90)
arrow4.forward(20)
arrow4.left(90)
arrow4.forward(20)
arrow4.left(90)
arrow5.forward(20)
arrow5.penup()
arrow5.goto(830,-130)
arrow5.left(90)
arrow5.pendown()
arrow5.forward(20)
	#Reset
arrow4.penup()
arrow4.goto(970,-180)
arrow4.pendown()
arrow5.penup()
arrow5.goto(980,-180)
arrow5.pendown()
	#Cua So 3
arrow4.forward(20)
arrow4.left(90)
arrow4.forward(20)
arrow4.left(90)
arrow4.forward(20)
arrow4.left(90)
arrow4.forward(20)
arrow4.left(90)
arrow5.forward(20)
arrow5.penup()
arrow5.goto(970,-170)
arrow5.right(90)
arrow5.pendown()
arrow5.forward(20)
	#Reset
arrow4.penup()
arrow4.goto(970,-130)
arrow4.pendown()
arrow5.penup()
arrow5.goto(970,-120)
arrow5.pendown()
	#Cua So 4
arrow4.forward(20)
arrow4.left(90)
arrow4.forward(20)
arrow4.left(90)
arrow4.forward(20)
arrow4.left(90)
arrow4.forward(20)
arrow4.left(90)
arrow5.forward(20)
arrow5.penup()
arrow5.goto(980,-130)
arrow5.left(90)
arrow5.pendown()
arrow5.forward(20)
	#Reset
arrow4.penup()
arrow4.goto(900,-130)
arrow4.pendown()
arrow5.penup()
arrow5.goto(900,-130)
arrow5.pendown()
	#Ve Hinh
t9 = 1
for t9 in range (360):
	arrow4.forward(0.05)
	arrow4.left(1)
	t9 += 1
arrow5.forward(20)
arrow5.penup()
arrow5.goto(890,-120)
arrow5.pendown()
arrow5.right(90)
arrow5.forward(20)
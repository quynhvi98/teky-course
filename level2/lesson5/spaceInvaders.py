import math
import random
import turtle

# set up sceen
wn = turtle.Screen()
wn.setup(800, 800)
wn.bgcolor("gray")

# Draw border
bpen = turtle.Turtle()
bpen.hideturtle()
bpen.speed(0)
bpen.color("white")
bpen.penup()
bpen.setposition(-300, -300)
bpen.pensize(3)
bpen.pendown()

for side in range(4):
    bpen.fd(600)
    bpen.lt(90)

# draw score
score = 0
score_pen = turtle.Turtle()
score_pen.color("white")
score_pen.speed(0)
score_pen.penup()
score_pen.hideturtle()
score_pen.setposition(-290, 280)
myscore = "Score: %s" % (score)
score_pen.write(myscore)

# Create player Turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.speed(0)
player.penup()
player.setposition(0, -250)
player.lt(90)

playerspeed = 20
# number of enemies
number_of_enemies = 5
wn.register_shape("space.gif")
enemies = []
for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())
for enemy in enemies:
    # Create the enemy
    enemy.color("red")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)
    enemy.speed(50)

enemyspeed = 4

# create the bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.speed(0)
bullet.penup()
bullet.hideturtle()
bullet.lt(90)
bullet.setposition(player.xcor(), player.ycor() + 15)

bulletspeed = 30

# define bullet state
bulletstate = "ready"


# move player left and right
def move_left():
    x = player.xcor()
    x -= playerspeed
    if (x < -280):
        x = -280
    player.setx(x)


def move_right():
    x = player.xcor()
    x += playerspeed
    if (x > 280):
        x = 280
    player.setx(x)


# define bullet movement
def fire_bullet():
    global bulletstate
    if (bulletstate == "ready"):
        bulletstate = "fire"
        x = player.xcor()
        y = player.ycor() + 15
        bullet.setposition(x, y)
        bullet.showturtle()


# define collision
def iscollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if (distance < 20):
        return True
    else:
        return False


# keyboard bindings
wn.listen()
wn.onkey(move_left, "Left")
wn.onkey(move_right, "Right")
wn.onkey(fire_bullet, "Space")

# Main game loop
while True:
    for enemy in enemies:
        # move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        # reverse enemy
        if (enemy.xcor() > 280):
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1

        if (enemy.xcor() < -280):
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1

        # check for collision between bullet and enemy
        if (iscollision(bullet, enemy)):
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(player.xcor(), player.ycor() + 15)
            x = random.randint(-200, 200)
            y = random.randint(180, 250)
            enemy.setposition(x, y)
            score += 10
            myscore = "Score: %s" % (score)
            score_pen.clear()
            score_pen.write(myscore)

        # check for player collison
        if (iscollision(player, enemy)):
            player.hideturtle()
            enemy.hideturtle()
            bullet.hideturtle()
            print('Game Over')
            break;

        for e in enemies:
            if (e.ycor() < -270):
                player.hideturtle()
                e.hideturtle()
                bullet.hideturtle()
                print('Game Over')
                break;

            # move the bullet
    y = bullet.ycor()
    y += bulletspeed
    bullet.sety(y)

    # border check bullet
    if (bullet.ycor() > 275):
        bullet.hideturtle()
        bulletstate = "ready"

Delay = input("Press enter to exit:")
print(delay)









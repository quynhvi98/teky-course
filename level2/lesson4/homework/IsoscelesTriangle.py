import turtle

screen = turtle.Screen()
screen.bgcolor("pink")

# simple equilateral triangle
simpleEquilateralTriangle = turtle.Turtle()

simpleEquilateralTriangle.forward(100)  # draw base

simpleEquilateralTriangle.left(120)
simpleEquilateralTriangle.forward(100)

simpleEquilateralTriangle.left(120)
simpleEquilateralTriangle.forward(100)

turtle.done()

# right angled triangle
right_angled_triangle = turtle.Turtle()

right_angled_triangle.forward(100)  # draw base

right_angled_triangle.left(90)
right_angled_triangle.forward(100)

right_angled_triangle.left(135)
right_angled_triangle.forward(142)

turtle.done()

# drawing two identical isosceles triangles
twoIdenticalIsoscelesTriangles = turtle.Turtle()

# first triangle for star
twoIdenticalIsoscelesTriangles.forward(100)  # draw base

twoIdenticalIsoscelesTriangles.left(120)
twoIdenticalIsoscelesTriangles.forward(100)

twoIdenticalIsoscelesTriangles.left(120)
twoIdenticalIsoscelesTriangles.forward(100)

twoIdenticalIsoscelesTriangles.penup()
twoIdenticalIsoscelesTriangles.right(150)
twoIdenticalIsoscelesTriangles.forward(50)

# second triangle for star
twoIdenticalIsoscelesTriangles.pendown()
twoIdenticalIsoscelesTriangles.right(90)
twoIdenticalIsoscelesTriangles.forward(100)

twoIdenticalIsoscelesTriangles.right(120)
twoIdenticalIsoscelesTriangles.forward(100)

twoIdenticalIsoscelesTriangles.right(120)
twoIdenticalIsoscelesTriangles.forward(100)

turtle.done()
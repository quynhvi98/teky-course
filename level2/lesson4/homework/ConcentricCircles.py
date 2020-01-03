import turtle

ConcentricCircles = turtle.Turtle()
for i in range(50):
    ConcentricCircles.circle(10 * i)
    ConcentricCircles.up()
    ConcentricCircles.sety((10 * i) * (-1))
    ConcentricCircles.down()
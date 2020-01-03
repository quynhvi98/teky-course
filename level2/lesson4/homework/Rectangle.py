import turtle

rectangle = turtle.Turtle()
rectangle.forward(150)  # Forward turtle by 150 units
rectangle.left(90)  # Turn turtle by 90 degree
rectangle.forward(80)  # Forward turtle by 80 units
rectangle.left(90)  # Turn turtle by 90 degree
rectangle.forward(150)  # Forward turtle by 150 units
rectangle.left(90)  # Turn turtle by 90 degree
rectangle.forward(80)  # Forward turtle by 80 units
rectangle.left(90)  # Turn turtle by 90 degree

# Using loops to draw rectangle 
#Forward turtle by 150 units turn turtle by 90 degree forward turtle by 80 units turn turtle by 90 degree
t = turtle.Turtle()
for i in range(2):
  t.forward(150)
  t.left(90)
  t.forward(80)
  t.left(90)
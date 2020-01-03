import turtle

square = turtle.Turtle()
square.forward(100)  # Forward turtle by 100 units
square.left(90)  # Turn turtle by 90 degree
square.forward(100)
square.left(90)
square.forward(100)
square.left(90)
square.forward(100)
square.left(90)

# using loop
t = turtle.Turtle()
for i in range(4): # for loop will run 4 times forward turtle by 100 units turn turtle by 90 degree
  t.forward(100)
  t.left(90) 
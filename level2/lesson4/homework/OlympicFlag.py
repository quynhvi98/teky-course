import turtle

OFFSET = 165
HALF_OFFSET = OFFSET/2
BORDER = 10
UPPER_LINE = 0
LOWER_LINE = UPPER_LINE - (HALF_OFFSET + BORDER/4)


def draw_circle(turtle, x=0, y=0, width=10, color="black", size=75):
       """
       Take a turtle, draw a circle.
       Takes 6 arguments, including the turtle.

       turtle: The turtle to use. Save the world, re-use your turtle.
       x: X coordinate offset from 0
       y: Y coordinate offset from 0
       width: width of the border of the ring
       """
       turtle.up()
       turtle.goto(x, y)
       turtle.down()
       turtle.width(width)
       turtle.color(color)
       turtle.circle(size)


def main():
       t = turtle.Pen()
       draw_circle(t, -OFFSET, UPPER_LINE, BORDER, "blue")
       draw_circle(t)
       draw_circle(t, OFFSET, UPPER_LINE, BORDER, "red")
       draw_circle(t, -HALF_OFFSET, LOWER_LINE, BORDER, "yellow")
       draw_circle(t, HALF_OFFSET, LOWER_LINE, BORDER, "green")

       input("Press any key...")

if __name__ == "__main__":
       main()


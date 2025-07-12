sides = int(input("How many sides does the figure have? (1, 2, 3, etc.): "))
degrees = 360 / sides

# Determine length based on number of sides
if sides >= 191:
    length = 2
elif 99 <= sides <= 190:
    length = 5
elif 40 <= sides <= 98:
    length = 10
elif 20 <= sides <= 39:
    length = 25
elif 11 <= sides <= 19:
    length = 50
else:
    length = 100

import turtle

timmy = turtle.Turtle()
timmy.shape("turtle")
timmy.color("chartreuse")

for _ in range(sides):
    timmy.forward(length)
    timmy.right(degrees)

my_screen = turtle.Screen()
my_screen.exitonclick()

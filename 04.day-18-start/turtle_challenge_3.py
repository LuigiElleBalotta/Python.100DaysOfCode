from turtle import Turtle, Screen
import random

# For each shape, divide 360 by the number of sides
# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon

colors = ["aquamarine", "sienna", "tomato", "medium violet red", "medium slate blue", "orange", "pale green", "black"]

# Initialize turtle
tim = Turtle()
tim.shape("turtle")
tim.color("red")

# Center the starting point
tim.hideturtle()
tim.penup()
tim.setx(-50)
tim.sety(50)

# Draw a dashed line
tim.pendown()
tim.showturtle()


# Power of logic!
def draw_shape(sides):
    for _ in range(sides):
        tim.forward(100)
        tim.right(360 / sides)


sides = 3
for _ in range(8):
    tim.color(random.choice(colors))
    draw_shape(sides)
    sides += 1

screen = Screen()
screen.exitonclick()

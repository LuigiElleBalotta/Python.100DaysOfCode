from turtle import Turtle, Screen, colormode
import random

# Make a Spirograph
# Draw a number of circles with a radius of 100 in distance and gap 10


# Initialize turtle
tim = Turtle()
tim.shape("turtle")
tim.color("red")
colormode(255)  # Set the color mode to RGB, otherwise turtle will only accept 0-1 and so it will throw error.

# Center the starting point
tim.hideturtle()
tim.penup()

tim.pendown()
tim.showturtle()
tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def draw_spirograph(gap: int, radius: int):
    for _ in range(int(360/gap)):
        tim.color(random_color())
        tim.circle(radius)
        tim.setheading(tim.heading() + gap)


draw_spirograph(10, 100)


screen = Screen()
screen.exitonclick()


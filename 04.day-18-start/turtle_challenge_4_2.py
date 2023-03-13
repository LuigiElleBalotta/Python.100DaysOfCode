from turtle import Turtle, Screen, colormode
import random

# Draw a random walk with random colors


# Initialize turtle
tim = Turtle()
tim.shape("turtle")
tim.color("red")
colormode(255)  # Set the color mode to RGB, otherwise turtle will only accept 0-1 and so it will throw error.

# Center the starting point
tim.hideturtle()
tim.penup()
tim.setx(-50)
tim.sety(50)

tim.pendown()
tim.showturtle()
tim.pensize(5)


# Power of logic!
directions = [0, 90, 180, 270]
tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()


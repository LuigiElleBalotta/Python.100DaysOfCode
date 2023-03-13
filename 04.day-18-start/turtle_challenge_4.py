from turtle import Turtle, Screen
import random

# Draw a random walk


# Initialize turtle
tim = Turtle()
tim.shape("turtle")
tim.color("red")

# Center the starting point
tim.hideturtle()
tim.penup()
tim.setx(-50)
tim.sety(50)

tim.pendown()
tim.showturtle()
tim.pensize(5)


# Power of logic!
colors = ["aquamarine", "sienna", "tomato", "medium violet red", "medium slate blue", "orange", "pale green", "black"]
directions = [0, 90, 180, 270]
tim.speed("fastest")


for _ in range(200):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()

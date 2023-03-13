from turtle import Turtle, Screen

# Initialize turtle
tim = Turtle()
tim.shape("turtle")
tim.color("red")
tim.speed("slowest")

# Center the starting point
tim.hideturtle()
tim.penup()
tim.setx(-50)
tim.sety(50)

# Draw a square
tim.pendown()
tim.showturtle()
for _ in range(4):
    tim.forward(100)
    tim.right(90)

import heroes
print(heroes.gen())

screen = Screen()
screen.exitonclick()

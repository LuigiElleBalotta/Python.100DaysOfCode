from turtle import Turtle, Screen

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
for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

screen = Screen()
screen.exitonclick()
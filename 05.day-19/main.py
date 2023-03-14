from turtle import Turtle, Screen

from movement_hander import MovementHandler

tim = Turtle()
tim.shape("turtle")
tim.color("green")

susanne = Turtle()
susanne.shape("turtle")
susanne.color("red")

tom = Turtle()
tom.shape("turtle")
tom.color("blue")

gerry = Turtle()
gerry.shape("turtle")
gerry.color("orange")

salva = Turtle()
salva.shape("turtle")
salva.color("purple")

screen = Screen()
screen.setup(width=500, height=400)

# Manual turtle handling: (comment out the following lines to use the MovementHandler)
# handler = MovementHandler(tim, screen)
# handler.start_listening()

# Turtle race:
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race= Enter a color: ")

tim.penup()
susanne.penup()
tom.penup()
gerry.penup()
salva.penup()

tim.goto(x=-230, y=100)
susanne.goto(x=-230, y=50)
tom.goto(x=-230, y=0)
gerry.goto(x=-230, y=-50)
salva.goto(x=-230, y=-100)

tim_handler = MovementHandler(tim, screen)
susanne_handler = MovementHandler(susanne, screen)
tom_handler = MovementHandler(tom, screen)
gerry_handler = MovementHandler(gerry, screen)
salva_handler = MovementHandler(salva, screen)

max_distance = 230
winner = ""

while winner == "":
    tim_handler.move_random_forwards()
    susanne_handler.move_random_forwards()
    tom_handler.move_random_forwards()
    gerry_handler.move_random_forwards()
    salva_handler.move_random_forwards()

    if tim.xcor() >= max_distance:
        winner = "green"

    if susanne.xcor() >= max_distance:
        winner = "red"

    if tom.xcor() >= max_distance:
        winner = "blue"

    if gerry.xcor() >= max_distance:
        winner = "orange"

    if salva.xcor() >= max_distance:
        winner = "purple"

if user_bet == winner:
    print(f"You've won! The {winner} turtle is the winner!")
else:
    print(f"You've lost! The {winner} turtle is the winner!")

screen.exitonclick()

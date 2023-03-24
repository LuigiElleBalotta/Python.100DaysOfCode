from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle = Turtle(shape=image)

data = pandas.read_csv("50_states.csv")

all_states = data.state.to_list()
correctStates = 0
placed_states = []


while correctStates < 50:
    answer_state = screen.textinput(title=f"{correctStates}/50 States Correct", prompt="What's another state's name?").title()
    if str.lower(answer_state) == "exit":
        break
    if answer_state.title() not in placed_states:
        queried_state = data[data.state == answer_state.title()]
        if not queried_state.empty:
            correctStates += 1
            state_lbl = Turtle()
            state_lbl.hideturtle()
            state_lbl.penup()
            state_lbl.goto(float(queried_state.x), float(queried_state.y))
            state_lbl.write(queried_state.state.item())
            placed_states.append(queried_state.state.item())

screen.exitonclick()

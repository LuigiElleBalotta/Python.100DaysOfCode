import colorgram as cg
import random
import turtle as t

# Exercise 1 - Print a list of all colors from the image. Eac item should be a tuple.

print("Parsing image colors...")
colors = cg.extract('image.jpg', 30)
rgb_colors = []


def get_color_tuple(color: cg.Color):
    return color.rgb.r, color.rgb.g, color.rgb.b


def is_not_white_like(colors_tp):
    return colors_tp[0] < 245 and colors_tp[1] < 245 and colors_tp[2] < 245


for c in colors:
    colors_tuple = get_color_tuple(c)
    if is_not_white_like(colors_tuple):  # Filter out white-like colors
        rgb_colors.append(colors_tuple)


print(rgb_colors)

# Exercise 2 - Use the colors from the list to draw a painting.
# Every dot size is 20x20, and there are 10 dots in a row and 10 dots in a column.
# The distance between each dot is 50 pixels.
print("Drawing painting...")

tim = t.Turtle()
tim.shape("turtle")
t.colormode(255)
tim.speed("fastest")
tim.penup()         # Don't draw the path
tim.hideturtle()    # Don't show the turtle
tim.setx(-250)      # Start from the left
tim.sety(-250)      # Start from the bottom

rows_number = 10
columns_number = 10

for _ in range(rows_number):
    for _ in range(columns_number):
        tim.dot(20, random.choice(rgb_colors))
        tim.forward(50)
    tim.setx(-250)      # Reset x
    tim.setheading(90)  # Turn to the top
    tim.forward(50)     # Move to the next row
    tim.setheading(0)   # Turn to the right for the next line

screen = t.Screen()
screen.exitonclick()



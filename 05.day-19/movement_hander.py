import random
import turtle as t


class MovementHandler:
    def __init__(self, turtle: t.Turtle, screen: t.Screen):
        self.turtle = turtle
        self.screen = screen

    def move_forwards(self):
        self.turtle.forward(10)

    def move_random_forwards(self):
        self.turtle.forward(random.randint(0, 10))

    def move_backwards(self):
        self.turtle.backward(10)

    def rotate_left(self):
        self.turtle.left(10)

    def rotate_right(self):
        self.turtle.right(10)

    def reset(self):
        # My solution:
        # self.turtle.reset()
        # self.turtle.setx(0)
        # self.turtle.sety(0)

        # Alternative (by Angela):
        self.turtle.clear()
        self.turtle.penup()
        self.turtle.home()
        self.turtle.pendown()

    def start_listening(self):
        self.screen.listen()
        self.screen.onkey(key="w", fun=self.move_forwards)
        self.screen.onkey(key="s", fun=self.move_backwards)
        self.screen.onkey(key="a", fun=self.rotate_left)
        self.screen.onkey(key="d", fun=self.rotate_right)
        self.screen.onkey(key="c", fun=self.reset)


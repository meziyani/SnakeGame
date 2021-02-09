from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        # Init
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=0.7 , stretch_wid=0.7)
        self.speed("fastest")
        self.color("white")
        self.refresh()

    def refresh(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)

from turtle import Turtle
from random import randint

class Food(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("yellow")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x_y = (randint(-280,280), randint(-280,280))
        self.goto(random_x_y)
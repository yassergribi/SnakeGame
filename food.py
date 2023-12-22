from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.shapesize(stretch_len=0.8,stretch_wid=0.8)
        self.color('blue')
        self.speed('fastest')
        self.refresh()
        

    def refresh(self):
        x = random.randint(-275, 275)
        y = random.randint(-275, 275)
        self.goto(x,y)


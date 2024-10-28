from turtle import Turtle
from random import randint
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.hideturtle()
        x = randint(-280, 280)
        y = randint(-280, 280)
        self.goto(x,y)
        self.showturtle()


    def on_collision_with_snake(self):
        self.hideturtle()
        x = randint(-280, 280)
        y = randint(-280, 280)
        self.goto(x, y)
        self.showturtle()




food=Turtle()
from turtle import Turtle

snake_positions = [(0,0),(-20,0),(-40,0)]

from random import randint
class Snake():
    def __init__(self):
        self.segments = []


        for i in range(0, len(snake_positions)):
            self.segment = Turtle('circle')
            self.segment.penup()
            self.segment.color("white")
            self.segment.goto(snake_positions[i])
            self.segments.append(self.segment)

    def  move(self):
        for i in range(len(self.segments)-1,0,-1):
            x=self.segments[i-1].xcor()
            y=self.segments[i-1].ycor()
            self.segments[i].goto(x,y)
        self.segments[0].forward(20)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)
    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)
    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)
    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def add_extension(self):
        new_segment=Turtle('circle')
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(self.segments[-1].position())
        self.segments.append(new_segment)














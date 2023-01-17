import turtle
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.shapesize(0.5, 0.5, 1)
        self.penup()


    def right_up(self):
        self.direction = 0
        self.newx = self.xcor() + 2
        self.newy = self.ycor() + 1
        self.goto(self.newx, self.newy)

    def right_down(self):
        self.direction = 1
        self.newx = self.xcor() + 2
        self.newy = self.ycor() - 1
        self.goto(self.newx, self.newy)

    def left_up(self):
        self.direction = 2
        self.newx = self.xcor() - 2
        self.newy = self.ycor() + 1
        self.goto(self.newx, self.newy)

    def left_down(self):
        self.direction = 3
        self.newx = self.xcor() - 2
        self.newy = self.ycor() - 1
        self.goto(self.newx, self.newy)

    def still(self):
        self.direction = 4
        self.newx = self.xcor()
        self.newy = self.ycor()
        self.goto(self.newx, self.newy)
from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(1, 4, 1)
        self.goto(-380, 0)
        self.right(90)

    def move_up(self):
        if self.ycor() > 240:
            return
        self.setheading(90)
        self.forward(40)

    def move_down(self):
        if self.ycor() < -240:
            return
        self.setheading(270)
        self.forward(40)

class Paddle2(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(1, 4, 1)
        self.goto(380, 0)
        self.right(90)

    def move_up(self):
        if self.ycor() > 240:
            return
        self.setheading(90)
        self.forward(40)

    def move_down(self):
        if self.ycor() < -240:
            return
        self.setheading(270)
        self.forward(40)
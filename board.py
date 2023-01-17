from turtle import Turtle

class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.pensize(5)
        self.goto(0, 300)
        self.color("white")
        self.shape("square")
        self.setheading(270)
        self.hideturtle()
        for n in range(20):
            self.pen(outline=0)
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(20)


class Score1(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(-80, 200)
        self.color("white")
        self.hideturtle()
        self.write(f"{self.score}", False, "left", ("Arial", 40, "normal"))

    def update(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", False, "left", ("Arial", 40, "normal"))

class Score2(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(80, 200)
        self.color("white")
        self.hideturtle()
        self.write(f"{self.score}", False, "right", ("Arial", 40, "normal"))

    def update(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", False, "left", ("Arial", 40, "normal"))
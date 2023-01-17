from turtle import Turtle, Screen
from paddle import Paddle, Paddle2
from board import Board, Score1, Score2
from ball import Ball
import random

import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.listen()
screen.tracer(0)

screen.title("Pong")
paddle = Paddle()
paddle2 = Paddle2()
board = Board()
ball = Ball()
score1 = Score1()
score2 = Score2()
screen.onkeypress(paddle.move_up, "w")
screen.onkeypress(paddle.move_down, "s")
screen.onkeypress(paddle2.move_up, "Up")
screen.onkeypress(paddle2.move_down, "Down")


ball.direction = 3

def move():
    paddle2_height = paddle2.ycor()
    paddle_height = paddle.ycor()

    if ball.direction == 0:
        ball.right_up()
        if ball.ycor() == 300:
            ball.direction = 1
        elif paddle2.xcor() - 10 < ball.xcor() < paddle2.xcor() + 10 and (paddle2_height + 40) > ball.ycor() > (paddle2_height - 40):
            ball.direction = 2
        elif ball.xcor() > 400:
            score1.update()
            new_round()


    if ball.direction == 1:
        ball.right_down()
        if ball.ycor() == -300:
            ball.direction = 0
        elif paddle2.xcor() - 10 < ball.xcor() < paddle2.xcor() + 10 and (paddle2_height + 40) > ball.ycor() > (paddle2_height - 40):
            ball.direction = 3
        elif ball.xcor() > 400:
            score1.update()
            new_round()


    if ball.direction == 2:
        ball.left_up()
        if ball.ycor() == 300:
            ball.direction = 3
        elif paddle.xcor() - 10 < ball.xcor() < paddle.xcor() + 10 and (paddle_height + 40) > ball.ycor() > (paddle_height - 40):
            ball.direction = 0
        elif ball.xcor() < -400:
            score2.update()
            new_round()

    if ball.direction == 3:
        ball.left_down()
        if ball.ycor() == -300:
            ball.direction = 2
        elif paddle.xcor() - 10 < ball.xcor() < paddle.xcor() + 10 and (paddle_height + 40) > ball.ycor() > (paddle_height - 40):
            ball.direction = 1
        elif ball.xcor() < -400:
            score2.update()
            new_round()


def new_round():
    ball.goto(0, 0)
    ball.direction = 4
    for n in range(100):
        screen.update()
        time.sleep(0.01)
    new_direction = random.randint(0, 3)
    ball.direction = new_direction


while True:
    screen.update()
    time.sleep(0.006)
    move()



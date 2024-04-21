from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.shape("turtle")

        self.set_start()

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def is_goal(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def set_start(self):
        self.goto(STARTING_POSITION)

from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-280, 250)
        self.level = 0
        self.increment_level()

    def increment_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}",align="left",font=FONT)

    def display_gameover(self):
        self.goto(0, 0)
        self.write("GAME OVER",align="center",font=FONT)

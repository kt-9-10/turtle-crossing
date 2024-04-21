import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

        self.cars = []

    def generate_car(self):
        if random.randint(0, 3) == 0:
            car = Turtle()
            car.penup()
            car.shape("square")
            car.setheading(180)
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.goto(320, random.randint(-240, 240))
            self.cars.append(car)

    def move(self):
        for i in range(0, len(self.cars) - 1):
            self.cars[i].forward(MOVE_INCREMENT)

    def destroy(self):
        for car in self.cars:
            if car.xcor() < -300:
                self.cars.remove(car)
                car.clear()
                car.hideturtle()

    def check_collision(self, player):
        for car in self.cars:
            if player.distance(car) < 20:
                return True
        return False


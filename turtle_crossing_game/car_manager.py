from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__ (self):

        self.allcars = []
        self.initial_speed = STARTING_MOVE_DISTANCE
        
    def create_car(self):
        x_pos = 300
        y_pos = random.randint(-250, 250)
        if random.randint(1, 6) == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid = 1, stretch_len = 2)
            new_car.penup()
            new_car.goto(y = y_pos, x = x_pos)
            new_car.setheading(180)
            self.allcars.append(new_car)
    
    def move_forward(self):
        for car in self.allcars:
            car.forward(self.initial_speed)
        
    def increase_speed(self):
        self.initial_speed += MOVE_INCREMENT
        
        
        

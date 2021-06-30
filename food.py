from turtle import Turtle
import random


class Food(Turtle):
    """Represents food for the game Snake."""

    def __init__(self):
        """Initialize attributes for the food class."""
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_wid=0.6, stretch_len=0.6)
        self.color("yellow")
        self.new_food()

    def new_food(self):
        """Spawns 1 food on the screen at a random coordinate."""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

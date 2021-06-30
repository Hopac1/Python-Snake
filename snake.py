from turtle import Turtle

# Game constants
START_POSITIONS = [(0, 0), (-20, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """
    A class used to represent a snake.
    """

    def __init__(self):
        """Initialize the snake's attributes."""
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head_shape()

    def create_snake(self):
        """Builds the snake head with 1 body block at the start of the game."""
        for position in START_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Adds one segment to the snake."""
        snake = Turtle("square")
        snake.color("green")
        snake.penup()
        snake.goto(position)
        self.segments.append(snake)
        self.snake_colour()

    def extend(self):
        """Extends the snake's body by 1 block (turtle)."""
        self.add_segment(self.segments[-1].position())

    def snake_colour(self):
        """Changes the colour of specific parts of the snake's body."""
        for seg in self.segments[4::5]:
            seg.color("pale goldenrod")

    def head_shape(self):
        """Changes the head shape of the snake to a circle and increases the
         size."""
        self.head.shape('circle')
        self.head.shapesize(1.3, 1.3)

    def snake_movement(self):
        """Move the snake's segments in reverse order."""
        for seg_index in range(len(self.segments) - 1, 0, -1):
            next_x = self.segments[seg_index - 1].xcor()
            next_y = self.segments[seg_index - 1].ycor()
            self.segments[seg_index].goto(next_x, next_y)
        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        """Removes all segments from the snake."""
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self.head_shape()

    def down(self):
        """Snake will head down if it isn't currently heading up."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def up(self):
        """Snake will head up if it isn't currently heading down."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def right(self):
        """Snake will head right if it isn't currently heading left."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        """Snake will head left if it isn't currently heading right."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

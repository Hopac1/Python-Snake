from turtle import Screen
import time

from snake import Snake
from food import Food
from score import Score

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

# Let user control the snake using their keyboard.
screen.listen()

# Keyboard controls
screen.onkeypress(fun=snake.down, key='s')
screen.onkeypress(fun=snake.up, key='w')
screen.onkeypress(fun=snake.right, key='d')
screen.onkeypress(fun=snake.left, key='a')

game_on = True

# Main game loop
while game_on:
    screen.update()
    time.sleep(0.1)
    score.refresh_score()
    snake.snake_movement()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.new_food()
        snake.extend()
        score.add_score()

    # Detect collision with wall
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or \
            snake.head.ycor() > 295 or snake.head.ycor() < -295:
        score.restart()
        snake.reset()
        time.sleep(1)

    # Detect collision with self
    for segment in snake.segments[1:]:
        if snake.head.position() == segment.position():
            score.restart()
            snake.reset()
            time.sleep(1)


screen.exitonclick()

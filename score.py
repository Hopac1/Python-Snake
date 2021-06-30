from turtle import Turtle

FONT = 'Times New Roman'


class Score(Turtle):
    """Represents a scoreboard for the Snake game."""

    def __init__(self):
        """Initialize attributes for the scoreboard."""
        super().__init__()
        self.score = 0
        with open('highscore.txt') as f:
            self.high_score = int(f.read())
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=0, y=270)

    def add_score(self):
        """Adds one to the current score."""
        self.score += 1
        self.refresh_score()

    def refresh_score(self):

        self.clear()
        self.write(arg=f"Score: {self.score}   High Score: {self.high_score}",
                   align="center",
                   font=(FONT, 18, "normal"))

    def restart(self):
        """Updates the high score and resets the score back to 0."""
        if self.score > self.high_score:
            self.high_score = self.score
            with open('highscore.txt', 'w') as file_object:
                file_object.write(f'{self.high_score}')
        self.score = 0
        self.refresh_score()

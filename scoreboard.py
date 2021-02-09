from turtle import Turtle


class Scoreboard(Turtle):

    FONT = ('Arial', 24, 'normal')

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.write(f"Score = {self.score}", True, align="center", font=self.FONT)

    def update(self):
        self.goto(0, 270)
        self.clear()
        self.score = self.score+1
        self.write(f"Score = {self.score}", True, align="center", font=self.FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", font=self.FONT)
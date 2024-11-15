from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 370)
        self.score = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Courier", 18, "normal"))

    def increase_score(self):
        self.score += 1
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 22, "normal"))
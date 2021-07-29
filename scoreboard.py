from turtle import Turtle


class Scoreboard(Turtle):
    score = 0

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        # self.goto(-100, 200)
        # self.print_score()
        # self.goto(100, 200)
        # self.print_score()

    def print_score(self):
        print("calling print score with 0")
        self.write(f"{self.score}", move=False, align="center", font=("Arial", 44, "normal"))

    def update_score(self):
        self.clear()
        self.score += 1
        self.print_score()

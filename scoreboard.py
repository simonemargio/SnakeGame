from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hight_score = 0
        self.check_score()
        self.penup()
        self.goto(-360, 380)
        self.hideturtle()
        self.color("white")
        self.scoreboard()

    def check_score(self):
        with open("data.txt", mode="r") as file:
            prev_score = file.read()
            self.hight_score = int(prev_score)

    def scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} - Hight score: {self.hight_score}", False, align="center",
                   font=("Arial", 20, "normal"))

    def update_score(self):
        self.score += 1
        self.scoreboard()

    def reset(self):
        if self.score > self.hight_score:
            self.hight_score = self.score
        self.score = 0
        self.scoreboard()

    def game_over(self):
        self.save_score()
        self.home()
        self.write("Game over! 🫡", False, align="center", font=("Arial", 20, "normal"))

    def save_score(self):
        with open("data.txt", mode="w") as file:
            file.write(str(self.hight_score))

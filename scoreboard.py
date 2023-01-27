from turtle import Turtle
file = open("data.txt")
high = int(file.read())

# Scoreboard that tracks score on game and saves high score to a file
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = high
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 275)

    def update(self):
        self.clear()
        self.write(arg=f"Score: {self.score} | High score: {self.high_score}", move=False, align="center", font=("Arial", 20,
                                                                                                   "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()

    def reset_board(self):
        if self.score > self.high_score:
            self.high_score = self.score
            file = open("data.txt", "w")
            file.write(str(self.high_score))
            file.close()
        self.score = 0
        self.update()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(arg="Game Over", move=False, align="center", font=("Arial", 20, "normal"))

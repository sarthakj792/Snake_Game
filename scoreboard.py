from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.pencolor("white")
        self.start=0
        try:
            with open("high_score.txt", mode="r") as f1:
                self.high_score = int(f1.read())
        except (FileNotFoundError, ValueError):
            self.high_score = 0  # Set a default score if file not found or invalid content

        self.write(f"Score : {self.start} High Score : {self.high_score}", False, "center", ("Arial", 16, "bold"))

    def add_increment(self):
        self.clear()
        self.start += 1
        self.write(f"Score : {self.start} High Score:{self.high_score}   ", False, "center", ("Arial", 16, "bold"))

    def display_game_over(self):
        self.goto(0, 0)
        self.write("Game Over",False,"center",("Arial",18,"bold"))
    def final_score(self):
        self.goto(0,140)
        self.write(f"Your final Score is {self.start}",True,"center",("Arial",18,"bold"))






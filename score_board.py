from turtle import Turtle

ALIGNMENT  = "center"
FONT = ('Arial', 15, 'normal')

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0,270)
        self.hideturtle()
        self.write(f"Score : {self.score}",align=ALIGNMENT, font= FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align=ALIGNMENT, font= FONT)
        
    def increase_score(self):
        self.score += 1 
        self.clear()
        self.write(f"Score : {self.score}",align= ALIGNMENT, font= FONT)
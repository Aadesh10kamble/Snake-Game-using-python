from turtle import Turtle

with open ("High_score.txt","r") as File :
    high_score = File.read ()

class Scoreboard (Turtle) :

    def __init__ (self) :
        super ().__init__ ()
        self.color ('white')
        self.hideturtle ()
        self.penup ()
        self.goto (0,310)
        self.score = 0
        self.highest_score = int (high_score)

    def show_score (self) :
        self.write (f"Score :  {self.score} || High Score : {self.highest_score}",align = "center",font = ("Arial",15,"normal") )
    
    def game_over (self) :
        self.goto (-80,0)
        self.write ("GAME OVER !!!",font = ("Arial",15,"normal"))

    def high_score (self) :
        if self.score > self.highest_score :
            self.highest_score = self.score 
        self.score = 0
        with open ("High_score.txt","w") as File :
            File.write (str (self.highest_score))
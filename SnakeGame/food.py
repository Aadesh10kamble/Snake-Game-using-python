from turtle import Turtle , Screen
from Turtle_user_function import box
import random 

class Food (Turtle) :

    def __init__ (self) :
        super().__init__ ()
        self.shape ('circle')
        self.penup ()
        self.shapesize (stretch_len = 0.5 , stretch_wid = 0.5)
        self.color ('red')
        self.speed (0)

    def random_position (self,x_cor,y_cor) :
        random_x = float (random.randrange ((- x_cor + 20) + 10,(x_cor -20 )- 10,20))
        random_y = float (random.randrange ((- y_cor + 20) + 10,(y_cor - 20) - 10,20))
        self.goto (random_x ,random_y)
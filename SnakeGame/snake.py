from turtle import Turtle 
from Turtle_user_function import random_color

class Snake :
    
    def __init__ (self) :
        self.snake = []
        self.starting_position = [(0,0),(-20,0),(-40,0)]

    def create_snake (self) :
        for position in self.starting_position :
            snake_element = Turtle (shape = 'square')
            snake_element.color ("white")
            snake_element.penup ()
            snake_element.goto (position)
            self.snake.append (snake_element)

    def movement (self) :
        previous_position = []
        for element in self.snake :
            previous_position.append ((element.xcor (),element.ycor ()))
            if self.snake.index (element) == 0 :
                element.forward (20)
            else :
                element.goto (previous_position[self.snake.index (element) - 1])
    
    def food_detected (self) :
        snake_part = Turtle (shape = 'square')
        snake_part.color ("white")
        snake_part.penup ()
        snake_part.goto (self.snake[-1].position ())
        self.snake.append (snake_part)

    def reset (self) :
        for snake_element in self.snake :
            snake_element.goto (1000,1000)
        self.snake.clear ()
        self.create_snake ()

    def up (self) :
        if self.snake[0].heading () != 270 :
            self.snake[0].setheading (90)

    def down (self) :
        if self.snake[0].heading () != 90 :
            self.snake[0].setheading (270)

    def right (self) :
        if self.snake[0].heading () != 180 :
            self.snake[0].setheading (0)

    def left (self) :
        if self.snake[0].heading () != 0 :
            self.snake[0].setheading (180)


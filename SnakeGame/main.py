from Turtle_user_function import box
from turtle import Turtle , Screen
from snake import Snake 
from food import Food
from scoreboard import Scoreboard
import time

display = Screen ()
display.bgcolor ('black')
display.canvheight = 620 
display.canvwidth = 620
display.setup (width = display.canvwidth + 100 , height = display.canvheight + 100)
display.tracer (0)


# Creating the wall.
boxer = Turtle ()
boxer.color ('white')
boxer.hideturtle ()
box (boxer)

# Indroducing apple.
apple = Food ()
apple.random_position (display.canvwidth/2 , display.canvheight/2)
display.update ()
scoreboard = Scoreboard ()

# Indroducing Snake.
player = Snake ()
player.create_snake ()

display.update ()
display.listen ()
display.onkey (key = 'w',fun = player.up)
display.onkey (key = 's',fun = player.down)
display.onkey (key = 'a',fun = player.left)
display.onkey (key = 'd',fun = player.right)
    
moving = True 
while moving :
    time.sleep (0.07)
    player.movement ()
    display.update ()
    scoreboard.show_score ()
    # Collison with food.
    if player.snake[0].distance (apple) < 10 :
        scoreboard.score += 1
        scoreboard.clear ()
        apple.random_position (display.canvwidth/2 , display.canvheight/2)
        player.food_detected ()
        # Collison with side walls.
    elif player.snake[0].xcor () > (display.canvwidth/2  ) or (player.snake[0].xcor () < - (display.canvwidth/2))  :
        scoreboard.high_score ()
        scoreboard.clear ()
        player.reset ()
    # Collison with top/bottom wall.
    elif player.snake[0].ycor () > (display.canvheight/2 ) or (player.snake[0].ycor () < - (display.canvheight/2))  :
        scoreboard.high_score ()
        scoreboard.clear ()
        player.reset ()
    # Collison with tail.
    for  snake_element in player.snake[1:] : 
        if player.snake[0].distance (snake_element) < 10 :
            scoreboard.high_score ()
            scoreboard.clear ()
            player.reset ()
    display.update ()
    
display.exitonclick ()
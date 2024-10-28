SCREEN_WIDTH = 600
SCREEN_HEIGHT=600
import time  #time.sleep  time module has a function called sleep which hold the program execution for a specific duration.
from turtle import  Screen #Screen is a class which creates an instance screen window.
from snake import Snake #snake is file , Snake is a class  in  which its  constructor has functionality to create snake body and class method called
#move used for moving the snake body with control.
from food import Food
from turtle import Turtle
from scoreboard import Scoreboard


screen = Screen()#window screeen is made up here.
screen.title("Snake Game") #window will get title called Snake Game
screen.setup(SCREEN_WIDTH,SCREEN_HEIGHT) #setting up the window height and width
screen.bgcolor("black") #sets the background color of winndow
screen.tracer(0) #keeps animation off (movement of every fragment of motion is turn off)


snake = Snake() #Snake class  constructor - creates snake body
food=Food()
screen.listen()#This alllows a screen to read the key which is pressed as an input.
screen.onkey(snake.up,"Up")#Interpreter would get to know on pressing key Up , it has to execute snake.up function
#snake.up is not called , it has left to be called on key pressing Up
screen.onkey(snake.down,"Down")
#Interpreter would ge to know on pressing Down key , snake.down function has to be called
screen.onkey(snake.right,"Right")
#Interpreter would ge to know on pressing Right key , snake.right  function has to be called
screen.onkey(snake.left,"Left")
#Interpreter would ge to know on pressing Left  key , snake.left  function has to be called
score=Scoreboard()
game_is_on = True
while game_is_on:

    screen.update() #Above created snake body display will get smoother.
    time.sleep(0.1)  #downslow the speed of fast moving snake.
    snake.move() #object snake has method move()  which will follow up segments in alignment.


    #snake collision wiith Food
    if snake.segments[0].distance(food)<20:
        food.on_collision_with_snake()
        score.add_increment()
        snake.add_extension()


    #collision with wall
    if snake.segments[0].xcor() > 295 or snake.segments[0].xcor() < -295  or snake.segments[0].ycor() > 295 or snake.segments[0].ycor() < -295:
        game_is_on=False
        score.display_game_over()
        score.final_score()
        if score.start > score.high_score:
            with open("high_score.txt",mode="w") as f1:
                f1.write(f"{score.start}")

    #collision with tail
    length=len(snake.segments)
    list_segment = snake.segments[1:length]
    for segment in list_segment:
        if snake.segments[0].distance(segment) < 10:
            game_is_on=False
            score.display_game_over()
            score.final_score()











screen.exitonclick()

















import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Set up GUI
screen = Screen()
screen.colormode(255)
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)

game = True

# Allows us to move snake using keyboard
snake = Snake()
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)


food = Food()
scoreboard = Scoreboard()
scoreboard.score = 0

# Game mechanics
while game:
    time.sleep(0.1)
    screen.update()
    snake.move()
    if snake.head.distance(food) < 15:
        food.move()
        scoreboard.increase_score()
        snake.add_snake()
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset_board()
        snake.rest()
    for seg in snake.snakes:
        if seg == snake.head:
            pass
        elif snake.head.distance(seg) < 10:
            scoreboard.reset_board()
            snake.rest()
    scoreboard.update()

screen.exitonclick()

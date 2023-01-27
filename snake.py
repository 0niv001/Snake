from turtle import Turtle

# Snake movement angles
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# Creates a segment of a snake and its movements
class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        x = 0
        for i in range(0,3):
            snake = Turtle("square")
            snake.color("white")
            snake.penup()
            snake.setx(x)
            x -=20
            self.snakes.append(snake)

    def add_snake(self):
        snake = Turtle("square")
        snake.penup()
        self.snakes.append(snake)
        snake.color("white")

    def move(self):
        for seg in range(len(self.snakes) - 1 ,0,-1):
            new_x = self.snakes[seg-1].xcor()
            new_y = self.snakes[seg -1].ycor()
            self.snakes[seg].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def rest(self):
        for snak in self.snakes:
            snak.goto(1000,1000)
        self.snakes.clear()
        self.create_snake()
        self.head = self.snakes[0]
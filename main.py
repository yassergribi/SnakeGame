import time
from turtle import Screen
from food import Food
from snake import Snake
from score_board import ScoreBoard


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detects collision with food. 
    if snake.head.distance(food) < 18:
        food.refresh()
        snake.get_bigger()
        score_board.increase_score()

    # Detects collision with wall
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285  or snake.head.ycor() < -285:
        game_on = False
        score_board.game_over()

    # Detects collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            score_board.game_over()
    
    
screen.exitonclick()
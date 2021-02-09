from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()

screen.setup(width=600, height=600)
screen.bgpic("random.png")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    snake.move()

    # Collision with food
    if snake.head.distance(food) < 15:
        scoreboard.update()
        food.refresh()
        snake.extend()

    # Collision with wall
    if snake.head.xcor() < -295 or snake.head.xcor() > 295 or snake.head.ycor() < -295 or snake.head.ycor() > 295:
        scoreboard.game_over()
        game_is_on = False

    # Collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()


from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
import time

in_game = True


def control():
    """
    Controls of the snake
    """
    s.onkey(snake.up, "Up")
    s.onkey(snake.down, "Down")
    s.onkey(snake.left, "Left")
    s.onkey(snake.right, "Right")
    s.onkey(exit_game, "q")


def exit_game():
    """
    Exit the game when the player presses q
    """
    global in_game
    in_game = False


def check_edge():
    """
    Check if the snake goes over the edge of the screen. If it happens = lose
    """
    if snake.head.xcor() > 480 or snake.head.xcor() < - 480 or snake.head.ycor() > 400 or snake.head.ycor() < - 400:
        return True
    else:
        return False


def engine():
    global in_game
    while in_game:
        time.sleep(0.1)
        s.update()
        snake.move()

        # I check that the snake approaches the yellow ball
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            score.update_score()

        # Check if the snake goes over the edge of the screen
        if check_edge():
            score.reset()
            snake.reset()

        # Check that the snake does not collide with itself
        for segnment in snake.segments[1:]:
            if snake.head.distance(segnment) < 10:
                score.reset()
                snake.reset()


# GUI
s = Screen()
s.screensize(600, 600)
s.tracer(0)
s.bgcolor("black")
s.title("Snake Game 🐍")

snake = Snake()
food = Food()
score = Scoreboard()

s.listen()
control()
engine()

score.game_over()
s.exitonclick()

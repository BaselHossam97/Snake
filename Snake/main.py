from snake import Snake
from turtle import Screen
import time
from food import Food
from ScoreBoard import scoreBoard

beso = Snake()
screen = Screen()
screen.bgcolor("Black")
screen.setup(600, 600)
screen.title("Snake")
food = Food()
board = scoreBoard()
screen.tracer(0)
screen.listen()
screen.onkey(beso.up, 'w')
screen.onkey(beso.up, 'Up')
screen.onkey(beso.down, 's')
screen.onkey(beso.down, 'Down')
screen.onkey(beso.right, 'd')
screen.onkey(beso.right, 'Right')
screen.onkey(beso.left, 'a')
screen.onkey(beso.left, 'Left')


game = True
while game:
    screen.update()
    time.sleep(0.1)
    beso.move()

    if beso.head.distance(food) < 15:
        board.incrementScore()
        beso.extend()
        food.refresh()
        #prevent food from spawning inside the snake
        for part in beso.parts:
            if part.distance(food) <15:
                food.refresh()

    if beso.head.xcor() > 290 or beso.head.xcor() < -290 or beso.head.ycor() > 280 or beso.head.ycor() < -280:
        game = False

    for seg in beso.parts:
        if seg == beso.head:
            pass
        elif seg.distance(beso.head) < 10:
            game = False


board.gameOver()




screen.exitonclick()











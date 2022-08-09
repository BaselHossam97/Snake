from turtle import Turtle

class scoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.speed('fastest')
        self.hideturtle()
        self.goto(0,270)
        self.penup()
        self.color('white')
        self.string1 = "Score: "
        self.write(self.string1 + str(self.score),align='center', font = ('arial', 20 , 'normal'))

    def incrementScore(self):
        self.score += 1
        self.clear()
        self.write(self.string1 + str(self.score),align='center', font = ('arial', 20 , 'normal'))

    def gameOver(self):
        self.color('red')
        self.goto(0,0)
        self.write("GAME OVER", align='center', font=('arial', 20, 'bold'))


from turtle import Turtle



class Snake:

    def __init__(self):
        self.parts = []
        self.createSnake()
        self.head = self.parts[0]



    def move(self):
        for n in range(len(self.parts) - 1, 0, -1):
            self.parts[n].goto(self.parts[n - 1].position())
        self.parts[0].forward(20)

    def addSegment(self,position):
        s = Turtle()
        s.color('white')
        s.shape('square')
        s.penup()
        s.goto(position)
        self.parts.append(s)

    def extend(self):
        self.addSegment(self.parts[-1].position())


    def createSnake(self):
        for n in range(3):
            self.addSegment((0,0))
        prevX = 0
        for t in self.parts:
            t.goto(prevX, 0)
            prevX -= 20

    def up(self):
        if self.head.heading() != 270:
            self.parts[0].setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.parts[0].setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.parts[0].setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.parts[0].setheading(0)



from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(5, 1)
        self.color("white")
        self.goto(position)

    def up(self):
        new_y_heading = self.ycor() + 20
        self.goto(self.xcor(), new_y_heading)

    def down(self):
        new_y_heading = self.ycor() - 20
        self.goto(self.xcor(), new_y_heading)

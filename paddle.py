from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_len=3)
        self.color('white')
        self.penup()
        # self.hideturtle()

    def set_paddle_position(self, position_x, position_y):
        self.goto(position_x, position_y)
        self.left(90)
        # self.showturtle()

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.backward(20)

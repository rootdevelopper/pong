from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.shape('circle')
        self.color('green')
        self.penup()
        self.x_move = 1
        self.y_move = 1

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)

    def bounce_ball(self):
        self.color('green')
        self.y_move *= -1

    def bounce_ball_on_paddle(self):
        self.color('blue')
        self.x_move *= -1

    def restart_ball_position(self):
        self.hideturtle()
        self.goto(x=0, y=0)
        self.showturtle()
        self.y_move *= -1
        self.x_move *= -1
        self.move_ball()

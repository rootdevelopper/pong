from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
PLAYER_1_COLOR = 'red'
PLAYER_2_COLOR = 'orange'


def setup_screen():
    screen.setup(height=600, width=800)
    screen.bgcolor('black')
    screen.listen()
    screen.title("PONG!")


def set_player_1():
    player_1.color(PLAYER_1_COLOR)
    player_1.set_paddle_position(position_x=350, position_y=0)


def set_player_2():
    player_2.color(PLAYER_2_COLOR)
    player_2.set_paddle_position(position_x=-350, position_y=0)


""" Passing the player to a function swaps the order in which the
    Paddles are displayed, not sure why...
"""


def set_player(player, color, x, y):
    player.color(color)
    player.set_paddle_position(position_x=-x, position_y=y)


def set_keyboard_controls():
    screen.listen()
    screen.onkey(player_1.move_up, 'Up')
    screen.onkey(player_1.move_down, 'Down')
    screen.onkey(player_2.move_up, 'q')
    screen.onkey(player_2.move_down, 'a')


def set_player_1_scoreboard():
    p1_scoreboard.goto(200, 200)
    p1_scoreboard.color(PLAYER_1_COLOR)
    p1_scoreboard.print_score()


def set_player_2_scoreboard():
    p2_scoreboard.goto(-200, 200)
    p2_scoreboard.color(PLAYER_2_COLOR)
    p2_scoreboard.print_score()


def bounce_ball_on_the_wall():
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_ball()


def bounce_ball_on_paddle():
    if ball.distance(player_1) < 50 and ball.xcor() > 330 or ball.distance(player_2) < 50 and ball.xcor() < -330:
        ball.bounce_ball_on_paddle()


def hit_right_wall():
    return ball.xcor() > 350


def hit_left_wall():
    return ball.xcor() < -360


def player_1_loose():
    print("Player 1 loose")
    ball.restart_ball_position()
    p2_scoreboard.update_score()


def player_2_loose():
    print("player 2 loose")
    ball.restart_ball_position()
    p1_scoreboard.update_score()


setup_screen()

player_1 = Paddle()
player_2 = Paddle()

set_player_1()
set_player_2()

set_keyboard_controls()

p1_scoreboard = Scoreboard()
p2_scoreboard = Scoreboard()
set_player_1_scoreboard()
set_player_2_scoreboard()

ball = Ball()
game_over = False

while not game_over:
    ball.move_ball()
    bounce_ball_on_the_wall()
    bounce_ball_on_paddle()

    if hit_right_wall():
        player_1_loose()
    elif hit_left_wall():
        player_2_loose()

screen.exitonclick()

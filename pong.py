from PPlay.window import *
from PPlay.keyboard import *
from PPlay.gameimage import *

WINDOW_SIZE_X = 600
WINDOW_SIZE_Y = 400

PADDLE_SIZE_Y = 80
PADDLE_SIZE_X = 15
BALL_SIZE_Y = 14


def main():
    goal_distance = 70
    left_goal = goal_distance
    right_goal = WINDOW_SIZE_X - goal_distance

    janela = Window(WINDOW_SIZE_X, WINDOW_SIZE_Y)

    janela.set_title("Pong")

    left_paddle = GameImage("paddle.png")
    right_paddle = GameImage("paddle.png")
    ball = GameImage("ball.png")
    meio = GameImage("meio.png")

    left_paddle.set_position(left_goal - PADDLE_SIZE_X, (WINDOW_SIZE_Y / 2) - (left_paddle.y / 2))
    right_paddle.set_position(right_goal + PADDLE_SIZE_X, (WINDOW_SIZE_Y / 2) - (right_paddle.y / 2))
    ball.set_position(WINDOW_SIZE_X / 2, WINDOW_SIZE_Y / 2)
    meio.set_position(WINDOW_SIZE_X / 2, 0)

    paddle_speed = 0.3
    ball_speed_y = 0.25
    ball_speed_x = 0.3

    player_1 = 0
    player_2 = 0

    keyboard = Keyboard()

    # ALTERACAO PRO EXERCICIO
    contador = 0

    while True:
        if keyboard.key_pressed("w"):
            if left_paddle.y >= 0:
                left_paddle.set_position(left_paddle.x, left_paddle.y - paddle_speed)
        elif keyboard.key_pressed("s"):
            if left_paddle.y <= WINDOW_SIZE_Y - PADDLE_SIZE_Y:
                left_paddle.set_position(left_paddle.x, left_paddle.y + paddle_speed)

        if keyboard.key_pressed("UP"):
            if right_paddle.y >= 0:
                right_paddle.set_position(right_paddle.x, right_paddle.y - paddle_speed)
        elif keyboard.key_pressed("DOWN"):
            if right_paddle.y <= WINDOW_SIZE_Y - PADDLE_SIZE_Y:
                right_paddle.set_position(right_paddle.x, right_paddle.y + paddle_speed)

        ball.set_position(ball.x + ball_speed_x, ball.y + ball_speed_y)

        # PONG NORMAL
        #if left_paddle.collided(ball) | right_paddle.collided(ball):
        #    ball_speed_x = 0 - ball_speed_x
        #    if (ball.y + BALL_SIZE_Y / 2 > left_paddle.y + PADDLE_SIZE_Y / 2) \
        #            | (ball.y + BALL_SIZE_Y / 2 > right_paddle.y + PADDLE_SIZE_Y / 2):
        #        ball_speed_y = abs(ball_speed_y)
        #    else:
        #        ball_speed_y = 0 - abs(ball_speed_y)

        # Colisao na parede esquerda
        if ball.x <= 0:
            # ALTERACAO DE EXERCICIO
            contador += 1
            if contador % 2 == 0 and ball_speed_x <= WINDOW_SIZE_X * 0.05 and ball_speed_y <= WINDOW_SIZE_Y * 0.05:
                if ball_speed_x >= 0:
                    ball_speed_x += 0.1
                else:
                    ball_speed_x -= 0.1
                print(ball_speed_x, ball_speed_y)
            ball_speed_x = - ball_speed_x
            # PONG NORMAL:
            #player_2 += 1
            #print(player_1, player_2)
            #ball.set_position(WINDOW_SIZE_X / 2, WINDOW_SIZE_Y / 2)
        # Colisao na parede direita
        if ball.x >= WINDOW_SIZE_X:
            # ALTERACAO DE EXERCICIO
            contador += 1
            if contador % 2 == 0 and ball_speed_x <= WINDOW_SIZE_X * 0.05 and ball_speed_y <= WINDOW_SIZE_Y * 0.05:
                if ball_speed_x >= 0:
                    ball_speed_x += 0.1
                else:
                    ball_speed_x -= 0.1
                print(ball_speed_x, ball_speed_y)
            ball_speed_x = - ball_speed_x
            # PONG NORMAL:
            #player_1 += 1
            #print(player_1, player_2)
            #ball.set_position(WINDOW_SIZE_X / 2, WINDOW_SIZE_Y / 2)
        # Colisao na parede superior e inferior
        if (ball.y <= 0) | (ball.y + BALL_SIZE_Y / 2 >= WINDOW_SIZE_Y):
            # ALTERACAO DE EXERCICIO
            contador += 1
            if contador % 2 == 0 and ball_speed_x <= WINDOW_SIZE_X * 0.05 and ball_speed_y <= WINDOW_SIZE_Y * 0.05:
                if ball_speed_y >= 0:
                    ball_speed_y += 0.1
                else:
                    ball_speed_y -= 0.1
                print(ball_speed_x, ball_speed_y)
            ball_speed_y = - ball_speed_y
            # PONG NORMAL
            # ball_speed_y = 0 - ball_speed_y

        janela.set_background_color((0, 0, 0))
        left_paddle.draw()
        right_paddle.draw()
        meio.draw()
        ball.draw()
        janela.update()


main()

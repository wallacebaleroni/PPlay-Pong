import random

from PPlay.window import *
from PPlay.keyboard import *
from PPlay.gameimage import *
from PPlay.mouse import *

WINDOW_SIZE_X = 600
WINDOW_SIZE_Y = 400

PADDLE_SIZE_Y = 80
PADDLE_SIZE_X = 15
BALL_SIZE_Y = 14
GOAL_DISTANCE = 70

BASE_SPEED = 100


def main():
    janela = Window(WINDOW_SIZE_X, WINDOW_SIZE_Y)
    janela.set_title("Pong")

    left_paddle = GameImage("../img/paddle.png")
    right_paddle = GameImage("../img/paddle.png")
    ball = GameImage("../img/ball.png")
    meio = GameImage("../img/meio.png")

    left_goal = GOAL_DISTANCE
    right_goal = WINDOW_SIZE_X - GOAL_DISTANCE

    left_paddle.set_position(left_goal - PADDLE_SIZE_X, (WINDOW_SIZE_Y / 2) - (left_paddle.y / 2))
    right_paddle.set_position(right_goal + PADDLE_SIZE_X, (WINDOW_SIZE_Y / 2) - (right_paddle.y / 2))
    ball.set_position(WINDOW_SIZE_X / 2, WINDOW_SIZE_Y / 2)
    meio.set_position(WINDOW_SIZE_X / 2, 0)

    paddle_speed = 5 * BASE_SPEED
    ia_left_paddle_speed = 5 * BASE_SPEED
    ia_right_paddle_speed = 3 * BASE_SPEED
    ball_speed_x = 4 * BASE_SPEED
    ball_speed_y = 5 * BASE_SPEED

    player_1_score = 0
    player_2_score = 0

    keyboard = Keyboard()
    mouse = Mouse()

    ultimo_frame_rate = janela.time_elapsed()
    frame_counter = 0
    frame_rate = 0

    # ALTERACAO PRO EXERCICIO - AUMENTAR VELOCIDADE
    #contador = 0

    while True:
        tempo = janela.delta_time()
        '''
        # Entrada do teclado pra controlar pad esquerdo
        if keyboard.key_pressed("w"):
            if left_paddle.y >= 0:
                #left_paddle.set_position(left_paddle.x, left_paddle.y - paddle_speed)
                left_paddle.set_position(left_paddle.x, left_paddle.y - paddle_speed * tempo)
        elif keyboard.key_pressed("s"):
            if left_paddle.y <= WINDOW_SIZE_Y - PADDLE_SIZE_Y:
                #left_paddle.set_position(left_paddle.x, left_paddle.y + paddle_speed)
                left_paddle.set_position(left_paddle.x, left_paddle.y + paddle_speed * tempo)
        '''
        # IA pra controlar pad direito
        if ball.y > left_paddle.y + PADDLE_SIZE_Y / 2:
            ia_left_paddle_speed = abs(ia_left_paddle_speed)
        else:
            ia_left_paddle_speed = 0 - abs(ia_left_paddle_speed)
        left_paddle.set_position(left_paddle.x, left_paddle.y + ia_left_paddle_speed * tempo)

        # ALTERACAO PRO EXERCICIO - MOVER COM MOUSE
        # Entrada do mouse pra controlar pad direito
        #mouse_pos = mouse.get_position()
        #right_paddle.set_position(right_paddle.x, mouse_pos[1])

        # PONG NORMAL
        # Entrada do teclado pra controlar pad direito
        #if keyboard.key_pressed("UP"):
        #    if right_paddle.y >= 0:
        #        right_paddle.set_position(right_paddle.x, right_paddle.y - paddle_speed * tempo)
        #elif keyboard.key_pressed("DOWN"):
        #    if right_paddle.y <= WINDOW_SIZE_Y - PADDLE_SIZE_Y:
        #        right_paddle.set_position(right_paddle.x, right_paddle.y + paddle_speed * tempo)

        # IA pra controlar pad direito
        if ball.y > right_paddle.y + PADDLE_SIZE_Y / 2:
            ia_right_paddle_speed = abs(ia_right_paddle_speed)
        else:
            ia_right_paddle_speed = 0 - abs(ia_right_paddle_speed)
        right_paddle.set_position(right_paddle.x, right_paddle.y + ia_right_paddle_speed * tempo)

        ball.set_position(ball.x + ball_speed_x * tempo, ball.y + ball_speed_y * tempo)


        # Colisao com as paletas
        if left_paddle.collided(ball) | right_paddle.collided(ball):
            ball_speed_x = 0 - ball_speed_x
            if (ball.y + BALL_SIZE_Y / 2 > left_paddle.y + PADDLE_SIZE_Y / 2) \
                    | (ball.y + BALL_SIZE_Y / 2 > right_paddle.y + PADDLE_SIZE_Y / 2):
                ball_speed_y = abs(ball_speed_y)
            else:
                ball_speed_y = 0 - abs(ball_speed_y)

        # Colisao na parede esquerda - ponto pro player 2
        if ball.x <= 0:
            # ALTERACAO DE EXERCICIO - AUMENTAR VELOCIDADE
            #contador += 1
            #if contador % 2 == 0 and ball_speed_x <= WINDOW_SIZE_X * 0.05 and ball_speed_y <= WINDOW_SIZE_Y * 0.05:
            #    if ball_speed_x >= 0:
            #        ball_speed_x += 0.1
            #    else:
            #        ball_speed_x -= 0.1
            #    print(ball_speed_x, ball_speed_y)
            # PONG NORMAL:
            player_2_score += 1
            # Reseta bola no centro com posicao aleatoria e direcao tambem aleatoria
            ball.set_position(WINDOW_SIZE_X / 2, random.randint(0, WINDOW_SIZE_Y))
            if random.randint(0,1) == 0:
                ball_speed_y = ball_speed_y
            else:
                ball_speed_y = 0 - ball_speed_y

            ball_speed_x = - ball_speed_x
        # Colisao na parede direita - ponto pro player 1
        if ball.x >= WINDOW_SIZE_X:
            # ALTERACAO DE EXERCICIO - AUMENTAR VELOCIDADE
            #contador += 1
            #if contador % 2 == 0 and ball_speed_x <= WINDOW_SIZE_X * 0.05 and ball_speed_y <= WINDOW_SIZE_Y * 0.05:
            #    if ball_speed_x >= 0:
            #        ball_speed_x += 0.1
            #    else:
            #        ball_speed_x -= 0.1
            #    print(ball_speed_x, ball_speed_y)
            # PONG NORMAL:
            player_1_score += 1
            # Reseta bola no centro com posicao aleatoria e direcao tambem aleatoria
            ball.set_position(WINDOW_SIZE_X / 2, random.randint(0, WINDOW_SIZE_Y))
            if random.randint(0,1) == 0:
                ball_speed_y = ball_speed_y
            else:
                ball_speed_y = 0 - ball_speed_y

            ball_speed_x = - ball_speed_x
        # Colisao na parede superior e inferior
        if (ball.y <= 0) | (ball.y + BALL_SIZE_Y / 2 >= WINDOW_SIZE_Y):
            # ALTERACAO DE EXERCICIO - AUMENTAR VELOCIDADE
            #contador += 1
            #if contador % 2 == 0 and ball_speed_x <= WINDOW_SIZE_X * 0.05 and ball_speed_y <= WINDOW_SIZE_Y * 0.05:
            #    if ball_speed_y >= 0:
            #        ball_speed_y += 0.1
            #    else:
            #        ball_speed_y -= 0.1
            #    print(ball_speed_x, ball_speed_y)
            #ball_speed_y = - ball_speed_y
            # PONG NORMAL
            # Rebate
            ball_speed_y = 0 - ball_speed_y

        # Controle do frame_rate
        tempo_atual = janela.time_elapsed()
        if(tempo_atual - ultimo_frame_rate > 1000):
            frame_rate = frame_counter
            frame_counter = 0
            ultimo_frame_rate = tempo_atual

        # Pinta fundo de preto
        janela.set_background_color((0, 0, 0))
        # Desenha placar e frame rate
        janela.draw_text(str(player_1_score), 10, 10, size=25, color=(255,255,255), bold=True)
        janela.draw_text(str(player_2_score), WINDOW_SIZE_X - 35, 10, size=25, color=(255,255,255), bold=True)
        janela.draw_text(str(frame_rate) + " FPS", 10, WINDOW_SIZE_Y - 22, size=15, color=(255, 255, 255), bold=True)
        # Desenha sprites
        left_paddle.draw()
        right_paddle.draw()
        meio.draw()
        ball.draw()
        # Atualiza janela
        janela.update()

        # Contador do frame rate
        frame_counter += 1

main()


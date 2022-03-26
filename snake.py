import outcome
import pygame
import time
import random

pygame.init()

tela_largura = 800
tela_altura = 600
tela = pygame.display.set_mode((tela_largura, tela_altura))
pygame.display.update()
pygame.display.set_caption("Snake Game - Geovanni Alves")

branco = (255, 255, 255)
amarelo = (255, 255, 102)
preto = (0, 0, 0)
vermelho = (255, 0, 0)
azul = (0, 0, 255)

snake_block = 10
snake_speed = 20

relogio = pygame.time.Clock()


font_style = pygame.font.SysFont("helvetica", 25)
score_font = pygame.font.SysFont("helvetica", 20)


def pontuacao(score):
    value = score_font.render("Sua Pontuação: " + str(score), True, preto)
    tela.blit(value, [0, 0])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(tela, preto, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    tela.blit(mesg, [tela_largura / 8, tela_altura / 8])


def gameLoop():

    game_over = False
    game_close = False

    x1 = tela_largura / 2
    y1 = tela_altura / 2

    x1_alterar = 0
    y1_alterar = 0

    snake_list = []
    len_of_snake = 1

    foodx = round(random.randrange(
        0, (tela_largura) - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(
        0, (tela_largura) - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            tela.fill(branco)
            message("Você perdeu! Precione S-Sair ou C-Continuar", vermelho)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_alterar = -snake_block
                    y1_alterar = 0
                elif event.key == pygame.K_RIGHT:
                    x1_alterar = snake_block
                    y1_alterar = 0
                elif event.key == pygame.K_UP:
                    x1_alterar = 0
                    y1_alterar = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_alterar = 0
                    y1_alterar = snake_block
        if x1 >= tela_largura or x1 < 0 or y1 >= tela_altura or y1 < 0:
            game_close = True

        x1 += x1_alterar
        y1 += y1_alterar
        tela.fill(branco)

        pygame.draw.rect(tela, azul, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > len_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)
        pontuacao(len_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(
                0, tela_largura - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(
                0, tela_altura - snake_block) / 10.0) * 10.0
            len_of_snake += 1
            pygame.display.update()

        relogio.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()

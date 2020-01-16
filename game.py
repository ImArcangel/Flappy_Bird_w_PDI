import pygame as pg
import sys
import time
import random as rd
import math as m
from pygame.locals import *


def pipe_random_height(gap, floor):
    a = rd.randint(100, height - gap - floor - 100)
    pipe_h = [a, int(a + gap + rd.randint(0, 3) * 20)]
    return pipe_h


def draw_game(play_surface, player_pos, pipe_pos, pipe_height, pipe_width):
    # background
    play_surface.fill((151, 203, 255))

    # draw player
    circle = pg.draw.circle(play_surface, (255, 244, 79),
                            (int(player_pos[0]), int(player_pos[1])), radius)

    # draw pipe
    pipe_up = pg.draw.rect(play_surface, (26, 148, 49), [
        pipe_pos, 0, pipe_width, pipe_height[0]], 0)
    pipe_dw = pg.draw.rect(play_surface, (26, 148, 49), [
        pipe_pos, pipe_height[1], pipe_width, 700], 0)

    # draw floor
    pg.draw.rect(play_surface, (150, 75, 0), [
        0, height - floor, width, floor], 0)

    return circle, pipe_up, pipe_dw


pg.init()

# window confi
width = 500
height = 700
play_surface = pg.display.set_mode((width, height))
pg.display.set_caption('Flappy Ball with DIP')
fps = pg.time.Clock()

# var init
gravity = 1
speed = 0
radius = 30
jump = -30
floor = 40
gap = (radius * 2) * 2.5
pipe_width = 70
score = 0

player1 = 'NA'
player2 = 'NA'
player3 = 'NA'

font_30 = pg.font.SysFont(None, 30)
font_50 = pg.font.SysFont(None, 50)

# stage game
welcome = True
game = False
game_over = False

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            if welcome:
                welcome = False
                game = True
            speed += jump

    if welcome:
        # pipe inicial
        player_pos = [height/5, height/2]
        pipe_pos = int(width / 2)
        pipe_height = [200, 450]

        # draw game
        draw_game(play_surface, player_pos,
                  pipe_pos, pipe_height, pipe_width)

        # init messages
        text_title_u = font_50.render(
            'Flappy Ball', True, (0, 0, 0), None)
        play_surface.blit(
            text_title_u, (width / 2 - text_title_u.get_rect().width / 2, height / 10))
        text_title_b = font_30.render(
            'with Digital Image Processing', True, (100, 100, 100), None)
        play_surface.blit(
            text_title_b, (width / 2 - text_title_b.get_rect().width / 2, height / 10 + text_title_u.get_rect().height + 5))

    if game:
        # player physics
        speed += gravity
        if speed > 0:
            speed *= 0.95
        else:
            speed *= 0.8

        player_pos[1] += speed

        # pipe physics
        if pipe_pos >= -pipe_width:
            pass
            pipe_pos -= 10
        else:
            pipe_pos = 500
            pipe_height = pipe_random_height(gap, floor)
            score += 1

        # hit edges
        if player_pos[1] >= height - radius - floor:
            game = False
            game_over = True
            player_pos[1] = height - radius - floor
        elif player_pos[1] <= 0 + radius:
            speed = 0
            player_pos[1] = 0 + radius

        # draw game
        circle, pipe_up, pipe_dw = draw_game(play_surface, player_pos,
                                             pipe_pos, pipe_height, pipe_width)

        # score message
        text_score = font_50.render(
            str(score), True, (0, 0, 0), None)
        play_surface.blit(
            text_score, (width / 2 - text_score.get_rect().width / 2, height/5))

        # hit pipe
        if circle.colliderect(pipe_dw) or circle.colliderect(pipe_up):
            game = False
            game_over = True

    if game_over:
        mx, my = pg.mouse.get_pos()
        # draw dead player
        draw_game(play_surface, player_pos, pipe_pos, pipe_height, pipe_width)
        pg.draw.circle(play_surface, (255, 0, 0),
                       (int(player_pos[0]), int(player_pos[1])), radius)
        pg.draw.circle(play_surface, (175, 175, 175), (mx, my), radius)
        pg.draw.circle(play_surface, (0, 0, 0),
                       (int(width / 2), int(height / 2)), radius, 1)

        # finish messages
        text_title_u = font_50.render(
            'Score: ' + str(score), True, (0, 0, 0), None)
        play_surface.blit(
            text_title_u, (width / 2 - text_title_u.get_rect().width / 2, height / 10))
        text_title_1 = font_30.render(
            '1st ' + player1, True, (100, 100, 100), None)
        play_surface.blit(
            text_title_1, (width / 2 - text_title_1.get_rect().width / 2, height / 10 + 45))
        text_title_2 = font_30.render(
            '2nd ' + player2, True, (100, 100, 100), None)
        play_surface.blit(
            text_title_2, (width / 2 - text_title_2.get_rect().width / 2, height / 10 + 45 + 21))
        text_title_3 = font_30.render(
            '3rd ' + player3, True, (100, 100, 100), None)
        play_surface.blit(
            text_title_3, (width / 2 - text_title_3.get_rect().width / 2, height / 10 + 45 + 2*21))

        if m.hypot(mx - width / 2, my - height / 2) <= 5:
            welcome = True
            game_over = False
            score = 0
            speed = 0

    pg.display.flip()
    fps.tick(30)

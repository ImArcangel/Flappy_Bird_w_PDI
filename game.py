import pygame
import sys
import time
import random
from pygame.locals import *


def pipe_random_height(gap, floor):
    a = random.randint(100, height - gap - floor - 100)
    pipe_h = [a, a + gap + random.randint(0, 3) * 20]
    return pipe_h


pygame.init()


def welcome_window(play_surface, fps, player_pos):
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                run = False

        # background
        play_surface.fill((151, 203, 255))

        # init messages

        # draw player
        pygame.draw.circle(play_surface, (255, 244, 79),
                           (int(player_pos[0]), int(player_pos[1])), radius)

        # draw floor
        pygame.draw.rect(play_surface, (150, 75, 0), [
                         0, height - floor, width, floor], 0)

        pygame.display.flip()
        fps.tick(30)


# window confi
width = 500
height = 700
play_surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Flappy Bird with PDI')
fps = pygame.time.Clock()

# var init
player_pos = [height/5, height/2]
gravity = 1
speed = 0
radius = 30
jump = -30
floor = 40
gap = (radius * 2) * 2.5
pipe_width = 70
score = 0

welcome_window(play_surface, fps, player_pos)

# pipe inicial
pipe_pos = 500
pipe_height = pipe_random_height(gap, floor)

font_30 = pygame.font.SysFont(None, 30)
font_50 = pygame.font.SysFont(None, 50)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                speed += jump

    # background
    play_surface.fill((151, 203, 255))

    # score message
    text_score = font_50.render(
        str(score), True, (0, 0, 0), (151, 203, 255))
    play_surface.blit(
        text_score, (width / 2 - text_score.get_rect().width / 2, height/5))

    # player physics
    speed += gravity
    if speed > 0:
        speed *= 0.95
    else:
        speed *= 0.8

    player_pos[1] += speed

    # pipe physics
    if pipe_pos >= -pipe_width:
        pipe_pos -= 10
    else:
        pipe_pos = 500
        pipe_height = pipe_random_height(gap, floor)
        score += 1

    # draw player
    pygame.draw.circle(play_surface, (255, 244, 79),
                       (int(player_pos[0]), int(player_pos[1])), radius)

    # draw pipe
    pygame.draw.rect(play_surface, (26, 148, 49), [
                     pipe_pos, 0, pipe_width, pipe_height[0]], 0)
    pygame.draw.rect(play_surface, (26, 148, 49), [
                     pipe_pos, pipe_height[1], pipe_width, 700], 0)

    # draw floor
    pygame.draw.rect(play_surface, (150, 75, 0), [
                     0, height - floor, width, floor], 0)

    # hit edges
    if player_pos[1] >= height - radius - floor:
        speed = 0
        player_pos[1] = height - radius - floor
    elif player_pos[1] <= 0 + radius:
        speed = 0
        player_pos[1] = 0 + radius

    # hit pipe
    if player_pos[1] - 20 <= pipe_height[0] or player_pos[1] + 20 >= pipe_height[1]:
        if player_pos[0] + 20 in list(range(pipe_pos, pipe_pos + pipe_width)) \
                or player_pos[0] - 20 in list(range(pipe_pos, pipe_pos + pipe_width)):
            print(f'Game over. Score {score}')

    pygame.display.flip()
    fps.tick(30)


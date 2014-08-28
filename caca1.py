bif = "ball.png"
bgif = "bg.jpg"

import pygame, sys
from pygame.locals import *
pygame.init()

randomColor = [100, 240, 160]
color = randomColor

size = [600, 400]

move = [0, 0]
pos = [0, 0]
speed = 0.5

screen = pygame.display.set_mode(size)

bg = pygame.image.load(bgif).convert()
ball = pygame.image.load(bif).convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_w:
                move[1] -= speed
            elif event.key == K_a:
                move[0] -= speed
            elif event.key == K_s:
                move[1] += speed
            elif event.key == K_d:
                move[0] += speed
        elif event.type == KEYUP:
            if event.key == K_w:
                move[1] = 0
            elif event.key == K_a:
                move[0] = 0
            elif event.key == K_s:
                move[1] = 0
            elif event.key == K_d:
                move[0] = 0

    pos[0] += move[0]
    pos[1] += move[1]

    screen.blit(bg, (0, 0))
    screen.blit(ball, pos)

    pygame.display.update()
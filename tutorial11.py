import pygame, sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((500, 500), 0, 32)

points = []

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            points.append(event.pos)

    if len(points) > 1:
        pygame.draw.lines(screen, (100, 240, 160), False, points)

        points.pop()
        points.pop()
    pygame.display.update()
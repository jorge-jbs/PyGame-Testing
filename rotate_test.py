import os
import sys
import math
import pygame

import pygame
from pygame.locals import *

SCREEN_SIZE = [720, 480]
FPS = 60

# Initialize screen
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Rotation test")
clock = pygame.time.Clock()

def main():
    cs = 0
    #points = [[0, 0], [0, cs], [cs, cs], [cs, 0]]
    points = [[cs, 0], [cs*2, cs*3], [cs, cs*2], [0, cs*3]]

    for i in range(len(points)):
        points[i][0] += 100
        points[i][1] += 100

    angle = int(sys.argv[1]) * (math.pi/180)
    new_points = []
    for i in points:
        new_points.append([0, 0])

    for i in range(len(points)):
        points[i][0] = points[i][0] - 150
        points[i][1] = points[i][1] - 150

        new_points[i][0] = points[i][0] * math.cos(angle)  -  points[i][1] * math.sin(angle)
        new_points[i][1] = points[i][1] * math.cos(angle)  +  points[i][0] * math.sin(angle)

        points[i][0] = new_points[i][0]
        points[i][1] = new_points[i][1]

        points[i][0] = points[i][0] + 150
        points[i][1] = points[i][1] + 150

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return 0

        pygame.draw.polygon(screen, (255, 255, 255), points)


if __name__ == "__main__": main(); sys.exit(0)

import os
import sys
import math
import random

import pygame
from pygame.locals import *

SCREEN_SIZE = [720, 480]
FPS = 60
#print(FPS)

# Initialize screen
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Juego en PyGame to guapo")
clock = pygame.time.Clock()

class Background(pygame.sprite.Sprite):
    """The randomly created background
    Returns: background object
    """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # Create image and rect variables, needed for the group
        self.image = pygame.Surface(SCREEN_SIZE)
        self.rect = self.image.get_rect()

        # Draw the stars into the background
        self.star_rate = 0.0025
        self.star_points = int((SCREEN_SIZE[0]*SCREEN_SIZE[1]) * self.star_rate)
        for i in range(self.star_points):
            pos = [random.randrange(SCREEN_SIZE[0]),
                   random.randrange(SCREEN_SIZE[1])]
            pygame.draw.line(self.image, (255, 255, 255), pos, pos)

background = Background()


class Ship(pygame.sprite.Sprite):
    def __init__(self):
        # Initialize the sprite and create general variables
        pygame.sprite.Sprite.__init__(self)
        self.cs = 10  # (Cube Size) this is used for changing the size of the ship
        self.size = (self.cs*3*2, self.cs*3*2)

        # Create image and rect variables, needed for the group
        self.image = pygame.Surface(self.size, flags=SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2)

        # Variables with different kinds of models of the ship
        self.model = ((self.cs, 0), (self.cs*2, self.cs*3), (self.cs, self.cs*2), (0, self.cs*3))  # Model of the ship in a tuple (only for reference)
        self.points = []  # Model of the ship in a list (this is the one that changes)
        self.centered_model = []  # Model of the default ship located at (0, 0)
        for i in self.model:
            self.points.append(list(i))
            self.centered_model.append([0, 0])

        for i in range(len(self.points)):
            self.centered_model[i][0] = self.model[i][0] - self.model[2][0]
            self.centered_model[i][1] = self.model[i][1] - self.model[2][1]

        # Movement and rotation
        #self.move_velocity = 500 / FPS
        self.move_velocity = 100 / FPS
        self.change_xy = 0
        self.change_x_p = 0  # Positive x
        self.change_x_n = 0  # Negative x
        self.change_y_p = 0  # Positive y
        self.change_y_n = 0  # Negative y

        self.angle = 0  # TODO: It would be nice to make this radians right away, instead of degrees. We'll keep it like this for now.
        self.rotation_velocity = 400 / FPS
        self.change_angle_p = 0
        self.change_angle_n = 0

    def update(self):

        # Increment/decrease angle
        self.angle += self.change_angle_p - self.change_angle_n

        # Rotate the ship
        radians = self.angle * (math.pi/180)
        for i in range(len(self.points)):
            self.points[i][0] = self.centered_model[i][0] * math.cos(radians)  -  self.centered_model[i][1] * math.sin(radians)
            self.points[i][1] = self.centered_model[i][1] * math.cos(radians)  +  self.centered_model[i][0] * math.sin(radians)

            self.points[i][0] = self.points[i][0] + self.size[0]/2
            self.points[i][1] = self.points[i][1] + self.size[1]/2

        # Move the ship.  TODO: move it with angle
#       self.rect.centerx += self.change_x_p - self.change_x_n
#       self.rect.centery += self.change_y_p - self.change_y_n

        self.rect.centerx += math.cos(radians-(math.pi/2)) * self.change_xy
        self.rect.centery += math.sin(radians-(math.pi/2)) * self.change_xy

        # Draw the ship with variables changed
        self.image = pygame.Surface(self.size, flags=SRCALPHA)
        pygame.draw.polygon(self.image, (255, 255, 255), self.points)

ship = Ship()


# Group that contains the sprites needed for the game.
game = pygame.sprite.OrderedUpdates()
game.add(background)
game.add(ship)

# Group that contains the sprites needed for the main meny.
menu = pygame.sprite.Group()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                # Movement
                if event.key == K_w:
                    #ship.change_y_n = ship.move_velocity
                    ship.change_xy += ship.move_velocity
                elif event.key == K_s:
                    #ship.change_y_p = ship.move_velocity
                    ship.change_xy -= ship.move_velocity
                # Rotation
                elif event.key == K_a:
                    ship.change_angle_n = ship.rotation_velocity
                elif event.key == K_d:
                    ship.change_angle_p = ship.rotation_velocity
                # Exiting
                elif event.key == K_ESCAPE:
                    return 0

            if event.type == KEYUP:
                # Movement
#               if event.key == K_w:
#                   ship.change_y_n = 0
#               elif event.key == K_s:
#                   ship.change_y_p = 0
                # Rotation
                if event.key == K_a:
                    ship.change_angle_n = 0
                elif event.key == K_d:
                    ship.change_angle_p = 0

            elif event.type == QUIT:
                return 0

        game.update()
        game.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    exit = main()
    sys.exit(exit)

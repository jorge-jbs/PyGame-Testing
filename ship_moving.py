import os
import sys
import random

import pygame
from pygame.locals import *

SCREEN_SIZE = [720, 480]
FPS = 60
print(FPS)

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
        self.star_points = int((SCREEN_SIZE[0] * SCREEN_SIZE[1]) * self.star_rate)
        for i in range(self.star_points):
            pos = [random.randrange(SCREEN_SIZE[0]),
                   random.randrange(SCREEN_SIZE[1])]
            pygame.draw.line(self.image, (255, 255, 255), pos, pos)

background = Background()


class Ship(pygame.sprite.Sprite):
    def __init__(self):
        # Initialize the sprite
        pygame.sprite.Sprite.__init__(self)
        cs = 10  # (Cube Size) this is used for changing the size of the ship

        # Create image and rect variables, needed for the group
        self.image = pygame.Surface((cs*2, cs*3), flags=SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2)

        # Draw the ship
        points = [[cs, 0], [cs*2, cs*3], [cs, cs*2], [0, cs*3]]
        pygame.draw.polygon(self.image, (255, 255, 255), points)

        # Movement
        self.move_velocity = 500 / FPS
        self.velocity_x_p = 0  # Positive x
        self.velocity_x_n = 0  # Negative x
        self.velocity_y_p = 0  # Positive y
        self.velocity_y_n = 0  # Negative y

    def update(self):
        ship.rect.centerx += ship.velocity_x_p - ship.velocity_x_n
        ship.rect.centery += ship.velocity_y_p - ship.velocity_y_n


ship = Ship()


# Group that contains the sprites needed for the game.
game = pygame.sprite.Group(background)
ship_ = pygame.sprite.Group(ship)

# Group that contains the sprites needed for the main meny.
menu = pygame.sprite.Group()

def main():
    # Event loop
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_w:
                    ship.velocity_y_n = ship.move_velocity
                elif event.key == K_a:
                    ship.velocity_x_n = ship.move_velocity
                elif event.key == K_s:
                    ship.velocity_y_p = ship.move_velocity
                elif event.key == K_d:
                    ship.velocity_x_p = ship.move_velocity
                elif event.key == K_ESCAPE:
                    return 0

            if event.type == KEYUP:
                if event.key == K_w:
                    ship.velocity_y_n = 0
                elif event.key == K_a:
                    ship.velocity_x_n = 0
                elif event.key == K_s:
                    ship.velocity_y_p = 0
                elif event.key == K_d:
                    ship.velocity_x_p = 0

            elif event.type == QUIT:
                return 0

#       ship.rect = ship.rect.move(ship.movex, ship.movey)
        ship_.update()
        game.draw(screen)
        ship_.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    exit = main()
    sys.exit(exit)

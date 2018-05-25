import pygame
from games.adventure.colors import *


class Wall(object):

    def __init__(self, pos, brick_size):
        self.rect = pygame.Rect(pos[0], pos[1], brick_size, brick_size)


class Chambers:

    def __init__(self, display, screen, brick_size):
        self._display = display
        self._screen = screen
        self._brick_size = brick_size

    def create_chamber1(self):
       schema = [
           "WWWW  WWWW",
           "W        W",
           "W        W",
           "W        W",
           "W        W",
           "W        W",
           "W        W",
           "W        W",
           "W        W",
           "WWWW  WWWW",
       ]
       self.create_any_chamber(schema, BLUE)

    def create_chamber2(self):
        schema = [
            "WWWW  WWWW",
            "W        W",
            "W        W",
            "W        W",
            "W        W",
            "W     W  W",
            "W     WWWW",
            "W        W",
            "W        W",
            "WWWW  WWWW",
        ]
        self.create_any_chamber(schema, RED)

    def create_any_chamber(self, chamber_schema, color):
        x = y = 0
        for row in chamber_schema:
            for col in row:
                if col == "W":
                    wall = Wall((x, y), brick_size=self._brick_size)
                    pygame.draw.rect(self._screen, color, wall.rect)
                x += self._brick_size
            y += self._brick_size
            x = 0
        self._display.update()

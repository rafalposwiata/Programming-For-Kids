import pygame
from games.adventure.chambers import Chambers


class Game:

    def __init__(self, screen_size=600, level=1):
        pygame.init()
        self._display = pygame.display
        self._screen = self._display.set_mode((screen_size, screen_size))
        self._running = True
        self._chambers = Chambers(self._display, self._screen, screen_size / 10)
        self._level = level

    def event_handle(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def draw(self):
        if self._level == 1:
            self._chambers.create_chamber1()
        else:
            self._chambers.create_chamber2()

    def start(self):
        while self._running:
            for event in pygame.event.get():
                self.event_handle(event)
            self.draw()
        self.quit()

    @staticmethod
    def quit():
        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.start()

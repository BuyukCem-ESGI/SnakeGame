import pygame
from global_var import WINDOW_WIDTH, WINDOW_HEIGHT


class window:
    def __init__(self):
        pygame.init()

        self._window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Pygame")
        self.clear_window()

    def get_window(self):
        return self._window

    def set_window(self, window):
        self._window = window

    def clear_window(self):
        self._window.fill(pygame.Color('black'))

    window = property(get_window, set_window)

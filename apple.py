import random
import pygame

from global_var import WINDOW_WIDTH, WINDOW_HEIGHT, GRID_SIZE

class apple:
    def __init__(self):
        self._color = (255, 0, 0)
        self._position_x = 0
        self._position_y = 0
        self.random_position()
        self.apple_size = GRID_SIZE

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    def get_position_x(self):
        return self._position_x

    def set_position_x(self, position_x):
        self._position_x = position_x

    def get_position_y(self):
        return self._position_y

    def set_position_y(self, position_y):
        self._position_y = position_y

    def random_position(self):
        self._position_x = random.randrange(110, 690, GRID_SIZE)
        self._position_y = random.randrange(110, 690, GRID_SIZE)

    def draw(self, window):
        pygame.draw.rect(window,
                         self.color,
                         (self.position_x, self.position_y, self.apple_size,
                          self.apple_size))


    color = property(get_color, set_color)
    position_x = property(get_position_x, set_position_x)
    position_y = property(get_position_y, set_position_y)

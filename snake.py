import pygame

class snake:
    def __init__(self):
        self._position_x = 300
        self._position_y = 300

        self._direction_x = 0
        self._direction_y = 0

        self._snake_body = 10
        self.snake_size = 1
        self.position_snake = []
        self.snake_color = (0, 255, 0)

    def get_position_x(self):
        return self._position_x

    def set_position_x(self, position_x):
        self._position_x = position_x

    def get_position_y(self):
        return self._position_y

    def set_positition_y(self, position_y):
        self._position_y = position_y

    def get_direction_x(self):
        return self._direction_x

    def set_direction_x(self, direction_x):
        self._direction_x = direction_x

    def get_direction_y(self):
        return self._direction_y

    def set_direction_y(self, direction_y):
        self._direction_y = direction_y

    def get_snake_body(self):
        return self._snake_body

    def set_snake_body(self, snake_body):
        self._snake_body = snake_body

    def change_direction(self, direction):
        if direction == 'up':
            print('up')
            self._direction_y = -10
            self._direction_x = 0
        elif direction == 'down':
            print('down')
            self._direction_y = 10
            self._direction_x = 0
        elif direction == 'left':
            print('left')
            self._direction_x = -10
            self._direction_y = 0
        elif direction == 'right':
            print('right')
            self._direction_x = 10
            self._direction_y = 0

    def move(self):
        self._position_x += self._direction_x
        self._position_y += self._direction_y

    def check_eat(self, apple):
        if (self.position_x == apple.position_x) and (self.position_y == apple.position_y):
            self.snake_size += 1
            apple.random_position()

    def draw(self, screen, *args):
        if len(args) == 2:
            pygame.draw.rect(screen,
                         self.snake_color,
                         (args[0], args[1], self.snake_body, self.snake_body))
        elif len(args) == 0:
            pygame.draw.rect(screen,
                             self.snake_color,
                             (self.position_x, self.position_y, self.snake_body,
                              self.snake_body))

    direction_x = property(get_direction_x, set_direction_x)
    direction_y = property(get_direction_y, set_direction_y)

    position_x = property(get_position_x, set_position_x)
    position_y = property(get_position_y, set_positition_y)

    snake_body = property(get_snake_body, set_snake_body)

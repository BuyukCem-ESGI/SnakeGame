import pygame
import random
from global_var import WINDOW_WIDTH, WINDOW_HEIGHT, GRID_SIZE

class snake:
    def __init__(self, color):
        self._position_x = random.randrange(110, 690, GRID_SIZE)
        self._position_y = random.randrange(110, 690, GRID_SIZE)

        self._direction_x = 0
        self._direction_y = 0

        self._snake_body = 10
        self.snake_size = 1
        self.position_snake = []


        self.snake_color = pygame.Color(color)

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
            self._direction_y = -10
            self._direction_x = 0
        elif direction == 'down':
            self._direction_y = 10
            self._direction_x = 0
        elif direction == 'left':
            self._direction_x = -10
            self._direction_y = 0
        elif direction == 'right':
            self._direction_x = 10
            self._direction_y = 0

    def move(self):
        self._position_x += self._direction_x
        self._position_y += self._direction_y

    def check_eat(self, apple):
        if (self.position_x == apple.position_x) and (self.position_y == apple.position_y):
            self.snake_size += 1
            apple.random_position()

    def add_position_snake(self):  # add snake head into body
        self.position_snake.append([self.position_x, self.position_y])

    def check_collision(self):
        if (self.position_x < 0) or (self.position_x > WINDOW_WIDTH):
            return True
        elif (self.position_y < 0) or (self.position_y > WINDOW_HEIGHT):
            return True
        else:
            for position in self.position_snake[:-1]:
                if position[0] == self.position_x and position[1] == self.position_y:
                    return True
            for position in self.position_snake[:-1]:
                if position == [self.position_x, self.position_y]:
                   return True
        return False

    def check_collision_friend(self,snake):
        for position in snake.position_snake:
            if position == [self.position_x, self.position_y]:
                return True

    def draw(self, screen):
        # si la position est supperieur a 1 alors on supprime le premier element
        if len(self.position_snake) > self.snake_size:
            self.position_snake.pop(0)

        for snake_part in self.position_snake[:-1]:
            pygame.draw.rect(screen,
                             self.snake_color,
                             (snake_part[0], snake_part[1], self.snake_body, self.snake_body))
        pygame.draw.rect(screen,
                         self.snake_color,
                         (self.position_x, self.position_y, self.snake_body,
                          self.snake_body))

    direction_x = property(get_direction_x, set_direction_x)
    direction_y = property(get_direction_y, set_direction_y)

    position_x = property(get_position_x, set_position_x)
    position_y = property(get_position_y, set_positition_y)

    snake_body = property(get_snake_body, set_snake_body)

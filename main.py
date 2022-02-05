import sys
import pygame

from window import window
from snake import snake
from apple import apple
from global_var import FPS


def main_run():
    main_window = window()
    main_snake = snake()
    main_apple = apple()
    clock = pygame.time.Clock()

    while game_run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    main_snake.change_direction('right')
                if event.key == pygame.K_LEFT:
                    main_snake.change_direction('left')
                if event.key == pygame.K_UP:
                    main_snake.change_direction('up')
                if event.key == pygame.K_DOWN:
                    main_snake.change_direction('down')

        main_snake.move()
        main_snake.check_eat(main_apple)

        if main_snake.check_collision():
            sys.exit()
        main_snake.add_position_snake()

        main_window.clear_window()

        main_apple.draw(main_window.window)
        main_snake.draw(main_window.window)

        clock.tick(FPS)
        pygame.display.flip()

if __name__ == "__main__":
    game_run = True
    main_run()

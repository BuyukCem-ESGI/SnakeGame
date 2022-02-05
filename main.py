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

        # PASASER CE CODE DANS LA CLASSE SNAKE
        # snek_head = main_snake.snake_body[0]
        main_snake.position_snake.append([main_snake.position_x, main_snake.position_y])
        if len(main_snake.position_snake) > main_snake.snake_size:
            main_snake.position_snake.pop(0)
            #print(main_snake.position_x, main_snake.position_y)

        main_window.clear_window()

        main_apple.draw(main_window.window)
        main_snake.draw(main_window.window)
        for snake_part in main_snake.position_snake[:-1]:
            main_snake.draw(main_window.window, snake_part[0], snake_part[1])


        clock.tick(FPS)
        pygame.display.flip()

if __name__ == "__main__":
    WIDTH = 800
    HEIGHT = 600
    game_run = True
    main_run()

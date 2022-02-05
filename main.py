import sys
import pygame

from window import window
from snake import snake
from apple import apple
from Player import Player
from global_var import FPS, WINDOW_WIDTH, WINDOW_HEIGHT


def main_run():
    clock = pygame.time.Clock()
    game_run_status = False
    game_init = True
    listPlayer = []
    main_window = window()
    name = ""

    while game_init:
        text = main_window.font.render('Voulez-vous jouer à deux?', True, (0, 255, 0), (0, 0, 255))
        text2 = main_window.font.render('presse N ou Y ', True, (0, 255, 0), (0, 0, 255))

        textRect = text.get_rect()
        textRect2 = text2.get_rect()

        textRect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        textRect2.center = ((WINDOW_WIDTH // 2), (WINDOW_HEIGHT // 2) + 35)
        main_window.window.blit(text, textRect)
        main_window.window.blit(text2, textRect2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                print(event.key)
                key = pygame.key.get_pressed()
                if key[pygame.K_n]:
                    listPlayer.append((Player("Player1"), snake("GREEN")))
                    pygame.event.clear()
                    game_init = False
                    game_run_status = False
                    insert_name_status = True
                    break

                if key[pygame.K_y]:
                    listPlayer.append((Player(), snake("GREEN")))
                    listPlayer.append((Player(), snake("BLUE")))
                    pygame.event.clear()
                    game_init = False
                    game_run_status = False
                    insert_name_status = True
                    main_window.clear_window()
                    break
            pygame.display.flip()
    i = 0
    while insert_name_status and i < len(listPlayer):
        text = main_window.font.render('Entrer le nom du player {}'.format(i+1), True, (0, 255, 0), (0, 0, 255))
        textRect = text.get_rect()
        textRect.center = ((WINDOW_WIDTH // 2), ((WINDOW_HEIGHT // 2))-35)
        main_window.window.blit(text, textRect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    name += event.unicode
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif event.key == pygame.K_KP_ENTER:
                    listPlayer[i][0].name = name
                    name = ""
                    i += 1
                block = main_window.font.render(name, True, (0, 255, 0), (0, 0, 255))
                rect = block.get_rect()
                rect.center = ((WINDOW_WIDTH // 2), (WINDOW_HEIGHT // 2))
                main_window.window.blit(block, rect)

                print("hello")
                pygame.display.flip()



    main_apple = apple()
    while game_run_status:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    listPlayer[0][1].change_direction('right')
                if event.key == pygame.K_LEFT:
                    listPlayer[0][1].change_direction('left')
                if event.key == pygame.K_UP:
                    listPlayer[0][1].change_direction('up')
                if event.key == pygame.K_DOWN:
                    listPlayer[0][1].change_direction('down')
                if len(listPlayer) > 1:
                    if event.key == pygame.K_z:
                        listPlayer[1][1].change_direction('up')
                    if event.key == pygame.K_s:
                        listPlayer[1][1].change_direction('down')
                    if event.key == pygame.K_q:
                        listPlayer[1][1].change_direction('left')
                    if event.key == pygame.K_d:
                        listPlayer[1][1].change_direction('right')

        if len(listPlayer) > 1:
            listPlayer[0][1].move()
            listPlayer[1][1].move()

            listPlayer[0][1].check_eat(main_apple)
            listPlayer[1][1].check_eat(main_apple)

            if listPlayer[1][1].check_collision() or listPlayer[0][1].check_collision():
                sys.exit()

            listPlayer[1][1].add_position_snake()
            listPlayer[0][1].add_position_snake()
            main_window.clear_window()
            listPlayer[1][1].draw(main_window.window)
            listPlayer[0][1].draw(main_window.window)

        else:
            listPlayer[0][1].move()
            listPlayer[0][1].check_eat(main_apple)
            if listPlayer[0][1].check_collision():
                sys.exit()
            listPlayer[0][1].add_position_snake()
            main_window.clear_window()
            listPlayer[0][1].draw(main_window.window)

        main_apple.draw(main_window.window)

        clock.tick(FPS)
        pygame.display.flip()


if __name__ == "__main__":
    main_run()

import sys
import pygame
import csv

from window import window
from snake import snake
from apple import apple
from Player import Player
from global_var import FPS, WINDOW_WIDTH, WINDOW_HEIGHT

clock = pygame.time.Clock()
game_init = True
main_window = window()
listPlayer = []

def init_game():
    listPlayer.clear()
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
                key = pygame.key.get_pressed()
                if key[pygame.K_n]:
                    listPlayer.append((Player(), snake("GREEN")))
                    pygame.event.clear()
                    insert_name_status()
                    main_window.clear_window()
                    break

                if key[pygame.K_y]:
                    listPlayer.append((Player(), snake("GREEN")))
                    listPlayer.append((Player(), snake("BLUE")))
                    pygame.event.clear()
                    insert_name_status()
                    main_window.clear_window()
                    break
            pygame.display.flip()
    

def main_run():
    init_game()
def insert_name_status():
    main_window.clear_window()
    name= ""
    i = 0
    colors = {0:"verte",1:"bleue"}
    while insert_name_status and i < len(listPlayer):
        text3 = main_window.font.render('Entrer le nom du player {}; votre couleur est la {} '.format(i + 1,colors[i]), True, (0, 255, 0), (0, 0, 255))
        textRect3 = text3.get_rect()
        textRect3.center = ((WINDOW_WIDTH // 2), ((WINDOW_HEIGHT // 2)) - 35)
        main_window.window.blit(text3, textRect3)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.unicode.isalpha() or event.unicode.isdigit():
                    name += event.unicode
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                    main_window.clear_window()
                elif event.key == pygame.K_RETURN:
                    main_window.clear_window()
                    listPlayer[i][0].name = name
                    save_player(listPlayer[i][0])
                    name = ""
                    i += 1
            
            block = main_window.font.render(name, True, (0, 255, 0), (0, 0, 255))
            rect = block.get_rect()
            rect.center = ((WINDOW_WIDTH // 2), (WINDOW_HEIGHT // 2))
            main_window.window.blit(block, rect)
            pygame.display.flip()

            if (i == len(listPlayer)):
                id_screen()
def id_screen():
    main_window.clear_window()
    while True:
        main_window.clear_window()
        message ="GARDEZ VOS ID POUR VOS PROCHAINES CONNEXION"
        id_message = ""
        message2 = "APPUYEZ SUR LA TOUCHE A POUR DEMARER"
        for k,player in enumerate(listPlayer):
            id_message += " ||Name: %s | ID: %s"%(listPlayer[k][0].name,listPlayer[k][0].get_id())
        id_block = main_window.font.render(message, True, (0, 255, 0), (0, 0, 255))
        rect = id_block.get_rect()
        rect.center = ((WINDOW_WIDTH // 2), (WINDOW_HEIGHT // 2))

        id_message_bloc = main_window.font.render(id_message, True, (0, 255, 0), (0, 0, 255))
        id_message_rect = id_message_bloc.get_rect()
        id_message_rect.center = ((WINDOW_WIDTH // 2), ((WINDOW_HEIGHT // 2) + 30))

        id_block2 = main_window.font.render(message2, True, (0, 255, 0), (0, 0, 255))
        rect2 = id_block2.get_rect()
        rect2.center = ((WINDOW_WIDTH // 2), ((WINDOW_HEIGHT // 2) + 60))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.key == pygame.K_a:
                    game_play()
        main_window.window.blit(id_block, rect)
        main_window.window.blit(id_message_bloc, id_message_rect)
        main_window.window.blit(id_block2, rect2)
        pygame.display.flip()


def game_play():
    main_window.clear_window()
    main_apple = apple()
    while True:
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

            if listPlayer[1][1].check_collision() or listPlayer[1][1].check_collision_friend(listPlayer[0][1]):
                listPlayer[1][0].score = -1
                listPlayer[0][0].score = listPlayer[0][1].snake_size
                listPlayer[1][0].is_GameOver = True
                save_score(listPlayer[0][0])
            elif listPlayer[0][1].check_collision() or listPlayer[0][1].check_collision_friend(listPlayer[1][1]):
                listPlayer[0][0].score = -1
                listPlayer[0][0].is_GameOver = True
                listPlayer[1][0].score = listPlayer[1][1].snake_size
                save_score(listPlayer[1][0])
            if listPlayer[1][0].is_GameOver or listPlayer[0][0].is_GameOver:
                game_over_status()

            listPlayer[1][1].add_position_snake()
            listPlayer[0][1].add_position_snake()

            main_window.clear_window()
            listPlayer[1][1].draw(main_window.window)
            listPlayer[0][1].draw(main_window.window)

        else:
            listPlayer[0][1].move()
            listPlayer[0][1].check_eat(main_apple)
            if listPlayer[0][1].check_collision():
                listPlayer[0][0].score = -1
                listPlayer[0][0].is_GameOver = True
                listPlayer[0][0].score = listPlayer[0][1].snake_size
                save_score(listPlayer[0][0])
                game_over_status()

            listPlayer[0][1].add_position_snake()
            main_window.clear_window()
            listPlayer[0][1].draw(main_window.window)

        main_apple.draw(main_window.window)

        clock.tick(FPS)
        pygame.display.flip()

def game_over_status():
    main_window.clear_window()
    while True:
        main_window.clear_window()
        text_game_end = ""

        for key, val in enumerate(listPlayer):
            text_game_end += str(listPlayer[key][0])

        text = main_window.font.render(text_game_end, True, (0, 255, 0), (0, 0, 255))
        textRect = text.get_rect()
        textRect.center = ((WINDOW_WIDTH // 2), ((WINDOW_HEIGHT // 2) + 35))

        restarttext = main_window.font.render("APPUYEZ SUR LA TOUCHE R POUR REJOUER OU Q POUR QUITTER", True, (0, 255, 0), (0, 0, 255))
        restarttextRect = restarttext.get_rect()
        restarttextRect.center = ((WINDOW_WIDTH // 2), (WINDOW_HEIGHT // 2))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.key == pygame.K_r:
                    init_game()
                    main_window.clear_window()
                if event.key == pygame.K_q:
                    sys.exit()
        main_window.window.blit(text, textRect)
        main_window.window.blit(restarttext, restarttextRect)
        pygame.display.flip()

 


def save_player(player):
    data = [player.get_id(),player.name,player.score]
    a_file = open("score.csv", "r+") 	  	 				 	 						 
    lines = a_file.readlines()
    writer = csv.writer(a_file)
    if(len(lines) <= 0):
        writer.writerow(data)
    else:
        exist_ids = []
        values = {}
        for line in lines:
            array = line.split(',')
            exist_ids.append(array[0])
            values[array[0]] = array
        if player.name in exist_ids:
            p = values[player.name]
            player.set_id(p[0])
            player.name = p[1]
            player.score = p[2]
        else:
            writer.writerow(data)

def save_score(player):
    a_file = open("score.csv", "r+") 	 				 	 						 
    lines = list(csv.reader(a_file))
    for k,line in enumerate(lines):
        if int(player.get_id()) == int(line[0]):
            lines[k][2] = "%d"%(int(player.score) + int(line[2]))
    writer = csv.writer(open('score.csv', 'w'))
    writer.writerows(lines)


if __name__ == "__main__":
    main_run()

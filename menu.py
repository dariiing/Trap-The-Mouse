import math
import random
import sys
import pygame
from constants import *
from hexagon import draw_hexagon
from map import generate_hexagon_map, get_neighbors

exit_button_x = WIDTH - 350
exit_button_y = HEIGHT - 80
exit_button_width = 300
exit_button_height = 60

return_button_x = 50
return_button_y = HEIGHT - 80
return_button_width = 300
return_button_height = 60

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.font.init()


def draw_title_and_timer(surface, timer):
    title_font = pygame.font.Font("Design/MagicEnglish.ttf", 60)
    timer_font = pygame.font.Font(None, 40)

    title_text = title_font.render("Trap the Mouse", True, WHITE, PINK)
    timer_text = timer_font.render("Time: {:02}:{:05.2f}".format(int(timer // 60), timer % 60), True, WHITE, PINK)

    title_rect = title_text.get_rect(center=(WIDTH // 2, 30))
    timer_rect = timer_text.get_rect(center=(WIDTH // 2, 70))

    surface.blit(title_text, title_rect)
    surface.blit(timer_text, timer_rect)


def draw_button(x, y, width, height, text, action=None):
    shadow_color = (240, 180, 190)
    shadow_offset = 5
    pygame.draw.rect(win, shadow_color, (x + shadow_offset, y + shadow_offset, width, height), border_radius=10)

    pygame.draw.rect(win, LIGHT_PINK, (x, y, width, height), border_radius=10)
    pygame.draw.rect(win, PINK, (x, y, width, height), 2, border_radius=10)

    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=(x + width / 2, y + height / 2))
    win.blit(text_surface, text_rect)

    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()

    if x < mouse_x < x + width and y < mouse_y < y + height:
        if mouse_click[0] == 1 and action is not None:
            action()


def menu():
    pygame.display.set_caption("Trap the Mouse")
    clock = pygame.time.Clock()
    run = True

    original_image = pygame.image.load("Design/mickey_mouse.png")

    scaled_width = original_image.get_width() // 1.5
    scaled_height = original_image.get_height() // 1.5
    image = pygame.transform.scale(original_image, (scaled_width, scaled_height))

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        win.fill(PINK)

        draw_title_and_timer(win, 0)

        draw_button(50, 200, 300, 60, "Player vs Player", lambda: run_game("Trap the Mouse - PvP", 25, 15, 20))

        draw_button(50, 300, 300, 60, "Player vs AI (Easy)", lambda: run_game("Trap the Mouse - PvAI Easy", 25, 15, 20))

        draw_button(50, 400, 300, 60, "Player vs AI (Medium)",
                    lambda: run_game("Trap the Mouse - PvAI Medium", 25, 15, 20))

        draw_button(50, 500, 300, 60, "Player vs AI (Hard)", lambda: run_game("Trap the Mouse - PvAI Hard", 25, 15, 20))

        draw_button(50, 600, 300, 60, "Rules")

        image_rect = image.get_rect(center=(WIDTH - image.get_width() // 1.5, HEIGHT // 2))

        win.blit(image, image_rect)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()


def display_congratulations_screen():
    win.fill(PINK)
    title_font = pygame.font.Font("Design/MagicEnglish.ttf", 60)

    title_text = title_font.render("Trap the Mouse", True, WHITE, PINK)
    title_rect = title_text.get_rect(center=(WIDTH // 2, 30))
    win.blit(title_text, title_rect)

    congratulation_text = pygame.font.Font("Design/MagicEnglish.ttf", 60)
    congratulation_text = congratulation_text.render("Congratulations! You've won!", True, (255, 255, 255))
    text_rect = congratulation_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    draw_button(return_button_x, return_button_y, return_button_width, return_button_height, "Return to Main Menu",
                lambda: menu())

    draw_button(exit_button_x, exit_button_y, exit_button_width, exit_button_height, "Exit", lambda: sys.exit())

    win.blit(congratulation_text, text_rect)
    pygame.display.update()

    run = True
    clock = pygame.time.Clock()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if (
                        return_button_x < mouse_pos[0] < return_button_x + return_button_width
                        and return_button_y < mouse_pos[1] < return_button_y + return_button_height
                ):
                    menu()
                elif (
                        exit_button_x < mouse_pos[0] < exit_button_x + exit_button_width
                        and exit_button_y < mouse_pos[1] < exit_button_y + exit_button_height
                ):
                    sys.exit()

        clock.tick(60)


def run_game(game_title, hex_size, map_rows, map_cols):
    pygame.display.set_caption(game_title)
    clock = pygame.time.Clock()
    run = True

    win.fill(PINK)

    # creating the map
    hexagons = generate_hexagon_map(map_rows, map_cols, hex_size, WIDTH, HEIGHT)

    timer = 0

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for hexagon in hexagons:
                    if hexagon.x < mouse_pos[0] < hexagon.x + 3 * hex_size / 2 and \
                            hexagon.y < mouse_pos[1] < hexagon.y + math.sqrt(3) * hex_size:
                        if hexagon.color != (0, 0, 0):
                            hexagon.color = RED

                # switch the mouse to a random neighbour hexagon
                for hexagon in hexagons:
                    if hexagon.color == BLACK:
                        neighbors = get_neighbors(hexagons, hexagon, hex_size)
                        valid_neighbors = [neighbor for neighbor in neighbors if neighbor.color == WHITE]
                        print(len(valid_neighbors))
                        if valid_neighbors:
                            random_choice = random.choice(valid_neighbors)
                            random_choice.color = BLACK
                            hexagon.color = WHITE
                        else:
                            display_congratulations_screen()
                            run = False
                        break

                if (
                        exit_button_x < mouse_pos[0] < exit_button_x + exit_button_width
                        and exit_button_y < mouse_pos[1] < exit_button_y + exit_button_height
                ):
                    run = False

        for hexagon in hexagons:
            draw_hexagon(win, hexagon.x, hexagon.y, hex_size, hexagon.color, BLACK, 1)

        # BUTTONS SECTION

        draw_title_and_timer(win, timer)

        draw_button(return_button_x, return_button_y, return_button_width, return_button_height, "Return to Main Menu",
                    lambda: menu())

        draw_button(exit_button_x, exit_button_y, exit_button_width, exit_button_height, "Exit", lambda: sys.exit())

        pygame.display.update()
        clock.tick(60)
        timer += 1 / 60

    pygame.quit()

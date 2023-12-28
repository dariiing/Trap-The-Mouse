import math
import random
import sys
from constants import *
from hexagon import draw_hexagon
from map import generate_hexagon_map, get_neighbors
from menu_utils import draw_button, draw_title, draw_image, draw_player_turn

pygame.font.init()


def initialize_window():
    pygame.display.set_caption("Trap the Mouse")


def draw_menu_buttons():
    draw_button(50, 200, 300, 60, "Player vs Player",
                lambda: run_player_vs_player("Trap the Mouse - PvP Mode", 25, 15, 20))
    draw_button(50, 300, 300, 60, "Player vs AI (Easy)",
                lambda: run_easy_game("Trap the Mouse - PvAI Easy", 25, 15, 20))
    draw_button(50, 400, 300, 60, "Player vs AI (Medium)", lambda: None)
    draw_button(50, 500, 300, 60, "Player vs AI (Hard)", lambda: None)
    draw_button(50, 600, 300, 60, "Rules", lambda: display_rules_screen())


def menu():
    initialize_window()
    clock = pygame.time.Clock()
    run = True
    original_image = pygame.image.load("Design/mickey_mouse.png")

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        win.fill(PINK)
        draw_title()
        draw_menu_buttons()
        draw_image(original_image)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()


def display_screen(message):
    win.fill(PINK)
    title_font = pygame.font.Font("Design/MagicEnglish.ttf", 60)

    title_text = title_font.render("Trap the Mouse", True, WHITE, PINK)
    title_rect = title_text.get_rect(center=(WIDTH // 2, 30))
    win.blit(title_text, title_rect)

    text = pygame.font.Font("Design/MagicEnglish.ttf", 60)
    text = text.render(message, True, (255, 255, 255))
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    draw_game_buttons()

    win.blit(text, text_rect)
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
                        RETURN_BUTTON["x"] < mouse_pos[0] < RETURN_BUTTON["x"] + RETURN_BUTTON["width"]
                        and RETURN_BUTTON["y"] < mouse_pos[1] < RETURN_BUTTON["y"] + RETURN_BUTTON["height"]
                ):
                    menu()
                elif (
                        EXIT_BUTTON["x"] < mouse_pos[0] < EXIT_BUTTON["x"] + EXIT_BUTTON["width"]
                        and EXIT_BUTTON["y"] < mouse_pos[1] < EXIT_BUTTON["y"] + EXIT_BUTTON["height"]
                ):
                    sys.exit()

        clock.tick(60)


def display_congratulations_screen():
    display_screen("Congratulations! You've won!")


def display_game_over_screen():
    display_screen("Game Over! You lost!")


def display_player1_screen():
    display_screen("Congratulations! Player 1 won!")


def display_player2_screen():
    display_screen("Congratulations! Player 2 won!")


def display_rules_screen():
    win.fill(PINK)
    title_font = pygame.font.Font("Design/MagicEnglish.ttf", 60)

    title_text = title_font.render("Game Rules", True, WHITE, PINK)
    title_rect = title_text.get_rect(center=(WIDTH // 2, 30))
    win.blit(title_text, title_rect)

    rules_text_lines = [
        "Trap the mouse by surrounding it with obstacles",
        "Click on a white hexagon to make an obstacle",
        "The mouse will then move to an empty neighbor",
        "Trap the mouse in as few moves as possible!",
        "Good luck!"
    ]

    text_font = pygame.font.Font("Design/MagicEnglish.ttf", 30)

    y_position = HEIGHT // 2 - 100

    for line in rules_text_lines:
        text = text_font.render(line, True, (255, 255, 255))
        text_rect = text.get_rect(center=(WIDTH // 2, y_position))
        win.blit(text, text_rect)
        y_position += 40

    draw_game_buttons()

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
                        RETURN_BUTTON["x"] < mouse_pos[0] < RETURN_BUTTON["x"] + RETURN_BUTTON["width"]
                        and RETURN_BUTTON["y"] < mouse_pos[1] < RETURN_BUTTON["y"] + RETURN_BUTTON["height"]
                ):
                    menu()
                elif (
                        EXIT_BUTTON["x"] < mouse_pos[0] < EXIT_BUTTON["x"] + EXIT_BUTTON["width"]
                        and EXIT_BUTTON["y"] < mouse_pos[1] < EXIT_BUTTON["y"] + EXIT_BUTTON["height"]
                ):
                    sys.exit()

        clock.tick(60)


def init_game(game_title, hex_size, map_rows, map_cols):
    pygame.display.set_caption(game_title)
    clock = pygame.time.Clock()
    run = True
    win.fill(PINK)

    # creating the map
    hexagons, start_x, total_width = generate_hexagon_map(map_rows, map_cols, hex_size, WIDTH, HEIGHT)

    return hexagons, start_x, total_width, clock, run


def draw_game_buttons():
    draw_button(RETURN_BUTTON["x"], RETURN_BUTTON["y"], RETURN_BUTTON["width"], RETURN_BUTTON["height"],
                "Return to Main Menu", lambda: menu())
    draw_button(EXIT_BUTTON["x"], EXIT_BUTTON["y"], EXIT_BUTTON["width"], EXIT_BUTTON["height"], "Exit",
                lambda: sys.exit())


# easy game
def run_easy_game(game_title, hex_size, map_rows, map_cols):
    hexagons, start_x, total_width, clock, run = init_game(game_title, hex_size, map_rows, map_cols)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                valid_move = False

                for hexagon in hexagons:
                    if (
                            hexagon.x < mouse_pos[0] < hexagon.x + 3 * hex_size / 2
                            and hexagon.y < mouse_pos[1] < hexagon.y + math.sqrt(3) * hex_size
                    ):
                        if hexagon.color == WHITE:
                            hexagon.color = RED
                            valid_move = True
                        break

                if valid_move:
                    # switch the mouse to a random neighbor hexagon
                    for hexagon in hexagons:
                        if hexagon.color == BLACK:
                            if hexagon.x <= start_x or hexagon.x + 3 * hex_size / 2 >= start_x + total_width:
                                display_game_over_screen()
                                run = False
                                break
                            else:
                                neighbors = get_neighbors(hexagons, hexagon, hex_size)
                                valid_neighbors = [neighbor for neighbor in neighbors if neighbor.color == WHITE]
                                if valid_neighbors:
                                    random_choice = random.choice(valid_neighbors)
                                    random_choice.color = BLACK
                                    hexagon.color = WHITE
                                    break
                                else:
                                    display_congratulations_screen()
                                    run = False
                                    break

                if (
                        EXIT_BUTTON["x"] < mouse_pos[0] < EXIT_BUTTON["x"] + EXIT_BUTTON["width"]
                        and EXIT_BUTTON["y"] < mouse_pos[1] < EXIT_BUTTON["y"] + EXIT_BUTTON["height"]
                ):
                    run = False

        for hexagon in hexagons:
            draw_hexagon(win, hexagon.x, hexagon.y, hex_size, hexagon.color, BLACK, 1)

        draw_title()
        draw_game_buttons()

        pygame.display.update()
        clock.tick(60)

    pygame.quit()


# pvp game
def run_player_vs_player(game_title, hex_size, map_rows, map_cols):
    hexagons, start_x, total_width, clock, run = init_game(game_title, hex_size, map_rows, map_cols)

    player_turn = 1

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                valid_move = False

                for hexagon in hexagons:
                    if (
                            hexagon.x < mouse_pos[0] < hexagon.x + 3 * hex_size / 2
                            and hexagon.y < mouse_pos[1] < hexagon.y + math.sqrt(3) * hex_size
                    ):
                        if hexagon.color == WHITE:
                            if player_turn == 1:
                                hexagon.color = RED
                                valid_move = True
                            else:
                                neighbors = get_neighbors(hexagons, hexagon, hex_size)
                                valid_neighbors = [neighbor for neighbor in neighbors if neighbor.color == BLACK]
                                if valid_neighbors:
                                    hexagon.color = BLACK
                                    for neighbor in valid_neighbors:
                                        if neighbor.color == BLACK:
                                            neighbor.color = WHITE
                                    valid_move = True
                                else:
                                    valid_move = False
                        break

                for hexagon in hexagons:
                    if hexagon.color == BLACK:
                        neighbors = get_neighbors(hexagons, hexagon, hex_size)
                        new_neighbors = [neighbor for neighbor in neighbors if neighbor.color == WHITE]
                        if not new_neighbors:
                            display_player1_screen()
                            run = False
                            break
                        elif hexagon.x <= start_x or hexagon.x + 3 * hex_size / 2 >= start_x + total_width:
                            display_player2_screen()
                            run = False
                            break

                if valid_move:
                    player_turn = 3 - player_turn

                if (
                        EXIT_BUTTON["x"] < mouse_pos[0] < EXIT_BUTTON["x"] + EXIT_BUTTON["width"]
                        and EXIT_BUTTON["y"] < mouse_pos[1] < EXIT_BUTTON["y"] + EXIT_BUTTON["height"]
                ):
                    run = False

        for hexagon in hexagons:
            draw_hexagon(win, hexagon.x, hexagon.y, hex_size, hexagon.color, BLACK, 1)

        draw_player_turn(player_turn)
        draw_game_buttons()

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

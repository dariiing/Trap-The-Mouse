from constants import *


def draw_title():
    title_font = pygame.font.Font("Design/MagicEnglish.ttf", 60)
    title_text = title_font.render("Trap the Mouse", True, WHITE, PINK)
    title_rect = title_text.get_rect(center=(WIDTH // 2, 30))
    win.blit(title_text, title_rect)


def draw_player_turn(player_turn):
    draw_title()

    title_font_small = pygame.font.Font("Design/MagicEnglish.ttf", 40)
    title_text_small = title_font_small.render(f"Player {player_turn}'s Turn", True, WHITE, PINK)
    title_rect_small = title_text_small.get_rect(center=(WIDTH // 2, 80))
    win.blit(title_text_small, title_rect_small)


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


def draw_image(image):
    scaled_width = image.get_width() // 1.5
    scaled_height = image.get_height() // 1.5
    scaled_image = pygame.transform.scale(image, (scaled_width, scaled_height))
    image_rect = scaled_image.get_rect(center=(WIDTH - scaled_image.get_width() // 1.5, HEIGHT // 2))
    win.blit(scaled_image, image_rect)
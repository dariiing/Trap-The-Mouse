from constants import *


def draw_title():
    """
    Draws the title on the pygame window.

    This function renders the title "Trap the Mouse" with a specific font and color,
    and then blits it to the pygame window at a specified location.

    Returns:
    None
    """
    title_font = pygame.font.Font("Design/MagicEnglish.ttf", 60)
    title_text = title_font.render("Trap the Mouse", True, WHITE, PINK)
    title_rect = title_text.get_rect(center=(WIDTH // 2, 30))
    win.blit(title_text, title_rect)


def draw_player_turn(player_turn):
    """
    Draws the current player's turn on the pygame window.

    This function first calls the draw_title function to draw the title,
    and then renders the text indicating the current player's turn with a specific font and color.
    The text is then blitted to the pygame window at a specified location.

    Parameters:
    player_turn (int): The current player's turn.

    Returns:
    None
    """
    draw_title()

    title_font_small = pygame.font.Font("Design/MagicEnglish.ttf", 40)
    title_text_small = title_font_small.render(f"Player {player_turn}'s Turn", True, WHITE, PINK)
    title_rect_small = title_text_small.get_rect(center=(WIDTH // 2, 80))
    win.blit(title_text_small, title_rect_small)


def draw_button(x, y, width, height, text, action=None):
    """
    Draws a button on the pygame window.

    This function draws a button with a shadow, a border, and a text label.
    If the button is clicked and an action is provided, the action is executed.

    Parameters:
    x (int): The x-coordinate of the top left corner of the button.
    y (int): The y-coordinate of the top left corner of the button.
    width (int): The width of the button.
    height (int): The height of the button.
    text (str): The text label of the button.
    action (function, optional): The function to execute when the button is clicked. Defaults to None.

    Returns:
    None
    """
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
    """
    Draws an image on the pygame window.

    This function scales the provided image, creates a rectangle for the image,
    and then blits the image to the pygame window at a specified location.

    Parameters:
    image (pygame.Surface): The image to be drawn.

    Returns:
    None
    """
    scaled_width = image.get_width() // 1.5
    scaled_height = image.get_height() // 1.5
    scaled_image = pygame.transform.scale(image, (scaled_width, scaled_height))
    image_rect = scaled_image.get_rect(center=(WIDTH - scaled_image.get_width() // 1.5, HEIGHT // 2))
    win.blit(scaled_image, image_rect)


def handle_click(mouse_pos, run):
    """
    Handles a mouse click event.

    This function checks if the mouse click position is within the bounds of the exit button.
    If it is, the function sets the run variable to False, indicating that the game should stop running.

    Parameters:
    mouse_pos (tuple): The x and y coordinates of the mouse click.
    run (bool): A flag indicating whether the game is currently running.

    Returns:
    None
    """
    if (
            EXIT_BUTTON["x"] < mouse_pos[0] < EXIT_BUTTON["x"] + EXIT_BUTTON["width"]
            and EXIT_BUTTON["y"] < mouse_pos[1] < EXIT_BUTTON["y"] + EXIT_BUTTON["height"]
    ):
        run = False

from pygame.math import Vector2
import pygame


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREY = (150, 255, 255)
TRANSPARENT = (0, 0, 0, 255)


FONT_ARIAL = pygame.font.match_font('arial')


SCREEN_SIZE = Vector2(1920, 1050)
SCREEN_SIZE_DEFAULT = Vector2(1920, 1080)
#SCREEN_SIZE_RATIO = SCREEN_SIZE / SCREEN_SIZE_DEFAULT
SCREEN_SIZE1 = SCREEN_SIZE / 2
SCREEN_TITLE = "The Chicken Invaders by Daniel Warloch"

ICON_PATH = "Icon.png"

MENU_BACKGROUND_1 = "Resources/Backgrounds/CI5_1.jpg"
MENU_BACKGROUND_2 = "Resources/Backgrounds/CI5_2.jpg"
MENU_BACKGROUND_3 = "Resources/Backgrounds/CI5_3.jpg"
MENU_BACKGROUND_4 = "Resources/Backgrounds/CI5_4.jpg"
MENU_BACKGROUND_5 = "Resources/Backgrounds/CI5_5.jpg"


INTRO_MUSIC_VOLUME = 0.5
PLAYER_SHIP_DESIGN = "Resources/Ships/2.png"


def strip_from_sheet(sheet, start, size, columns, rows=1):
    """
    Strips individual frames from a sprite sheet given a start location,
    sprite size, and number of columns and rows.
    """
    frames = []
    for j in range(rows):
        for i in range(columns):
            location = (start[0]+size[0]*i, start[1]+size[1]*j)
            frames.append(sheet.subsurface(pygame.Rect(location, size)))
    return frames
def draw_group_index(surface, Group):
    for G in Group:
        surface.blit(G.image[G.index], G.rect.topleft)

def draw_text_TL(surface, text, Font, size, position):
    font = pygame.font.Font(Font, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.topleft = position

    surface.blit(text_surface, text_rect)
    pygame.display.update()
def draw_text_BL(surface, text, Font, size, position):
    font = pygame.font.Font(Font, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.bottomleft = position

    surface.blit(text_surface, text_rect)
    pygame.display.update()
def draw_text_C(surface, text, Font, size, position):
    font = pygame.font.Font(Font, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.center = position

    surface.blit(text_surface, text_rect)
    pygame.display.update()
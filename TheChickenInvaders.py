import pygame
from constants import *
from Menus import StartScreen

class TheChickenInvaders(object):
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(SCREEN_TITLE)
        pygame.display.set_icon(pygame.image.load(ICON_PATH))
        pygame.mixer.init()

        self.screen = pygame.display.set_mode([int(SCREEN_SIZE.x), int(SCREEN_SIZE.y)])

    def main(self):
        StartScreen(self.screen).intro()
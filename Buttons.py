import pygame
import sys

class Button(pygame.sprite.Sprite):
    def __init__(self, *group):
        super(Button, self).__init__(*group)
        self.index = 0
        self.choice = 0
        self.pointing = False
 
    def update(self, menu):
        try:
            if self.rect.right > menu.mouseX > self.rect.left and self.rect.y < menu.mouseY < self.rect.y + self.rect.height:
                self.index = 1
                self.pointing = True
            else:
                self.index = 0
                self.pointing = False
            self.image = self.images[self.index]
        except AttributeError:
            pass

    def getChoice(self):
        return self.choice

class PlayButton(Button):
    def __init__(self, x, y, *group):
        super(PlayButton, self).__init__(*group)
        self.images = [pygame.image.load("Resources/Menu/PLAY_OFF.png"),
                       pygame.image.load("Resources/Menu/PLAY_ON.png")]
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.choice = "Play"

class LearnButton(Button):
    def __init__(self, x, y, *group):
        super(LearnButton, self).__init__(*group)
        self.images = [pygame.image.load("Resources/Menu/TUTORIAL_OFF.png"),
                       pygame.image.load("Resources/Menu/TUTORIAL_ON.png")]
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.choice = "Learn"

class RankingButton(Button):
    def __init__(self, x, y, *group):
        super(RankingButton, self).__init__(*group)
        self.images = [pygame.image.load("Resources/Menu/RANKING_OFF.png"),
                       pygame.image.load("Resources/Menu/RANKING_ON.png")]
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.choice = "Ranking"

class QuitButton(Button):
    def __init__(self, x, y, *group):
        super(QuitButton, self).__init__(*group)
        self.images = [pygame.image.load("Resources/Menu/EXIT_OFF.png"),
                       pygame.image.load("Resources/Menu/EXIT_ON.png")]
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.choice = "Quit"
class OptionsButton(Button):
    def __init__(self, x, y, *group):
        super(OptionsButton, self).__init__(*group)
        self.images = [pygame.image.load("Resources/Menu/SETTINGS_OFF.png"),
                       pygame.image.load("Resources/Menu/SETTINGS_ON.png")]
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.choice = "Options"




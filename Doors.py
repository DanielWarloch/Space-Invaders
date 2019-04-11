import pygame
from constants import *

class UpperDoor(pygame.sprite.Sprite):
    def __init__(self, *group):
        super(UpperDoor, self).__init__(*group)
        self.image = pygame.image.load("Resources/Menu/upper.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = -self.rect.height - 10

        self.sound = pygame.mixer.Sound("Resources/Sounds/doorsound.wav")


    def playSound(self):
        self.sound.play()
        self.sound.fadeout(6000)


    def update(self, menu):
        self.rect.y += 15
        if self.rect.y + self.rect.height >= menu.lowerDoor.rect.y + 15:
            menu.done = True

class LowerDoor(pygame.sprite.Sprite):
    def __init__(self, *group):
        super(LowerDoor, self).__init__(*group)
        self.image = pygame.image.load("Resources/Menu/lower.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = SCREEN_SIZE.x + 10

    def playSound(self):
        pass

    def update(self, menu):
        self.rect.y -= 15

class SpecialUpperDoor(UpperDoor):
    def __init__(self, *group):
        super(SpecialUpperDoor, self).__init__(*group)
        self.rect.y = 350 - self.rect.height

    def update(self, menu):
        self.rect.y -= 20
        if self.rect.y + self.rect.height < 0 and menu.lowerDoor.rect.y > SCREEN_SIZE.x:
            menu.done = True

class SpecialLowerDoor(LowerDoor):
    def __init__(self, *group):
        super(SpecialLowerDoor, self).__init__(*group)
        self.rect.y = 350

    def update(self, menu):
        self.rect.y += 20
    

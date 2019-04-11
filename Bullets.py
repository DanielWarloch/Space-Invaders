import pygame
from pygame.math import Vector2
from constants import *
import random

class Bullet(pygame.sprite.Sprite):
    def __init__(self, position, rodzaj):
        pygame.sprite.Sprite.__init__(self)
        self.index = rodzaj
        self.speed = -30
        self.bullet_list = [pygame.image.load("Resources/Bullets/BoronRailgunWeak.png"),
                       pygame.image.load("Resources/Bullets/BoronRailgunMedium.png"),
                       pygame.image.load("Resources/Bullets/BoronRailgunStrong.png"),
                       pygame.image.load("Resources/Bullets/IonBlasterSingle.png"),
                       pygame.image.load("Resources/Bullets/IonBlasterDouble.png"),
                       pygame.image.load("Resources/Bullets/IonBlasterDouble - Copy.png"),
                       pygame.image.load("Resources/Bullets/UtensilPokerCarving.png"),
                       pygame.image.load("Resources/Bullets/UtensilPokerFork.png"),
                       pygame.image.load("Resources/Bullets/UtensilPokerFork - Copy.png"),
                       pygame.image.load("Resources/Bullets/VulcanChaingunWeak.png"),
                       pygame.image.load("Resources/Bullets/VulcanChaingunMedium.png"),
                       pygame.image.load("Resources/Bullets/VulcanChaingunStrong.png")]
        #self.size = Vector2(self.bullet_list[self.index].get_size)
        self.image = pygame.transform.scale(self.bullet_list[self.index], (20, 60))
        #self.image = pygame.transform.scale(self.bullet_list[self.index], (int(self.size.x / 5), int(self.size.y / 5)))
        self.rect = self.image.get_rect()
        self.rect.midbottom = position

    def update(self):
        self.rect.bottom += self.speed

        if self.rect.bottom < 0:
            self.kill()

class Egg(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)

        self.speed = 5
        self.bullet_list = pygame.image.load("Resources/Bullets/Regularegg.png")
        self.image = self.bullet_list
        #self.image = pygame.transform.scale(self.bullet_list, self.bullet_list.get_size() * SCREEN_SIZE_RATIO)

        self.rect = self.image.get_rect()
        self.rect.midbottom = position

    def update(self):
        self.rect.bottom += self.speed

        if self.rect.bottom > SCREEN_SIZE.y:
            self.kill()


class Power_ups(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10
        self.index = 0
        self.list = []
        for x in range(1, 25):
            self.list.append(pygame.image.load("Resources/Power-ups/Power_ups/atom/atom (" + str(x) + ").png"))



        self.image = pygame.transform.scale(self.list[self.index], (20, 60))

        self.rect = self.image.get_rect()
        self.rect.midbottom = position

    def update(self):
        self.rect.bottom += self.speed

        if self.rect.bottom > SCREEN_SIZE.y:
            self.kill()
        self.index += 1
        self.index = (self.index + 1) % 24
        self.image = self.list[self.index]
class Eat(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10
        self.list = [pygame.image.load("Resources/Power-ups/Eats/Corny1.png"),
                            pygame.image.load("Resources/Power-ups/Eats/CheeseBurger.png"),
                            pygame.image.load("Resources/Power-ups/Eats/CI3Leg.png"),
                            pygame.image.load("Resources/Power-ups/Eats/CI3Roast.png"),
                            pygame.image.load("Resources/Power-ups/Eats/Corny2.png"),
                            pygame.image.load("Resources/Power-ups/Eats/Pumpkin.png"),
                            pygame.image.load("Resources/Power-ups/Eats/PlainBurger.png"),
                            pygame.image.load("Resources/Power-ups/Eats/QuadBurger.png"),
                            pygame.image.load("Resources/Power-ups/Eats/TLCBurger.png"),
                            pygame.image.load("Resources/Power-ups/Eats/TomatoCheeseBurger.png"),
                            pygame.image.load("Resources/Power-ups/Eats/TripleBurger.png")]

        self.index = random.randint(0, len(self.list)-1)



        self.image = pygame.transform.scale(self.list[self.index], (20, 60))

        self.rect = self.image.get_rect()
        self.rect.midbottom = position

    def update(self):
        self.rect.bottom += self.speed

        if self.rect.bottom > SCREEN_SIZE.y:
            self.kill()
class Presents(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10
        self.list = []
        self.index = 0
        self.index1 = random.randint(0, 2)
        for x in range(1, 50):
            self.list.append(pygame.image.load("Resources/Power-ups/Gifts/" + str(self.index1) + "/present ("+ str(x) +").png"))



        self.image = pygame.transform.scale(self.list[self.index], (20, 60))

        self.rect = self.image.get_rect()
        self.rect.midbottom = position

    def update(self):
        self.rect.bottom += self.speed

        if self.rect.bottom > SCREEN_SIZE.y:
            self.kill()
        self.index += 1
        self.index = (self.index + 1) % 50
        self.image = self.list[self.index]
class Coins(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10
        self.list = [   pygame.image.load("Resources/Power-ups/Coins/CoinBrown.png"),
                        pygame.image.load("Resources/Power-ups/Coins/CoinGold.png"),
                        pygame.image.load("Resources/Power-ups/Coins/CoinSilver.png")]
        self.index = random.randint(0, len(self.list)-1)



        self.image = pygame.transform.scale(self.list[self.index], (20, 60))

        self.rect = self.image.get_rect()
        self.rect.midbottom = position

    def update(self):
        self.rect.bottom += self.speed

        if self.rect.bottom > SCREEN_SIZE.y:
            self.kill()
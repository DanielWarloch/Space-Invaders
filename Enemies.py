import pygame
import random
import Bullets
from constants import *
'''
from Hazards import *
from Deaths import *
'''
class Chicken(pygame.sprite.Sprite):
    id_counter = 0
    position_change = 0
    k: bool = False

    def __init__(self, position, level):
        pygame.sprite.Sprite.__init__(self)
        #super().__init__(self)
        self.id_counter += 1
        self.rozrzut_x = -60
        self.rozrzut_y = -40
        if random.randint(0, 100000) > 85000 + level * 2000:
            self.index = random.randint(1, 5)
        else:
            self.index = 0

        self.health = 100 * level + 200 * self.index


        self.image_list = [pygame.image.load("Resources/Enemies/Chickens/CI3Chicken.png"),
                      pygame.image.load("Resources/Enemies/Chickens/BalloonChicken.png"),
                      pygame.image.load("Resources/Enemies/Chickens/BigChicken.png"),
                      pygame.image.load("Resources/Enemies/Chickens/SweaterChicken.png"),
                      pygame.image.load("Resources/Enemies/Chickens/MotherHenShip.png"),
                      pygame.image.load("Resources/Enemies/Chickens/UFOCI3.png")]
        self.image = pygame.transform.scale(self.image_list[self.index], (128, 128))
        self.rect = self.image.get_rect()
        self.position_default = position
        self.rect.topright = position

    def hit(self, hit_power, list_of_powerups, list_of_eat,
                      list_of_presents, list_of_coins):
        self.health -= hit_power
        if self.health <= 0:
            if random.randint(0, 10000) < 8000:
                if random.randint(0, 10000) < 1000:
                    list_of_powerups.add(Bullets.Power_ups((self.rect.centerx + random.randint(self.rozrzut_x, -self.rozrzut_x), self.rect.centery + random.randint(self.rozrzut_y, -self.rozrzut_y))))
                if random.randint(0, 10000) < 6000:
                    list_of_eat.add(Bullets.Eat((self.rect.centerx + random.randint(self.rozrzut_x, -self.rozrzut_x), self.rect.centery + random.randint(self.rozrzut_y, -self.rozrzut_y))))
                if random.randint(0, 10000) < 1000:
                    list_of_presents.add(Bullets.Presents((self.rect.centerx + random.randint(self.rozrzut_x, -self.rozrzut_x), self.rect.centery + random.randint(self.rozrzut_y, -self.rozrzut_y))))
                if random.randint(0, 10000) < 4000:
                    list_of_coins.add(Bullets.Coins((self.rect.centerx + random.randint(self.rozrzut_x, -self.rozrzut_x), self.rect.centery + random.randint(self.rozrzut_y, -self.rozrzut_y))))
            self.kill()




    def update(self, list_of_eggs):
        if not self.k:
            self.position_change += 2
            if self.position_change >= 80:
                self.k = True
        if self.k:
            self.position_change -= 2
            if self.position_change <= -80:
                self.k = False
        self.rect.topleft = self.position_default
        self.rect.right += self.position_change
        if random.randint(0, 100000) < 100:
            list_of_eggs.add(Bullets.Egg(self.rect.midbottom))


        #self.screen.blit(self.image, self.rect, (0, 0, self.image[self.index].get_width(), self.image[self.index].get_height()))

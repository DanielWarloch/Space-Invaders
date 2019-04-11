import pygame
from pygame.math import Vector2
from constants import *
import Bullets

class Player(pygame.sprite.Sprite):
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.x      =   x
        self.clock  =   pygame.time.Clock()
        self.clock1  =   pygame.time.Clock()
        self.clock2  =   pygame.time.Clock()
        self.score = 0
        self.gun = 1
        self.power = 1
        self.lives  =   3
        self.player_name = "Player name"

        self.index  = 17

        self.image_list = pygame.image.load(PLAYER_SHIP_DESIGN)
        self.size = self.image_list.get_size()
        self.image_list = strip_from_sheet(self.image_list, (0, 0), (self.size[0]/31, self.size[1]), 31, 1)
        self.image = self.image_list[0]
        self.rect = self.image.get_rect()



        self.position_change = Vector2(2, 2)
        self.position_default = (SCREEN_SIZE.x / 2, SCREEN_SIZE.y * 0.85)
        self.rect.center = self.position_default
        self.vel = Vector2(0, 0)
        self.acc = Vector2(0, 0)

        self.overcheat = 0
        self.overcheat_limit = 8
        self.overcheat_t = 0.0
        self.shooting_value = True

        self.tps_delta = 0.0
        self.tps_delta_shooting = 0.0
        self.tps_max_shooting = 5
        self.tps_max = 150

    def update(self, list_of_bulets):
        self.tps_delta += self.clock.tick() / 1000.0

        while self.tps_delta > (1 / self.tps_max):
            self.tps_delta -= (1 / self.tps_max)
            self.position_correction()
        self.physics()
        self.shooting(list_of_bulets)
        self.image = self.image_list[self.index]

    def shooting(self, list_of_bulets):
        self.overcheat_t += self.clock2.tick() / 1000.0
        if self.shooting_value:
            if self.overcheat <= self.overcheat_limit:
                self.tps_delta_shooting += self.clock1.tick() / 1000.0
                if self.tps_delta_shooting > (1 / self.tps_max_shooting):
                    self.tps_delta_shooting = 0.0
                    if pygame.key.get_pressed()[pygame.K_SPACE]:
                        list_of_bulets.add(Bullets.Bullet(self.rect.midtop, self.gun))
                        self.addforce((0, 5))
                        self.overcheat += 1
            else:
                self.shooting_value = False
        if self.overcheat_t > 5 / 10:
            self.overcheat_t -= 5 / 10
            if self.overcheat > 0:
                self.overcheat -= 1
            else:
                self.shooting_value = True


    def power_ups(self):
        if self.power < 10:
            self.power += 1
    def eat(self):
        self.score += 200
    def presents(self):
        if self.gun < 11:
            self.gun += 1
        else:
            self.gun = 0
    def coins(self):
        self.score += 1000

    def death(self):
        self.lives -= 1
        if self.lives >= 1:
            self.rect.center = self.position_default
        else:
            self.x.GameExit = True

    def position_correction(self):

        self.keys_pressed = pygame.key.get_pressed()
        if self.rect.left > 10:
            if self.keys_pressed[pygame.K_LEFT]:
                self.addforce(Vector2(-self.position_change.x, 0))
        else:
            self.rect.left = 10
        if self.rect.right < SCREEN_SIZE.x - 10:
            if self.keys_pressed[pygame.K_RIGHT]:
                self.addforce(Vector2(self.position_change.x, 0))
        else:
            self.rect.right = SCREEN_SIZE.x - 10
        if self.rect.top > 10:
            if self.keys_pressed[pygame.K_UP]:
                self.addforce(Vector2(0, -self.position_change.y))
        else:
            self.rect.top = 10
        if self.rect.bottom < SCREEN_SIZE.y - 10:
            if self.keys_pressed[pygame.K_DOWN]:
                self.addforce(Vector2(0, self.position_change.y))
        else:
            self.rect.bottom = SCREEN_SIZE.y - 10

        self.ship_degree()

    def addforce(self, force):
        self.acc += force

    def physics(self):
        self.vel += self.acc
        self.vel *= 0.8
        self.rect.center += self.vel
        self.acc *= 0

    def ship_degree(self):
        if self.keys_pressed[pygame.K_LEFT] or self.keys_pressed[pygame.K_RIGHT]:
            if self.keys_pressed[pygame.K_LEFT] and self.index >= 1:
                self.index -= 1
            elif self.keys_pressed[pygame.K_RIGHT] and self.index < 30:
                self.index += 1
            else:
                pass
        else:
            if self.index > 15-1:
                self.index -= 1
            elif self.index < 15-1:
                self.index += 1
            else:
                pass
    def draw(self, surface):
        surface.blit(self.image, self.rect)
import sys
from constants import *
import pygame
import Player
import Enemies
from back import *




class Game(object):
    def __init__(self, screen):
        self.screen = screen
        self.level = 1
        self.player1 = 0
        self.player_lives = 3
        self.GameExit = False
        self.clock = pygame.time.Clock()
        self.BackGround = Background("Resources/Backgrounds/CI5_1.jpg", (0, 0))

        self.list_of_players = pygame.sprite.Group()
        self.list_of_enemies = pygame.sprite.Group()
        self.list_of_bullets = pygame.sprite.Group()
        self.list_of_eggs    = pygame.sprite.Group()
        self.list_of_powerups    = pygame.sprite.Group()
        self.list_of_eat    = pygame.sprite.Group()
        self.list_of_presents    = pygame.sprite.Group()
        self.list_of_coins    = pygame.sprite.Group()


    def main(self):
        self.Player1 = Player.Player(self)
        self.list_of_players.add(self.Player1)
        self.enemiesGeneration()
        self.game()
    def enemiesGeneration(self):
        for i in range(9):
            for c in range(4):
                x = Enemies.Chicken([int(SCREEN_SIZE.x / 21) + i * int(SCREEN_SIZE.x / 9.5),
                                     int(SCREEN_SIZE.y / 27) + c * int(SCREEN_SIZE.y / 7.75)], self.level)
                self.list_of_enemies.add(x)

    def game(self):
        while not self.GameExit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.GameExit = True
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.GameExit = True
            self.tick()
            self.render()
        self.game_over_time = 0
        while self.game_over_time < 5:
            self.game_over_time += self.clock.tick() / 1000.0
            self.screen.fill(BLACK)
            draw_text_C(self.screen, "Game Over", FONT_ARIAL, 112, SCREEN_SIZE1)

    def tick(self):
        if len(self.list_of_enemies) == 0 and len(self.list_of_bullets) == 0:
            self.next_level()
        self.Player1.update(self.list_of_bullets)
        self.list_of_bullets.update()
        self.list_of_enemies.update(self.list_of_eggs)
        self.list_of_powerups.update()
        self.list_of_eat.update()
        self.list_of_presents.update()
        self.list_of_coins.update()
        self.list_of_eggs.update()
        self.collidate()


    def collidate(self):
        self.collided_p_enemies = pygame.sprite.groupcollide(self.list_of_players, self.list_of_enemies, False, True)


        self.collided_e_b = pygame.sprite.groupcollide(self.list_of_enemies, self.list_of_bullets, False, True)
        self.collided_p_power_ups = pygame.sprite.groupcollide(self.list_of_players, self.list_of_powerups, False, True)
        self.collided_p_eat = pygame.sprite.groupcollide(self.list_of_players, self.list_of_eat, False, True)
        self.collided_p_presents = pygame.sprite.groupcollide(self.list_of_players, self.list_of_presents, False, True)
        self.collided_p_coins = pygame.sprite.groupcollide(self.list_of_players, self.list_of_coins, False, True)
        self.collided_p_eggs = pygame.sprite.groupcollide(self.list_of_players, self.list_of_eggs, False, True)

        self.death(self.collided_p_enemies)
        self.bullets(self.collided_e_b)
        self.eat(self.collided_p_eat)
        self.power_ups(self.collided_p_power_ups)
        self.presents(self.collided_p_presents)
        self.coins(self.collided_p_coins)
        self.death(self.collided_p_eggs)


    def render(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.BackGround.image, self.BackGround.rect)

        self.Player1.draw(self.screen)
        self.list_of_eggs        .draw(self.screen)
        self.list_of_enemies.draw(self.screen)

        self.list_of_bullets.draw(self.screen)
        self.list_of_powerups.draw(self.screen)
        self.list_of_eat.draw(self.screen)
        self.list_of_presents.draw(self.screen)
        self.list_of_coins.draw(self.screen)
        self.draw_text()
        pygame.display.update()




    def bullets(self, lista):
        for event in lista:
            event.hit(1000 + self.Player1.gun * self.Player1.power, self.list_of_powerups, self.list_of_eat,
                      self.list_of_presents, self.list_of_coins)

    def power_ups(self, lista):
        for event in lista:
            event.power_ups()

    def eat(self, lista):
        for event in lista:
            event.eat()

    def presents(self, lista):
        for event in lista:
            event.presents()

    def coins(self, lista):
        for event in lista:
            event.coins()

    def death(self, lista):
        for event in lista:
            event.death()



    def next_level(self):
        self.level += 1
        self.enemiesGeneration()
    def draw_text(self):
        draw_text_TL(self.screen, "Score: " + str(self.Player1.score), FONT_ARIAL, 30, (5, 5))
        draw_text_TL(self.screen, "Overheat: " + str(self.Player1.overcheat / self.Player1.overcheat_limit * 100) + "%", FONT_ARIAL, 30, (250, 5))
        draw_text_BL(self.screen, "Lives: " + str(self.Player1.lives), FONT_ARIAL, 30, (5, SCREEN_SIZE.y - 5))
        draw_text_BL(self.screen, "Lvl: " + str(self.level), FONT_ARIAL, 30, (120, SCREEN_SIZE.y - 5))
        draw_text_BL(self.screen, "Power: " + str(self.Player1.power), FONT_ARIAL, 30, (220, SCREEN_SIZE.y - 5))




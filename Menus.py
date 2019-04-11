import pygame
import sys
import random
import GameLoop
import Instruction
import Ranking

from constants import *
from back import *
from Buttons import *
from Doors import *

class StartScreen(object):
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.done = False

        pygame.mixer.music.load("Resources/Music/intro.mp3")
        pygame.mixer.music.play()

        self.StartLogo = pygame.image.load("Resources/Logo/CI5.png")
        self.StartLogo = pygame.transform.scale(self.StartLogo, (int(SCREEN_SIZE.x * 0.5), int(SCREEN_SIZE.y * 0.4)))
        self.StartBackground = []
        for x in range(1, 60):
            self.StartBackground.append(pygame.image.load("Resources/Backgrounds/Snow/snow ("+ str(x) +").png"))

    def eventsInput(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                return True
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def intro(self):
        index = 0
        counter = 0
        done = False
        while not done:
            done = self.eventsInput()
            self.screen.fill(BLACK)
            self.screen.blit(self.StartBackground[index], (0, 0))
            if counter >= 7:
                index = (index + 1) % len(self.StartBackground)
                counter = 0
            counter += 1
            self.screen.blit(self.StartLogo, (SCREEN_SIZE/2 - self.StartLogo.get_rect().center))
            pygame.display.update()
        while True:
            MainMenu(self.screen).main()


class MainMenu(object):
    def __init__(self, screen):
        pygame.mouse.set_visible(True)

        self.screen = screen
        self.clock = pygame.time.Clock()
        self.index = 0
        self.counter = 0
        self.mouseX = 0
        self.mouseY = 0
        self.done = False
        self.choice = 0
        self.alreadyClick = False

        self.graphic_load()
        self.buttons_gen()
        self.doors_gen()

    def graphic_load(self):
        self.MenuBackground = [ pygame.image.load(MENU_BACKGROUND_1),
                                pygame.image.load(MENU_BACKGROUND_2),
                                pygame.image.load(MENU_BACKGROUND_3),
                                pygame.image.load(MENU_BACKGROUND_4),
                                pygame.image.load(MENU_BACKGROUND_5)]

        self.Ship_logo = pygame.image.load("Resources/Ships/Ship_logo.png")
        self.Ship_logo = pygame.transform.scale(self.Ship_logo, (int(SCREEN_SIZE.x * 0.7), int(SCREEN_SIZE.y * 0.8)))

    def buttons_gen(self):
        self.buttonList = pygame.sprite.Group()
        self.playBut = PlayButton(SCREEN_SIZE.x * 0.75, SCREEN_SIZE.y * 0.28 + SCREEN_SIZE.y * 0.19 * 0, self.buttonList)
        self.learnBut = LearnButton(SCREEN_SIZE.x * 0.75, SCREEN_SIZE.y * 0.28 + SCREEN_SIZE.y * 0.19 * 1, self.buttonList)
        self.rankingBut = RankingButton(SCREEN_SIZE.x * 0.75, SCREEN_SIZE.y * 0.28 + SCREEN_SIZE.y * 0.19 * 2, self.buttonList)
        self.quitBut = QuitButton(SCREEN_SIZE.x * 0.1, SCREEN_SIZE.y * 0.28 + SCREEN_SIZE.y * 0.19 * 3, self.buttonList)
        self.optionsBut = OptionsButton(SCREEN_SIZE.x * 0.75, SCREEN_SIZE.y * 0.28 + SCREEN_SIZE.y * 0.19 * 3, self.buttonList)

    def doors_gen(self):
        self.doorList = pygame.sprite.Group()
        self.upperDoor = UpperDoor(self.doorList)
        self.lowerDoor = LowerDoor(self.doorList)

    def events_input(self):
        self.mouseX, self.mouseY = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.process_choice()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def process_choice(self):
        if self.choice:
            self.alreadyClick = True
            self.upperDoor.playSound()

    def display_frame(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.MenuBackground[self.index], [0, (SCREEN_SIZE.y - self.MenuBackground[self.index].get_height())//2])
        self.screen.blit(self.Ship_logo, (0, 0))
        self.buttonList.draw(self.screen)
        self.doorList.draw(self.screen)
        pygame.display.update()

    def run_logic(self):
        self.counter += random.randint(0, 3000)
        if self.counter > 10000:
            self.index = random.randint(0, 5) % 5
            self.counter = 0
        else:
            pass
        if not self.alreadyClick:
            self.choice = 0
            for button in self.buttonList:
                if button.pointing:
                    self.choice = button.getChoice()
        self.buttonList.update(self)
        if self.alreadyClick:
            self.doorList.update(self)
        
    def main(self):
        while not self.done:
            self.events_input()
            self.display_frame()
            self.run_logic()


        if self.choice == "Play":
            GameLoop.Game(self.screen).main()

        elif self.choice == "Tutorial":
            pass
            #Instruction.Instruction(self.screen).main()

        elif self.choice == "Ranking":
            Ranking.Ranking(self.screen).main()

        elif self.choice == "Options":
            pass
        elif self.choice == "Quit":
            pygame.quit()
            sys.exit()
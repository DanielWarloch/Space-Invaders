import pygame
import sys

import Menus
from ScoreProcessor import *
from Doors import *

class Ranking(object):
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.index = 0
        self.counter = 0
        self.TitleFont = pygame.font.Font("Resources/Generals/font.ttf", 120)
        self.font = pygame.font.Font("Resources/Generals/font.ttf", 50)
        self.background = pygame.image.load("Resources/Backgrounds/CI5_1.jpg")

        self.done = False
        self.alreadyClick = False

        self.doorList = pygame.sprite.Group()
        self.upperDoor = UpperDoor(self.doorList)
        self.lowerDoor = LowerDoor(self.doorList)

        self.mouseX = 0
        self.mouseY = 0

        self.scores = ScoreProcessor().getScores()
        self.colors = ScoreProcessor().getColors()

        self.headers = sorted(self.scores.keys())[::-1]
        
    def eventsInput(self):
        self.mouseX, self.mouseY = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.processChoice()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def processChoice(self):
        self.alreadyClick = True
        self.upperDoor.playSound()

    def displayFrame(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.background, (0, 0))
        text = self.TitleFont.render("Ranking", True, WHITE)
        x = SCREEN_SIZE.x//2 - text.get_width()//2
        y = 5
        self.screen.blit(text, [x, y])

        for i in range(15):
            try:
                text = self.font.render(str(i + 1) + ". " + str(self.headers[i]), True, self.colors[self.headers[i]])
                x = 150
                y = (i + 4) * 65 - text.get_height()//2
                self.screen.blit(text, [x, y])
                text = self.font.render("." * 60, True, WHITE)
                xx = SCREEN_SIZE.x // 2 - text.get_width() // 2
                yy = (i + 4) * 65 - text.get_height() // 2
                self.screen.blit(text, [xx, yy])
                text = self.font.render(self.scores[self.headers[i]], True, self.colors[self.headers[i]])
                x = SCREEN_SIZE.x - 150 - text.get_width()
                self.screen.blit(text, [x, y])
            except IndexError:
                break
    

        
        self.doorList.draw(self.screen)
        pygame.display.update()

    def runLogic(self):
        if self.alreadyClick:
            self.doorList.update(self)
        
    def main(self):
        while not self.done:
            self.eventsInput()
            self.displayFrame()
            self.runLogic()
            self.clock.tick(60)
        Menus.MainMenu(self.screen).main()


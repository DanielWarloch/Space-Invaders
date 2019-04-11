import pygame

import Menus
import sys
from Enemies import *
from Doors import *
from constants import *

class Instruction(object):
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.done = False
        self.index = 0

        self.moveOn = False

        self.chickenList = pygame.sprite.Group()
        self.allSpriteList = pygame.sprite.Group()
        
        self.lowerDoor = LowerDoor(self.allSpriteList)
        self.upperDoor = UpperDoor(self.allSpriteList)

        self.chicken = Chicken(self.screen, (0, 0), 1)


        self.chicken.rect.x = 225 - self.chicken.rect.width//2
        self.chicken.rect.y = 68 + 563 * 0.4 - self.chicken.rect.height


        for chick in self.chickenList:
            chick.moveX = chick.moveY = 0
            try:
                chick.moveSlow = 0
            except AttributeError:
                continue

        self.leftArrow = pygame.image.load("Resources/Generals/arrow.png")
        self.rightArrow = pygame.transform.flip(self.leftArrow, True, False)

        self.background = pygame.image.load("Resources/Backgrounds/CI5_1.jpg")
        self.teacher = pygame.image.load("Resources/Generals/teacher.png")
        self.contents = [pygame.image.load("Resources/Backgrounds/md_5b155a67a7a43.png"),
                         pygame.image.load("Resources/Backgrounds/md_5b155a67a7a43.png"),
                         pygame.image.load("Resources/Backgrounds/md_5b155a67a7a43.png")]
        

        self.mouseX = 0
        self.mouseY = 0

    def logics(self):        
        if self.moveOn:
            self.allSpriteList.update(self)
        self.chickenList.update(self)
        
    def eventsInput(self):
        self.mouseX, self.mouseY = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.mouseX < 10 + self.leftArrow.get_width():
                    if self.index > 0:
                        self.index -= 1
                elif self.mouseX > SCREEN_SIZE.x - self.leftArrow.get_width() - 10:
                    if self.index < 2:
                        self.index += 1
                else:
                    self.processChoice()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if self.index > 0:
                        self.index -= 1
                elif event.key == pygame.K_RIGHT:
                    if self.index < 2:
                        self.index += 1

    def processChoice(self):
        self.moveOn = True
        self.upperDoor.playSound()
               
    def displayFrame(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.background, [0, 68])
        self.screen.blit(self.contents[self.index], [0, 68])
        if self.index == 1:
            self.chickenList.draw(self.screen)
        self.screen.blit(self.teacher, [SCREEN_SIZE.x - self.teacher.get_width(),
                                        SCREEN_SIZE.y - self.teacher.get_height()])
        if self.index != 0:
            self.screen.blit(self.leftArrow, [10, SCREEN_SIZE.y//2 - self.leftArrow.get_height()//2])
        if self.index != 2:
            self.screen.blit(self.rightArrow, [SCREEN_SIZE.x - self.rightArrow.get_width() - 10, SCREEN_SIZE.y//2 - self.leftArrow.get_height()//2])
        self.allSpriteList.draw(self.screen)
        pygame.display.update()

    def main(self):
        while not self.done:
            self.eventsInput() 
            self.displayFrame()
            self.logics()
            self.clock.tick(60)
        Menus.MainMenu(self.screen).main()

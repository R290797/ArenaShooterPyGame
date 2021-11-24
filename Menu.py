import pygame
from tkinter import *
from HUD import TitleCard

class menu:

    def __init__(self, screen):

        # Menu Variables
        self.gameState = "menu"
        self.screen = screen

        # Screen Variables
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()

        # Fonts Variables
        startFont = pygame.font.Font('freesansbold.ttf', 70)
        self.descText = startFont.render("Press Space to play", True, (255, 255, 255))
        self.displayTime = 0
        self.displayTimeSnapshot = 0
        self.snapshotCounter = 0

        helpFont = pygame.font.Font('freesansbold.ttf', 30)
        self.helpText = helpFont.render("Press H for help", True, (255, 255, 255))

        # Background Variables
        background = pygame.image.load("resources/menu.png")
        self.background = background

    def menuScreen(self):
        self.screen.blit(self.background, (-60, -100))

        # Blink Text
        self.blinkText()

        # Input Handler
        self.input()

        # Help text
        self.screen.blit(self.helpText, (10, 760))

    def blinkText(self):
        if self.displayTime < 1000:
            self.displayTime = (pygame.time.get_ticks() - self.displayTimeSnapshot)
            self.screen.blit(self.descText, (110, 400))

        elif 1000 <= self.displayTime < 2000:
            self.displayTime = (pygame.time.get_ticks() - self.displayTimeSnapshot)

        elif self.displayTime >= 2000:
            self.displayTime = (pygame.time.get_ticks() - self.displayTimeSnapshot)

            # set Snapshot
            self.displayTimeSnapshot = 2000*self.snapshotCounter
            self.snapshotCounter += 1

            print(self.displayTimeSnapshot)
            self.displayTime = 0

    def setGameState(self, gameState):
        self.gameState = gameState

    def input(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.gameState = "game"

                if event.key == pygame.K_h:
                    self.gameState = "help"




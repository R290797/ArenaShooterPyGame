import pygame


class helpMenu:

    def __init__(self, screen, menu):
        self.screen = screen
        self.menu = menu

        # Font Variables
        # Fonts Variables
        startFont = pygame.font.Font('freesansbold.ttf', 40)
        self.descText = startFont.render("Leertaste drücken um zurück zu gehen", True, (255, 255, 255))
        self.displayTime = 0
        self.displayTimeSnapshot = 0
        self.snapshotCounter = 0

        # Background variables
        background = pygame.image.load("resources/helpMenu.png")
        self.background = background

    def helpScreen(self):
        self.input()

        self.screen.fill((0, 0, 0))
        self.screen.blit(self.background, (0, 0))
        self.blinkText()

    def blinkText(self):
        if self.displayTime < 1000:
            self.displayTime = (pygame.time.get_ticks() - self.displayTimeSnapshot)
            self.screen.blit(self.descText, (65, 600))

        elif 1000 <= self.displayTime < 2000:
            self.displayTime = (pygame.time.get_ticks() - self.displayTimeSnapshot)

        elif self.displayTime >= 2000:
            self.displayTime = (pygame.time.get_ticks() - self.displayTimeSnapshot)

            # set Snapshot
            self.displayTimeSnapshot = 2000*self.snapshotCounter
            self.snapshotCounter += 1

            print(self.displayTimeSnapshot)
            self.displayTime = 0

    def input(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.menu.setGameState("menu")


import pygame

class gameOver:

    def __init__(self, screen, wave, player, menu):
        self.screen = screen
        self.wave = wave
        self.score = 0
        self.waveNum = 0
        self.menu = menu

        background = pygame.image.load("resources/gameOver.png")
        self.background = background

        self.font = pygame.font.Font('freesansbold.ttf', 40)
        self.scoreText = self.font.render("Score: " + str(self.score), True, (255, 255, 255))
        self.waveText = self.font.render("Wave: " + str(self.waveNum), True, (255, 255, 255))
        self.exitText = self.font.render("press X to Exit", True, (255, 255, 255))

    def gameOverScreen(self):
        self.input()
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.background, (0, -90))

        self.screen.blit(self.scoreText, (100, 200))
        self.screen.blit(self.waveText, (100, 300))
        self.screen.blit

    def input(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.menu.setGameState("restart")

                if event.key == pygame.K_m:
                    self.menu.setGameState("menuRestart")

    def statUpdate(self, player, wave):
        self.score = player.score
        self.waveNum = wave.waveNum
        self.scoreText = self.font.render("Score: " + str(self.score), True, (255, 255, 255))
        self.waveText = self.font.render("Wave: " + str(self.waveNum), True, (255, 255, 255))













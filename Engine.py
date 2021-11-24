from Collision import *
import HUD
from Menu import menu
from HelpMenu import helpMenu
from GameOver import gameOver
from Wave import *

# initialize the game
pygame.init()

# Clock Init
gameClock = pygame.time.Clock()

# Initialize window
icon = pygame.image.load("resources/skullBoy.png")
pygame.display.set_icon(icon)
gameWindow = pygame.display.set_mode((900, 800))

# Background initialize
background = pygame.image.load("resources/background.png").convert(gameWindow)

# Player Init
ozzy = player("resources/Protagonist.png", 100, 100, 25, gameWindow)

# Wave mechanics
waveCount = 0
activeWave = False
initWave = Wave(gameWindow, ozzy, 0)

# Menus
menu = menu(gameWindow)
helpScreen = helpMenu(gameWindow, menu)
gameOver = gameOver(gameWindow, initWave, ozzy, menu)

# Program Loop
running = True
while running:
    # Main Menu
    if menu.gameState == "menu":
        pygame.display.flip()
        menu.menuScreen()
        pygame.display.update()

    # Help Screen
    if menu.gameState == "help":
        pygame.display.flip()
        helpScreen.helpScreen()
        pygame.display.update()

    if menu.gameState == "gameOver":
        pygame.display.flip()
        gameOver.gameOverScreen()
        pygame.display.update()

    # restart game
    if menu.gameState == "restart":
        ozzy = player("resources/Protagonist.png", 100, 100, 25, gameWindow)
        initWave = Wave(gameWindow, ozzy, 0)
        menu.gameState = "game"

    if menu.gameState == "menuRestart":
        ozzy = player("resources/Protagonist.png", 100, 100, 25, gameWindow)
        initWave = Wave(gameWindow, ozzy, 0)
        menu.gameState = "menu"

    # Game Loop
    if menu.gameState == "game":
        pygame.display.flip()

        # Update scores
        gameOver.statUpdate(ozzy, initWave)

        gameClock.tick(60)
        gameWindow.blit(background, (-50, -50))

        # Player Inputs
        ozzy.setTime()
        ozzy.input()
        ozzy.healthCheck()
        ozzy.shoot(gameWindow)

        # Blitting
        ozzy.blit(gameWindow)
        ozzy.bulletBlit(gameWindow)

        # Game Loop
        initWave = waveLoop(initWave)
        initWave.renderWave()

        # Collision
        isHit(ozzy, initWave)
        playerHit(ozzy, initWave.enemyList, menu)

        # HUD init and Indicators
        pygame.draw.rect(gameWindow, (0, 0, 0), (0, 0, 900, 100))
        HUD.ammoDisplay(ozzy, gameWindow)
        HUD.healthDisplay(ozzy, gameWindow)
        HUD.enemyDisplay(initWave, gameWindow)
        HUD.waveDisplay(initWave, gameWindow)
        HUD.skillpointDisplay(ozzy, gameWindow)
        HUD.scoreDisplay(ozzy, gameWindow)
        ozzy.upgradeDisplay()
        initWave.hitIndiactor()

        pygame.display.update()

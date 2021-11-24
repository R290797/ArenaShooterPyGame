import pygame


def ammoDisplay(player, screen):
    ammoFont = pygame.font.Font('freesansbold.ttf', 32)

    displayString = "Ammo: "
    tmp = ((player.ammo + 1) - len(player.bulletList))
    displayString += str(tmp)
    ammoText = ammoFont.render(displayString, True, (255, 255, 255), (0, 0, 0))
    screen.blit(ammoText, (10, 0))


def healthDisplay(player, screen):
    healthFont = pygame.font.Font('freesansbold.ttf', 32)

    displayString = "Health: "
    tmp = player.health
    displayString += str(tmp)
    healthText = healthFont.render(displayString, True, (255, 255, 255), (0, 0, 0))
    screen.blit(healthText, (700, 0))


def enemyDisplay(wave, screen):
    enemyFont = pygame.font.Font('freesansbold.ttf', 32)

    displayString = "Remaining: "
    tmp = wave.enemiesRemaining
    displayString += str(tmp)
    enemyText = enemyFont.render(displayString, True, (255, 255, 255), (0, 0, 0))
    screen.blit(enemyText, (10, 32))


def waveDisplay(wave, screen):
    waveFont = pygame.font.Font('freesansbold.ttf', 32)

    displayString = "Wave: "
    tmp = wave.waveNum
    displayString += str(tmp)
    waveText = waveFont.render(displayString, True, (255, 255, 255), (0, 0, 0))
    screen.blit(waveText, (10, 64))


def skillpointDisplay(player, screen):
    spFont = pygame.font.Font('freesansbold.ttf', 32)

    displayString = "SP: "
    tmp = player.skillpoints
    displayString += str(tmp)
    spText = spFont.render(displayString, True, (255, 255, 255), (0, 0, 0))
    screen.blit(spText, (700, 32))


def newRoundDisplay(screen, time):
    nrFont = pygame.font.Font('freesansbold.ttf', 40)

    displayString = "Next wave in: "
    tmp = int(10 - (time / 600))
    displayString += str(tmp)
    nrText = nrFont.render(displayString, True, (0, 0, 0))
    screen.blit(nrText, (600, 120))


def scoreDisplay(player, screen):
    sFont = pygame.font.Font('freesansbold.ttf', 50)

    displayString = "Score: "
    tmp = int(player.score)
    displayString += str(tmp)
    sText = sFont.render(displayString, True, (255, 255, 255))
    screen.blit(sText, (340, 20))


def TitleCard(screen):
    sFont = pygame.font.Font('freesansbold.ttf', 100)

    displayString = "Arena"
    sText = sFont.render(displayString, True, (255, 255, 255))
    screen.blit(sText, (270, 20))

def playButton(screen):
    sFont = pygame.font.Font('freesansbold.ttf', 100)

    displayString = "Play"
    sText = sFont.render(displayString, True, (255, 255, 255))
    screen.blit(sText, (270, 20))

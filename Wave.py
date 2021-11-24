import random
from enemies.Enemy import *
from Player import *
from HUD import newRoundDisplay
import Spawn


# Logic of the game loop, getting a skill point and moving to the next wave
def waveLoop(wave):
    if wave.enemiesRemaining == 0 and wave.roundEnd is False:
        wave.roundEnd = True
        wave.endRoundTimer = pygame.time.get_ticks()
        if wave.waveNum % 5 == 0 and wave.waveNum != 0:
            wave.player.skillpoints += 3
        else:
            wave.player.skillpoints += 1
        return wave

    if wave.roundEnd is True and (pygame.time.get_ticks() - wave.endRoundTimer < wave.roundDelay):
        newRoundDisplay(wave.screen, pygame.time.get_ticks() - wave.endRoundTimer)

    if wave.roundEnd is True and (pygame.time.get_ticks() - wave.endRoundTimer > wave.roundDelay):
        wave.roundEnd = False
        wave.player.invFrame = True
        wave.player.hitTime = pygame.time.get_ticks()
        return Wave(wave.screen, wave.player, wave.waveNum + 1)

    else:
        return wave


class Wave:

    def __init__(self, screen, player, waveNum):
        self.player = player
        self.screen = screen
        self.waveNum = waveNum

        if self.waveNum % 5 == 0:
            if self.waveNum <= 20:
                self.enemies = int(waveNum / 5)
            else:
                self.enemies = 5
        else:
            if self.waveNum < 30:
                self.enemies = random.randint(waveNum, 2 *  waveNum)
            else:
                self.enemies = waveNum + (random.randint(0, 10))

        self.enemiesRemaining = self.enemies

        # Logic to start timer at the end of the wave before next timer
        self.roundEnd = False
        self.endRoundTimer = 0
        self.roundDelay = 6000

        # Fill the enemy List
        self.enemyList = []

        # Here we can change the spawn Behaviour
        self.enemyList = Spawn.spawnList(self.waveNum, self.enemies, self.screen, self.player)

    def renderWave(self):
        renderEnemies(self.screen, self.enemyList, self.player)

    def hitIndiactor(self):
        for enemies in range(len(self.enemyList)):
            self.enemyList[enemies].hitIndicator()

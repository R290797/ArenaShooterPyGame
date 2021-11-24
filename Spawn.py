import pygame
import random
from enemies.Enemy import *


def spawn(player, screen):
    choose = random.randint(1, 7)
    if choose == 1:
        return swarmer(random.randint(0, 875), random.randint(0, 50))

    if choose == 2:
        return fastSwarmer(random.randint(0, 875), random.randint(0, 50))

    if choose == 3:
        return bigSwarmer(random.randint(0, 875), random.randint(0, 50))

    if choose == 4:
        return fireTurret(random.randint(0, 875), random.randint(100, 775), screen, player)

    if choose == 5:
        return spiderHEnemy(random.randint(0, 875), random.randint(100, 775))

    if choose == 6:
        return spiderVEnemy(random.randint(0, 875), random.randint(100, 775))

    if choose == 7:
        return bigSpider(random.randint(0, 875), random.randint(100, 775))


def bossSpawn(player, screen):
    choose = random.randint(1, 2)
    if choose == 1:
        return bouncingFire(random.randint(0, 875), random.randint(100, 775), screen, player)
    if choose == 2:
        return bigBot(random.randint(0, 875), random.randint(100, 775), screen, player)


def spawnList(waveNum, waveEnemies, screen, player):
    enemyList = []

    for x in range(waveEnemies):
        if waveNum % 5 != 0:
            enemyList.append(spawn(player, screen))
        if waveNum % 5 == 0:
            enemyList.append(bossSpawn(player, screen))

    return enemyList


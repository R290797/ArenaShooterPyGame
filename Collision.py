import pygame
import math
from Bullet import dummyBullet
from enemies.Enemy import dummyEnemy


def isCollisionStandard(entityA, entityB):
    # Find the distance between the two entities (Pythagorean Theorem)
    distanceX = entityA.x - entityB.x
    distanceX = math.pow(distanceX, 2)

    distanceY = entityA.y - entityB.y
    distanceY = math.pow(distanceY, 2)

    distance = math.sqrt(distanceX + distanceY)

    if distance < 20:
        return True
    else:
        return False


def isCollisionFlex(entityA, entityB, radius=20):
    # Find the distance between the two entities (Pythagorean Theorem)
    distanceX = entityA.x - entityB.x
    distanceX = math.pow(distanceX, 2)

    distanceY = entityA.y - entityB.y
    distanceY = math.pow(distanceY, 2)

    distance = math.sqrt(distanceX + distanceY)
    #
    if radius > distance:
        return True
    else:
        return False


def isHit(player, wave):
    for bullet in range(len(player.bulletList)):
        for enemy in range(len(wave.enemyList)):
            if isCollisionFlex(player.bulletList[bullet], wave.enemyList[enemy], wave.enemyList[enemy].radius):
                player.bulletList[bullet] = dummyBullet()

                # Here we add the lowering of the enemies health upon being hit
                if wave.enemyList[enemy].health != 0:
                    wave.enemyList[enemy].hit = True
                    wave.enemyList[enemy].health -= 1
                if wave.enemyList[enemy].health == 0:
                    # Here we lower the remaining enemies, each time an enemy is killed, and increase score
                    player.score += wave.enemyList[enemy].score
                    wave.enemiesRemaining -= 1
                    wave.enemyList[enemy] = dummyEnemy()

def playerHit(player, enemyList, menu):
    for enemy in range(len(enemyList)):
        if isCollisionFlex(player, enemyList[enemy], enemyList[enemy].radius) and player.invFrame is False:
            player.hit = True
            player.invFrame = True
            player.health -= 1
            player.hitTime = pygame.time.get_ticks()
        # Show the hit
        player.hitIndicator()

    if player.health == 0:
        menu.gameState = "gameOver"



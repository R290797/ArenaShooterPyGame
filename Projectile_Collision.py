import pygame
import math


def projectileCollision(entityA, entityB, radius=15):
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


def projectileHit(player, projectileList):
    for enemy in range(len(projectileList)):
        if projectileCollision(player, projectileList[enemy], projectileList[enemy].radius) and player.invFrame is False:
            player.hit = True
            player.hitIndicator()
            player.invFrame = True
            player.health -= 1
            player.hitTime = pygame.time.get_ticks()

import pygame


def dummyBullet():
    return bullet(-1000, -1000, "null")


class bullet:

    def __init__(self, playerX, playerY, direction):
        self.entityImg = pygame.image.load("resources/playerBullet.png")
        self.x = playerX + 8
        self.y = playerY

        if direction == "W":
            self.dx = 0
            self.dy = -10
        elif direction == "A":
            self.dx = -10
            self.dy = 0
        elif direction == "S":
            self.dx = 0
            self.dy = 10
        elif direction == "D":
            self.dx = 10
            self.dy = 0
        elif direction == "null":
            self.dx = 0
            self.dy = 0

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def setChange(self, dx, dy):
        self.dx = dx
        self.dy = dy

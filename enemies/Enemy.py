import pygame
import math
import random
from Projectile_Collision import projectileHit, projectileCollision


# Render a list of enemies on a screen, and make them attack the player
def renderEnemies(screen, enemyList, player):
    for enemy in range(len(enemyList)):
        enemyList[enemy].attackPattern(player)
        enemyList[enemy].blit(screen)


def renderProjectiles(screen, projectileList):
    for projectile in range(len(projectileList)):
        screen.blit(projectileList[projectile], (projectileList[projectile].x, projectileList[projectile].y))


def dummyEnemy():
    return defaultEnemy("resources/bullet.png", -2000, - 2000, 0)


class defaultEnemy:

    def __init__(self, entityImg, x, y, speed):
        self.entityImg = pygame.image.load(entityImg)
        self.x = x
        self.y = y

        # These attributes are there to allow flowing movement
        self.change_y = 0
        self.change_x = 0

        # This attribute is used to affect the speed of the entity
        self.speed = speed

        # Health attribute - Shot before dead
        self.health = 3

        # Radius attribute
        self.radius = 20

        # Hit indicators and Variables
        self.hit = False
        self.hitShowing = False
        self.hit = 0
        self.hitImg = pygame.image.load("resources/bullet.png")
        self.normalImg = pygame.image.load("resources/bullet.png")

        # Score
        self.score = 1
        self.showScore = 0

    def blit(self, screen):
        screen.blit(self.entityImg, (self.x, self.y))

    def hitIndicator(self):
        if self.hit is True and self.hitShowing is False:
            self.hitShowing = True
            self.entityImg = self.hitImg
            self.hit = pygame.time.get_ticks()
        if pygame.time.get_ticks() - self.hit > 500:
            self.entityImg = self.normalImg
            self.hit = False
            self.hitShowing = False

    def move(self):
        self.x += self.change_x * self.speed
        self.y += self.change_y * self.speed

    # Logic to make the enemy track the player
    def attackPattern(self, player):
        dx = player.x - self.x
        dy = player.y - self.y
        distance = math.hypot(dx, dy)

        # Normalize the vectors to get the actual movement values
        dx /= distance
        dy /= distance

        # Move along this value
        self.change_x = dx
        self.change_y = dy
        self.move()


class swarmer(defaultEnemy):

    def __init__(self, x, y):
        defaultEnemy.__init__(self, "resources/Swarmer.png", x, y, 3)
        self.health = 3

        self.normalImg = pygame.image.load("resources/Swarmer.png")
        self.hitImg = pygame.image.load("resources/SwarmerHit.png")


class fastSwarmer(defaultEnemy):

    def __init__(self, x, y):
        defaultEnemy.__init__(self, "resources/FastSwarmer.png", x, y, 5)
        self.health = 2

        self.normalImg = pygame.image.load("resources/FastSwarmer.png")
        self.hitImg = pygame.image.load("resources/FastSwarmerHit.png")


class bigSwarmer(defaultEnemy):

    def __init__(self, x, y):
        defaultEnemy.__init__(self, "resources/BigSwarmer.png", x, y, 1)
        self.health = 10
        self.radius = 30


        self.normalImg = pygame.image.load("resources/BigSwarmer.png")
        self.hitImg = pygame.image.load("resources/BigSwarmerHit.png")


# An enemy which has the ability to fire more enemies
class fireTurret(defaultEnemy):

    def __init__(self, x, y, screen, player):
        defaultEnemy.__init__(self, "resources/fireTurret.png", x, y, 0)
        self.health = 5

        self.screen = screen
        self.player = player
        self.projectileState = [0, 0, 0, 0]
        self.projectiles = []
        self.fired = False

        self.normalImg = pygame.image.load("resources/fireTurret.png")
        self.hitImg = pygame.image.load("resources/fireTurretHit.png")

    def attackPattern(self, player):

        # To ensure that projectiles hit the player
        projectileHit(self.player, self.projectiles)

        if self.fired is False and self.projectileState.count(0) == 4:
            self.fired = True
            p1, p2, p3, p4 = fireProjectile(self.x, self.y, "up", self.screen, self.player), \
                             fireProjectile(self.x, self.y, "left", self.screen, self.player), \
                             fireProjectile(self.x, self.y, "down", self.screen, self.player), \
                             fireProjectile(self.x, self.y, "right", self.screen, self.player)

            self.projectiles.append(p1)
            self.projectiles.append(p2)
            self.projectiles.append(p3)
            self.projectiles.append(p4)

        if self.fired is True:
            for projectile in range(len(self.projectiles)):
                self.projectiles[projectile].attackPattern(self.player)

                if self.projectiles[projectile].passedWall() is True:
                    self.projectiles[projectile].dummy()
                    self.projectileState[projectile] = 1

        if self.fired is True and self.projectileState.count(1) == 4:
            self.projectiles = []
            self.fired = False
            self.projectileState = [0, 0, 0, 0]


class fireProjectile(defaultEnemy):

    def __init__(self, x, y, direction, screen, player):
        defaultEnemy.__init__(self, "resources/enemyBullet.png", x, y, 6)
        self.direction = direction
        self.health = 5
        self.screen = screen

    # Projectiles will fire in the direction that they are called
    def attackPattern(self, player):

        if self.direction == "up":
            self.change_x = 0
            self.change_y = -1
        if self.direction == "left":
            self.change_x = -1
            self.change_y = 0
        if self.direction == "down":
            self.change_x = 0
            self.change_y = 1
        if self.direction == "right":
            self.change_x = 1
            self.change_y = 0
        if self.direction == "dUL":
            self.change_x = -1
            self.change_y = -1
        if self.direction == "dDL":
            self.change_x = -1
            self.change_y = 1
        if self.direction == "dDR":
            self.change_x = 1
            self.change_y = 1
        if self.direction == "dUR":
            self.change_x = 1
            self.change_y = -1

        self.blit(self.screen)
        self.move()

    def passedWall(self):
        if self.x < 0:
            return True
        if self.x > 875:
            return True
        if self.y < 100:
            return True
        if self.y > 775:
            return True
        else:
            return False

    def dummy(self):
        self.x = 2000
        self.y = 2000
        self.change_x = 0
        self.change_y = 0


class bouncingFire(defaultEnemy):

    def __init__(self, x, y, screen, player):
        defaultEnemy.__init__(self, "resources/bigTurret.png", x, y, 3)

        firstMove = [-1, 1]
        initMovement = firstMove[random.randint(0, 1)]

        self.change_x = initMovement
        self.change_y = random.randint(-1, 1)

        self.health = 15

        self.screen = screen
        self.player = player
        self.projectileState = [0, 0, 0, 0, 0, 0, 0, 0]
        self.projectiles = []
        self.fired = False

        self.normalImg = pygame.image.load("resources/bigTurret.png")
        self.hitImg = pygame.image.load("resources/bigTurretHit.png")

        self.score = 5

    def attackPattern(self, player):

        # To ensure that projectiles hit the player
        projectileHit(self.player, self.projectiles)

        if self.fired is False and self.projectileState.count(0) == 8:
            self.fired = True
            p1, p2, p3, p4, p5, p6, p7, p8 = fireProjectile(self.x + 32, self.y + 32, "up", self.screen, self.player), \
                                             fireProjectile(self.x + 32, self.y + 32, "left", self.screen, self.player), \
                                             fireProjectile(self.x + 32, self.y + 32, "down", self.screen, self.player), \
                                             fireProjectile(self.x + 32, self.y + 32, "right", self.screen,self.player), \
                                             fireProjectile(self.x + 32, self.y + 32, "dUL", self.screen, self.player), \
                                             fireProjectile(self.x + 32, self.y + 32, "dDL", self.screen, self.player), \
                                             fireProjectile(self.x + 32, self.y + 32, "dDR", self.screen, self.player), \
                                             fireProjectile(self.x + 32, self.y + 32, "dUR", self.screen, self.player)

            self.projectiles.append(p1)
            self.projectiles.append(p2)
            self.projectiles.append(p3)
            self.projectiles.append(p4)
            self.projectiles.append(p5)
            self.projectiles.append(p6)
            self.projectiles.append(p7)
            self.projectiles.append(p8)

        if self.fired is True:
            for projectile in range(8):
                self.projectiles[projectile].attackPattern(self.player)

                if self.projectiles[projectile].passedWall() is True:
                    self.projectiles[projectile].dummy()
                    self.projectileState[projectile] = 1

        if self.fired is True and self.projectileState.count(1) == 8:
            self.projectiles = []
            self.fired = False
            self.projectileState = [0, 0, 0, 0, 0, 0, 0, 0]

        if self.x < 0:
            self.change_x = 1
            self.change_y = random.randint(-1, 1)

        if self.x > 875:
            self.change_x = -1
            self.change_y = random.randint(-1, 1)

        if self.y < 100:
            self.change_x = random.randint(-1, 1)
            self.change_y = 1

        if self.y > 775:
            self.change_x = random.randint(-1, 1)
            self.change_y = -1

        self.move()

    def move(self):
        self.x += self.change_x * self.speed
        self.y += self.change_y * self.speed


class spiderHEnemy(defaultEnemy):

    def __init__(self, x, y):
        defaultEnemy.__init__(self, "resources/floater.png", x, y, 4)

        # Randomly set the starting direction
        self.change_x = pow(-1, random.randint(1, 4))
        self.change_y = 0

        self.health = 1

        self.normalImg = pygame.image.load("resources/floater.png")
        self.hitImg = pygame.image.load("resources/floaterHit.png")

    # Here we change the attack pattern of this enemy
    # since this is the H version, we want it to move left to right. Switching when hitting a wall
    def attackPattern(self, player):

        # Movement behaviour when hitting a wall
        if self.x < 0:
            self.x = 1
            self.change_x = 1

        if self.x > 875:
            self.x = 874
            self.change_x = -1

        self.move()


class spiderVEnemy(defaultEnemy):

    def __init__(self, x, y):
        defaultEnemy.__init__(self, "resources/floater.png", x, y, 3)

        # Randomly set the starting direction
        self.change_y = pow(-1, random.randint(1, 4))
        self.change_x = 0

        self.health = 1

        self.normalImg = pygame.image.load("resources/floater.png")
        self.hitImg = pygame.image.load("resources/floaterHit.png")

    # Here we change the attack pattern of this enemy
    # since this is the V version, we want it to move left to right. Switching when hitting a wall
    def attackPattern(self, player):

        # Movement behaviour when hitting a wall
        if self.y < 100:
            self.y = 101
            self.change_y = 1

        if self.y > 775:
            self.y = 774
            self.change_y = -1

        self.move()


class bigSpider(defaultEnemy):

    def __init__(self, x, y):
        defaultEnemy.__init__(self, "resources/bouncer.png", x, y, 3)

        firstMove = [-1, 1]
        initMovement = firstMove[random.randint(0, 1)]

        self.change_x = initMovement
        self.change_y = random.randint(-1, 1)

        self.health = 3

        self.normalImg = pygame.image.load("resources/bouncer.png")
        self.hitImg = pygame.image.load("resources/bouncerHit.png")

    # Bouncing behaviour
    def attackPattern(self, player):

        if self.x < 0:
            self.change_x = 1
            self.change_y = random.randint(-1, 1)

        if self.x > 875:
            self.change_x = -1
            self.change_y = random.randint(-1, 1)

        if self.y < 100:
            self.change_x = random.randint(-1, 1)
            self.change_y = 1

        if self.y > 775:
            self.change_x = random.randint(-1, 1)
            self.change_y = -1

        self.move()


class bigBot(defaultEnemy):

    def __init__(self, x, y, screen, player):
        defaultEnemy.__init__(self, "resources/bigBot.png", x, y, 3)

        firstMove = [-1, 1]
        initMovement = firstMove[random.randint(0, 1)]

        self.change_x = initMovement
        self.change_y = random.randint(-1, 1)

        self.health = 7

        self.screen = screen
        self.player = player
        self.projectileState = [0]
        self.projectiles = []
        self.fired = False

        self.normalImg = pygame.image.load("resources/bigBot.png")
        self.hitImg = pygame.image.load("resources/bigBotHit.png")

        self.score = 5

    def attackPattern(self, player):

        # To ensure that projectiles hit the player
        projectileHit(self.player, self.projectiles)

        if self.fired is False and self.projectileState.count(0) == 1:
            self.fired = True
            p1 = breakBot(self.x, self.y, random.randint(3, 5), self.screen, self.player)

            self.projectiles.append(p1)

        if self.fired is True:
            for projectile in range(1):
                self.projectiles[projectile].attackPattern(self.player)

                if projectileCollision(self.player, self.projectiles[projectile]) is True:
                    self.projectiles[projectile].dummy()
                    self.projectileState[projectile] = 1

        if self.fired is True and self.projectileState.count(1) == 1:
            self.projectiles = []
            self.fired = False
            self.projectileState = [0]

        if self.x < 0:
            self.change_x = 1
            self.change_y = random.randint(-1, 1)

        if self.x > 875:
            self.change_x = -1
            self.change_y = random.randint(-1, 1)

        if self.y < 100:
            self.change_x = random.randint(-1, 1)
            self.change_y = 1

        if self.y > 775:
            self.change_x = random.randint(-1, 1)
            self.change_y = -1

        self.move()

    def move(self):
        self.x += self.change_x * self.speed
        self.y += self.change_y * self.speed


# these are the robots the bigBot shoots
class breakBot(defaultEnemy):

    def __init__(self, x, y, speed, screen, player):
        defaultEnemy.__init__(self, "resources/enemyBullet.png", x, y, speed)
        self.screen = screen
        self.player = player
        self.off = False

    def dummy(self):
        self.off = True
        self.x = 3000
        self.y = 3000

    def attackPattern(self, player):
        if self.off is False:
            defaultEnemy.attackPattern(self, player)
            self.blit(self.screen)

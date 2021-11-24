# Information and actions of the player stored here
from pygame import *
from Bullet import *

class player:

    def __init__(self, entityImg, x, y, speed, screen):

        # Text Variables
        self.reloadFont = pygame.font.Font('freesansbold.ttf', 20)

        self.entityImg = pygame.image.load(entityImg)
        self.x = x
        self.y = y

        # These attributes are there to allow flowing movement
        self.change_x = 0
        self.change_y = 0

        # This attribute is used to affect the speed of the player
        self.speed = speed

        # initialize the gun and bullet list within the character
        self.bulletList = []

        # Time Variables
        self.current_Time = pygame.time.get_ticks()
        self.previous_time = 0
        self.reload_time = 0

        # Shooting Variable
        self.keyPress = ""
        self.shooting = False
        self.reloading = False

        # Gun Variables
        self.ammo = 9
        self.firerate = 500
        self.accuracy = 0

        # Health Variables
        self.health = 3
        self.invFrame = False
        self.invTime = 1000
        self.hitTime = 0

        # Upgrade System
        self.skillpoints = 0
        self.skillTimer = 0
        self.skilling = ""
        self.skillLockout = False

        # Hit indicator variables
        self.hit = False
        self.hitShowing = False
        self.hit = 0

        # Screen
        self.screen = screen

        # Score
        self.score = 0

    # Function to show player on desired screen
    def blit(self, screen):
        screen.blit(self.entityImg, (self.x, self.y))

    def hitIndicator(self):
        if self.hit is True and self.hitShowing is False:
            self.hitShowing = True
            self.entityImg = pygame.image.load("resources/ProtHit.png")
            self.hit = pygame.time.get_ticks()
        if pygame.time.get_ticks() - self.hit > 500:
            self.entityImg = pygame.image.load("resources/Protagonist.png")
            self.hit = False
            self.hitShowing = False

    def move(self):
        if self.x < 0:
            self.x = 0
        if self.x > 875:
            self.x = 875
        if self.y < 101:
            self.y = 101
        if self.y > 775:
            self.y = 775

        self.x += self.change_x
        self.y += self.change_y

    def shoot(self, screen):
        # This works because ammo is basically a threshold, if the length goes over this, then we know
        # we have no more ammo left.
        if len(self.bulletList) > self.ammo and self.reloading is False:
            self.reloadStart()

        elif self.keyPress != "" and self.shooting is True and self.reloading is False and (
                self.current_Time - self.previous_time > self.firerate):
            self.previous_time = pygame.time.get_ticks()
            newBullet = bullet(self.x, self.y, self.keyPress)
            self.bulletList.append(newBullet)

        elif self.reloading is True:
            self.reloadEnd(screen)

    def reloadStart(self):
        self.reloading = True
        self.reload_time = pygame.time.get_ticks()

    def reloadEnd(self, screen):
        timer = int((1799 - (pygame.time.get_ticks() - self.reload_time)) / 600)
        reloadText = self.reloadFont.render(str(timer), True,
                                            (255, 255, 255), (0, 0, 0))
        screen.blit(reloadText, (self.x + 30, self.y + 30))
        if pygame.time.get_ticks() - self.reload_time > 1799:
            self.bulletList = []
            self.reloading = False

    def setTime(self):
        self.current_Time = pygame.time.get_ticks()

    # In this function we also make the bullets move
    def bulletBlit(self, screen):
        for x in range(len(self.bulletList)):
            self.bulletList[x].move()
            screen.blit(self.bulletList[x].entityImg, (self.bulletList[x].x, self.bulletList[x].y))

    def upgradeDisplay(self):

        spFont = pygame.font.Font('freesansbold.ttf', 40)
        spText = spFont.render(self.skilling, True, (0, 0, 0))

        if (pygame.time.get_ticks() - self.skillTimer < 1000) and self.skillLockout is True:
            self.screen.blit(spText, (10, 120))
        if (pygame.time.get_ticks() - self.skillTimer > 1000) and self.skillLockout is True:
            self.skillLockout = False
            self.skilling = " "

    def input(self):
        # Check if an event occurred, if it is a key down, then use it!

        for keyPress in pygame.event.get():
            if keyPress.type == pygame.KEYDOWN:

                if keyPress.key == pygame.K_LEFT:
                    self.change_x = -0.2 * self.speed
                    print("Left Pressed")
                if keyPress.key == pygame.K_RIGHT:
                    self.change_x = 0.2 * self.speed
                    print("Right Pressed")
                if keyPress.key == pygame.K_UP:
                    self.change_y = -0.2 * self.speed
                    print("Up Pressed")
                if keyPress.key == pygame.K_DOWN:
                    self.change_y = 0.2 * self.speed
                    print("Down Pressed")

                # Shooting mechanic

                if keyPress.key == pygame.K_w:
                    print("W Pressed")
                    self.keyPress = "W"
                    self.shooting = True

                if keyPress.key == pygame.K_a:
                    print("A Pressed")
                    self.keyPress = "A"
                    self.shooting = True

                if keyPress.key == pygame.K_s:
                    print("S Pressed")
                    self.keyPress = "S"
                    self.shooting = True

                if keyPress.key == pygame.K_d:
                    print("D Pressed")
                    self.keyPress = "D"
                    self.shooting = True

                if keyPress.key == pygame.K_1:
                    if self.skillpoints == 0 and self.skillLockout is False:
                        self.skillLockout = True
                        self.skilling = "NO SP"
                        self.skillTimer = pygame.time.get_ticks()

                    elif self.skillLockout is False:
                        self.skillLockout = True
                        self.skillpoints -= 1
                        self.ammo += 3
                        self.skilling = "Ammo increased"
                        self.skillTimer = pygame.time.get_ticks()

                if keyPress.key == pygame.K_2:
                    if self.skillpoints == 0 and self.skillLockout is False:
                        self.skillLockout = True
                        self.skilling = "NO SP"
                        self.skillTimer = pygame.time.get_ticks()

                    elif self.skillLockout is False:
                        self.skillLockout = True
                        self.skillpoints -= 1
                        self.firerate -= 20
                        self.skilling = "Firerate increased"
                        self.skillTimer = pygame.time.get_ticks()

                if keyPress.key == pygame.K_3:
                    if self.skillpoints == 0 and self.skillLockout is False:
                        self.skillLockout = True
                        self.skilling = "NO SP"
                        self.skillTimer = pygame.time.get_ticks()

                    elif self.skillLockout is False:
                        self.skillLockout = True
                        self.skillpoints -= 1
                        self.speed += 5
                        self.skilling = "Player speed increased"
                        self.skillTimer = pygame.time.get_ticks()


                if keyPress.key == pygame.K_4:
                    if self.skillpoints == 0 and self.skillLockout is False:
                        self.skillLockout = True
                        self.skilling = "NO SP"
                        self.skillTimer = pygame.time.get_ticks()

                    elif self.skillLockout is False:
                        self.skillLockout = True
                        self.skillpoints -= 1
                        self.health = 3
                        self.skilling = "Health Restored"
                        self.skillTimer = pygame.time.get_ticks()

                if keyPress.key == pygame.K_r:
                    if self.reloading is False:
                        self.reloadStart()

            if keyPress.type == pygame.KEYUP:
                if keyPress.key == pygame.K_LEFT:
                    self.change_x = 0 * self.speed
                    print("Left released")
                if keyPress.key == pygame.K_RIGHT:
                    self.change_x = 0 * self.speed
                    print("Right released")
                if keyPress.key == pygame.K_UP:
                    self.change_y = 0 * self.speed
                    print("Up released")
                if keyPress.key == pygame.K_DOWN:
                    self.change_y = 0 * self.speed
                    print("Down released")

                # stop the shooting when releasing the key
                if keyPress.key == pygame.K_w:
                    self.keyPress = ""
                    self.shooting = False
                if keyPress.key == pygame.K_a:
                    self.keyPress = ""
                    self.shooting = False
                if keyPress.key == pygame.K_s:
                    self.keyPress = ""
                    self.shooting = False
                if keyPress.key == pygame.K_d:
                    self.keyPress = ""
                    self.shooting = False

            if keyPress.type == pygame.QUIT:
                pygame.quit()

        self.move()

    def healthCheck(self):
        if self.invFrame is True:
            if (pygame.time.get_ticks() - self.hitTime) > self.invTime:
                self.invFrame = False

# this file is mainly for the ball class
from Background import *


# this function calculate the dimension of boundary
def boundaryElem():
    marginWidth = 35
    marginHeight = 17
    scoreTableHeight = 60
    topLeftX = marginWidth
    topLeftY = scoreTableHeight + marginHeight
    displayWidth = 1100
    displayHeight = 620
    fieldWidth = displayWidth - 2 * marginWidth
    fieldHeight = displayHeight - 2 * marginHeight
    return topLeftX, topLeftY, fieldWidth, fieldHeight,\
           marginWidth, marginHeight, scoreTableHeight,\
           displayWidth, displayHeight


# the move method of the ball is search
# on google in pygame documentation
# https://stackoverflow.com/questions/43171369/
# using-self-rect-centerx-in-pygame-to-move-character-at-random


# this is the class for soccer ball
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super(Ball, self).__init__()
        self.owner = None
        self.isMoving = False
        ballSize = 15
        ballImg = pygame.image.load('assets/images/ball/ball1.png')
        self.image = pygame.transform.scale(ballImg, (ballSize, ballSize))
        self.rect = self.image.get_rect()
        self.speed = (0, 0)
        self.friction = 0.95
        displayWidth = getGameDimension()[0]
        displayHeight = getGameDimension()[1]
        scoreTableHeight = getGameDimension()[3]
        self.rect.centerx = displayWidth // 2
        self.rect.centery = scoreTableHeight + displayHeight // 2.2
        self.boundary = pygame.Rect(boundaryElem()[0], boundaryElem()[1],
                                   boundaryElem()[2], boundaryElem()[3])

    # update the ball's position
    def update(self):
        offset = 20
        offset2 = 15
        if self.owner is not None:
            self.speed = (0, 0)
        elif self.owner is None and self.speed == (0, 0):
            self.isMoving = False
        elif self.owner is None and self.speed != (0, 0):
            self.rect.x += self.speed.x
            self.rect.y += self.speed.y
            # the soccer ball will stop moving due to the friction
            self.speed *= self.friction
            # check whether or not the ball is collide with
            # boundary of the soccer field
            if self.rect.x < self.boundary.left:
                self.rect.x = self.boundary.left
                self.speed.x = - self.speed.x
            elif self.rect.x > self.boundary.right - offset2:
                self.rect.x = self.boundary.right - offset2
                self.speed.x = - self.speed.x
            elif self.rect.y < self.boundary.top:
                self.rect.y = self.boundary.top
                self.speed.y = - self.speed.y
            elif self.rect.y > self.boundary.bottom - offset:
                self.rect.y = self.boundary.bottom - offset
                self.speed.y = - self.speed.y

    # this is the passBall method
    def passBall(self, vel):
        self.isMoving = True
        self.owner = None
        self.speed = vel

    # this is the shoot ball method
    def shoot(self, vel):
        self.isMoving = True
        self.owner = None
        self.speed = vel * 30

    # this method move's the ball to it's initial position
    def generateNewBall(self):
        displayWidth = getGameDimension()[0]
        displayHeight = getGameDimension()[1]
        scoreTableHeight = getGameDimension()[3]
        self.rect.centerx = displayWidth // 2
        self.rect.centery = scoreTableHeight + displayHeight // 2.2
        self.owner = None
        self.speed = (0, 0)

# this is the generate ball function
def generateBallObject():
    ball = Ball()
    return ball

ball = generateBallObject()

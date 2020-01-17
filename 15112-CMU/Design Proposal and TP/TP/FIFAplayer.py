# This file is mainly for the super class for all FIFA players
import pygame
from enum import Enum
from Ball import *
import os


# helper function for loading images
def loadImgHelper(path, team, FIFAPlayerSize, sprites, key):
    for filename in os.listdir(path + team + "/" + key + "/"):
        if filename.endswith(".png"):
            image = pygame.image.load(path + team + "/" + key + "/" + filename)
            resizedImage = pygame.transform.scale(image,
                                                  (FIFAPlayerSize, FIFAPlayerSize))
            if "-" not in key:
                sprites[key].append(resizedImage)
            else:
                if key == "up-right":
                    char = 'upRight'
                    sprites[char].append(resizedImage)
                elif key == "up-left":
                    char = 'upLeft'
                    sprites[char].append(resizedImage)
                elif key == "down-right":
                    char = 'downRight'
                    sprites[char].append(resizedImage)
                elif key == "down-left":
                    char = 'downLeft'
                    sprites[char].append(resizedImage)


# helper function for add Images to sprites
def addImagesToSprites(sprites, team, FIFAPlayerSize):
    path = "assets/images/player/"
    for key in sprites:
        if key == 'up':
            loadImgHelper(path, team, FIFAPlayerSize, sprites, key)
        if key == 'down':
            loadImgHelper(path, team, FIFAPlayerSize, sprites, key)
        if key == "right":
            loadImgHelper(path, team, FIFAPlayerSize, sprites, key)
        if key == 'left':
            loadImgHelper(path, team, FIFAPlayerSize, sprites, key)
        if key == 'upRight':
            directory = "up-right"
            loadImgHelper(path, team, FIFAPlayerSize, sprites, directory)
        if key == 'upLeft':
            directory = "up-left"
            loadImgHelper(path, team, FIFAPlayerSize, sprites, directory)
        if key == 'downRight':
            directory = "down-right"
            loadImgHelper(path, team, FIFAPlayerSize, sprites, directory)
        if key == 'downLeft':
            directory = "down-left"
            loadImgHelper(path, team, FIFAPlayerSize, sprites, directory)


# helper function for calculating distance between FIFAPlayers and the ball
def calculateDistanceBetweemBallAndPlayers(playerRect, ballRect):
    return (abs(playerRect[0] - ballRect[0])**2 + abs(playerRect[1] - ballRect[1])**2)



#  load distance values into dictionary
def loadDict(directions, runningSpeedX, runningSpeedY, distances, playerRect):
    runningSpeed = 6
    for direction in directions:
        playerRect1 = None
        ballRect = ball.rect
        if direction == "up":
            playerRect1 = (playerRect.centerx, playerRect.centery - runningSpeed)
        if direction == "down":
            playerRect1 = (playerRect.centerx, playerRect.centery + runningSpeed)
        if direction == "left":
            playerRect1 = (playerRect.centerx - runningSpeed, playerRect.centery)
        if direction == "right":
            playerRect1 = (playerRect.centerx + runningSpeed, playerRect.centery)
        if direction == "upLeft":
            playerRect1 = (playerRect.centerx - runningSpeedX,
                          playerRect.centery - runningSpeedY)
        if direction == "upRight":
            playerRect1 = (playerRect.centerx + runningSpeedX,
                          playerRect.centery - runningSpeedY)
        if direction == "downLeft":
            playerRect1 = (playerRect.centerx - runningSpeedX,
                          playerRect.centery + runningSpeedY)
        if direction == "downRight":
            playerRect1 = (playerRect.centerx + runningSpeedX,
                          playerRect.centery + runningSpeedY)
        distances[direction] = \
            calculateDistanceBetweemBallAndPlayers(playerRect1, ballRect)


#  load distance values into dictionary
def loadDict2(directions, runningSpeedX, runningSpeedY, distances, playerRect, goalZoneRect):
    runningSpeed = 5
    for direction in directions:
        playerRect1 = None
        if direction == "up":
            playerRect1 = (playerRect.centerx, playerRect.centery - runningSpeed)
        if direction == "down":
            playerRect1 = (playerRect.centerx, playerRect.centery + runningSpeed)
        if direction == "left":
            playerRect1 = (playerRect.centerx - runningSpeed, playerRect.centery)
        if direction == "right":
            playerRect1 = (playerRect.centerx + runningSpeed, playerRect.centery)
        if direction == "upLeft":
            playerRect1 = (playerRect.centerx - runningSpeedX,
                          playerRect.centery - runningSpeedY)
        if direction == "upRight":
            playerRect1 = (playerRect.centerx + runningSpeedX,
                          playerRect.centery - runningSpeedY)
        if direction == "downLeft":
            playerRect1 = (playerRect.centerx - runningSpeedX,
                          playerRect.centery + runningSpeedY)
        if direction == "downRight":
            playerRect1 = (playerRect.centerx + runningSpeedX,
                          playerRect.centery + runningSpeedY)
        distances[direction] = \
            calculateDistanceBetweemGoalZoneAndPlayers(playerRect1, goalZoneRect)


# this is a small probability event generate function
def ballBeenCutIsSmallProb():
    import random
    if random.randint(0, 1000) <= 2:
        return True

# this is the helper function to calculate distance between players and goalZone
def calculateDistanceBetweemGoalZoneAndPlayers(playerRect, goalZoneRect):
    return (abs(playerRect[0] - 0)**2 + abs(playerRect[1] - goalZoneRect.centery)**2)


# this subclass of Enum is searched by google
# from https://stackoverflow.com/questions/36932/how-can-i-represent-an-enum-in-python
class GameState(Enum):
    findBall = 1
    free = 2
    attacking = 3
    computer = 4


class FIFAPlayer(pygame.sprite.Sprite):
    # cite the structure of my class __init__ is followed by 112 TA's slide
    # Dot class example like self.image self.rect and so on
    def __init__(self, centerx, centery, team):
        super(FIFAPlayer, self).__init__()
        self.FIFAPlayerSize = 60
        self.originalX = centerx
        self.originalY = centery
        self.velocity = pygame.Vector2(0, 0)
        # This is the total eight directions
        self.directions = ['up', 'down', 'right', 'left',
                           'upRight', 'upLeft', 'downRight',
                           'downLeft']
        self.sprites = dict()
        for direction in self.directions:
            self.sprites[direction] = []
        addImagesToSprites(self.sprites, team, self.FIFAPlayerSize)
        if team == 'blue-team':
            # this is the start direction when the game begin
            self.direction = 'right'
        elif team == 'red-team':
            # this is the start direction when the game begin
            self.direction = 'left'
        self.images = self.sprites[self.direction]
        # this is the start image when the game begin and
        # it also the first image when change direction
        self.image = self.images[0]
        self.rect = pygame.Rect(centerx - self.FIFAPlayerSize / 2,
                                centery - self.FIFAPlayerSize / 2,
                                self.FIFAPlayerSize, self.FIFAPlayerSize)
        # the purpose for player rect is to cut the real player out of the image
        # since self.rect is the Rect of image not the real player
        # and the real player is smaller than the image
        self.playerRect = pygame.Rect(self.rect.centerx - self.FIFAPlayerSize / 3.8,
                                      self.rect.centery,
                                      self.FIFAPlayerSize / 4,
                                      self.FIFAPlayerSize / 4)
        self.validFieldRect = pygame.Rect(boundaryElem()[4], boundaryElem()[5] + boundaryElem()[6],
                                          boundaryElem()[2], boundaryElem()[3])
        self.runningSpeed = 6
        self.gameState = GameState.free
        self.goalZoneRect = pygame.Rect(boundaryElem()[4],
                                        (boundaryElem()[5]+boundaryElem()[6] +
                                         1 / 3 * (boundaryElem()[3]) - 50), 150, 300)
        self.goalZoneRect2 = pygame.Rect(boundaryElem()[4] + boundaryElem()[2] - 250,
                                        (boundaryElem()[5] + boundaryElem()[6] +
                                         1 / 3 * (boundaryElem()[3]) - 50), 150, 300)


    # this function is used to update the direction of players
    def updateDirect(self, direction):
        self.direction = direction
        self.images = self.sprites[self.direction]
        self.image = self.images[1]


    # this is the helper function for move method
    def moveHelper(self, direction, runningSpeedX, runningSpeedY):
        if direction == 'up':
            if self.validFieldRect.contains\
                        (self.playerRect.move(0, -self.runningSpeed)):
                self.rect = self.rect.move(0, -self.runningSpeed)
        elif direction == 'down':
            if self.validFieldRect.contains\
                        (self.playerRect.move(0, self.runningSpeed)):
                self.rect = self.rect.move(0, self.runningSpeed)
        elif direction == 'left':
            if self.validFieldRect.contains\
                        (self.playerRect.move(-self.runningSpeed, 0)):
                self.rect = self.rect.move(-self.runningSpeed, 0)
        elif direction == 'right':
            if self.validFieldRect.contains\
                        (self.rect.move(0, self.runningSpeed)):
                self.rect = self.rect.move(self.runningSpeed, 0)
        elif direction == 'upLeft':
            if self.validFieldRect.contains\
                        (self.playerRect.move(-runningSpeedX, -runningSpeedY)):
                self.rect = self.rect.move(-runningSpeedX, -runningSpeedY)
        elif direction == 'upRight':
            if self.validFieldRect.contains\
                        (self.playerRect.move(runningSpeedX, -runningSpeedY)):
                self.rect = self.rect.move(runningSpeedX, -runningSpeedY)
        elif direction == 'downLeft':
            if self.validFieldRect.contains\
                        (self.playerRect.move(-runningSpeedX, runningSpeedY)):
                self.rect = self.rect.move(-runningSpeedX, runningSpeedY)
        elif direction == 'downRight':
            if self.validFieldRect.contains\
                        (self.playerRect.move(runningSpeedX, runningSpeedY)):
                self.rect = self.rect.move(runningSpeedX, runningSpeedY)

    # I searched the move rect method like rect.move() on pygame
    # documentaion, here is the link
    # https://github.com/search?q=pygame.Rect.move&type=Code
    # this is the move method for FIFAPlayer
    def move(self, direction):
        runningSpeedX = self.runningSpeed / (2 ** 0.5)
        runningSpeedY = runningSpeedX
        self.updateDirect(direction)
        if ball.owner == self:
            self.afterPlayerMoveUpdateBall()
        self.moveHelper(direction, runningSpeedX, runningSpeedY)




    # This is the update method for FIFAPlayer
    def update(self):
        self.playerRect = pygame.Rect(self.rect.centerx - self.FIFAPlayerSize / 3.8,
                                      self.rect.centery,
                                      self.FIFAPlayerSize / 4,
                                      self.FIFAPlayerSize / 4)

    # this is the shoot method for FIFAPlayer in this method
    # since the ball is global I can call the ball's shoot method
    def shoot(self):
        self.runningSpeed = 6
        if ball.owner == self:
            if self.direction == 'left':
                vel = pygame.Vector2(-1, 0).normalize()
                ball.shoot(vel)
            elif self.direction == 'right':
                vel = pygame.Vector2(1, 0).normalize()
                ball.shoot(vel)
            elif self.direction == 'up':
                vel = pygame.Vector2(0, -1).normalize()
                ball.shoot(vel)
            elif self.direction == 'down':
                vel = pygame.Vector2(0, 1).normalize()
                ball.shoot(vel)
            elif self.direction == 'upRight':
                vel = pygame.Vector2(1, -1).normalize()
                ball.shoot(vel)
            elif self.direction == 'upLeft':
                vel = pygame.Vector2(-1, -1).normalize()
                ball.shoot(vel)
            elif self.direction == 'downRight':
                vel = pygame.Vector2(1, 1).normalize()
                ball.shoot(vel)
            elif self.direction == 'downLeft':
                vel = pygame.Vector2(-1, 1).normalize()
                ball.shoot(vel)


    # this is the cross ball method of FIFA player
    def crossBall(self):
        self.runningSpeed = 6
        if ball.owner == self:
            directionVector = pygame.Vector2(self.goalZoneRect2.centerx
                                             - self.rect.centerx,
                                            self.goalZoneRect2.centery
                                             - self.rect.centery)
            vel = directionVector.normalize()
            ball.shoot(vel)


    # this is the helper function for finding ball
    def changeGameState(self):
        self.gameState = GameState.computer
        self.getBall()


    # this is the helper function for find ball method
    def findBallHelper(self):
        if ball.owner != None:
            # the probability of ball been cut off by redTeam(computer)
            # when the ball is controlled by blueTeam(player)
            if ballBeenCutIsSmallProb():
                self.changeGameState()
        elif ball.owner == None:
            # the ball is controlled by nobody, computer will get the ball
            self.changeGameState()


    # this is the run to find ball method for FIFA players
    def runToFindBall(self):
        # prevent the case when blueTeam player shoot
        # been cut off by red team player
        if ball.owner == None:
            # since the min passBall speed vector's length is 15
            if (ball.speed[0] ** 2 +
                ball.speed[1] **2 ) ** 0.5 > 10:
                return None
        runningSpeedX = self.runningSpeed / (2 ** 0.5)
        runningSpeedY = runningSpeedX
        # the ball is controlled by computer
        if ball.owner == self:
            return None
        distances = dict()
        loadDict(self.directions, runningSpeedX,
                 runningSpeedY, distances, self.playerRect)
        minDistance = distances["down"]
        minDirection = "down"
        # select the direction which has the min distance to the ball
        for key in distances:
            if distances[key] < minDistance:
                minDistance = distances[key]
                minDirection = key
        self.move(minDirection)
        self.findBallHelper()


    # this is the get ball method and self is blue or red team player object
    def getBall(self):
        if ball.owner != self:
            if self.playerRect.colliderect(ball.rect):
                ball.owner = self


    # this method update ball's position after the ball was get by FIFAPlayer
    def afterPlayerMoveUpdateBall(self):
        if ball.owner == self:
            if self.direction == "up":
                # this is the ball's position relative to the players
                # makes the screen look better
                ball.rect.centery = self.rect.centery + self.FIFAPlayerSize / 4
            elif self.direction == "down":
                ball.rect.centery = self.rect.centery + self.FIFAPlayerSize / 4
            elif self.direction == "left":
                ball.rect.centerx = self.rect.centerx - self.FIFAPlayerSize / 6
            elif self.direction == "right":
                ball.rect.centerx = self.rect.centerx + self.FIFAPlayerSize / 6
            else:
                # for directions like upRight,upLeft, downLeft and downRight
                ball.rect.centerx = self.rect.centerx
                ball.rect.centery = self.rect.centery + self.FIFAPlayerSize / 3


    # this is the function to implement game AI to
    # bLue and red team players and it is also the
    # most difficult part of this game
    def aiMove(self, aIMoveUp, aIMoveDown, aIMoveLeft, aIMoveRight):
        offset = 100
        if aIMoveUp and aIMoveLeft:
            self.move('upLeft')
        elif aIMoveUp and aIMoveRight:
            self.move('upRight')
        elif aIMoveDown and aIMoveLeft:
            self.move('downLeft')
        elif aIMoveDown and aIMoveRight:
            self.move('downRight')
        elif aIMoveLeft and self.rect.centerx > offset:
            self.move('left')
        elif aIMoveRight and self.rect.centerx < \
                boundaryElem()[7] - offset:
            self.move('right')
        elif aIMoveUp:
            self.move('up')
        elif aIMoveDown:
            self.move('down')


    # this is the gameAi helper function basically
    # using the difference of player's original position and its
    # current postion on the screen to implement the game AI
    # the reason why I add the offset is if offset == 0,
    # there will be some error if I don't move my current player
    # following is  my ai helper function which gives a series of bool values
    # on whether to move up, down, right, left, upLeft, upRight, downLeft, downRight
    def aiHelper(self, team):
        offset = 15
        aIMoveRight = True if self.rect.centerx - self.originalX + offset \
                          < team.player.rect.centerx - team.player.originalX else False
        aIMoveLeft = True if self.rect.centerx - self.originalX - offset \
                         > team.player.rect.centerx - team.player.originalX else False
        aIMoveUp = True if self.rect.centery - self.originalY > offset else False
        aIMoveDown = True if - (self.rect.centery - self.originalY) > offset else False
        self.aiMove(aIMoveUp, aIMoveDown, aIMoveLeft, aIMoveRight)


    # this is the gameAI main function
    def teamPlayerAI(self, team):
        if self.gameState == GameState.computer:
            runningSpeedX = 5 / (2 ** 0.5)
            runningSpeedY = runningSpeedX
            distances = dict()
            playerRect = team.player.rect
            loadDict2(self.directions, runningSpeedX,
                      runningSpeedY, distances, playerRect, self.goalZoneRect)
            minDistance = distances["down"]
            minDirection = "down"
            for key in distances:
                if distances[key] < minDistance:
                    minDistance = distances[key]
                    minDirection = key
            self.move(minDirection)
            squareOfdistance = 60000
            if calculateDistanceBetweemGoalZoneAndPlayers\
                        (self.rect, self.goalZoneRect) < squareOfdistance:
                self.shoot()
        elif self.gameState == GameState.attacking:
            if self != team.player:
                self.aiHelper(team)
        elif self.gameState == GameState.findBall:
            self.runToFindBall()


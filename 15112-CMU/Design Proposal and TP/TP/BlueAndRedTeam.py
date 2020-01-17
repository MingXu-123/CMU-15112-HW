# this file is mainly for class BlueAndRedTeam, class blueTeam, class redTeam
from playerAndComputer import *
import pygame


# this function get the element value of game
def getElem():
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


# get the player's direction vector
def getDirectionVector(direction):
    if direction == 'left':
        vector = pygame.Vector2(-1, 0).normalize()
        return vector
    elif direction == 'right':
        vector = pygame.Vector2(1, 0).normalize()
        return vector
    elif direction == 'up':
        vector = pygame.Vector2(0, -1).normalize()
        return vector
    elif direction == 'down':
        vector = pygame.Vector2(0, 1).normalize()
        return vector
    elif direction == 'upRight':
        vector = pygame.Vector2(1, -1).normalize()
        return vector
    elif direction == 'upLeft':
        vector = pygame.Vector2(-1, -1).normalize()
        return vector
    elif direction == 'downRight':
        vector = pygame.Vector2(1, 1).normalize()
        return vector
    elif direction == 'downLeft':
        vector = pygame.Vector2(-1, 1).normalize()
        return vector


# this is the helper function help to calculate the angle between two team players
def calculateAngleBetweenTwoPlayers(directionVector, comparingVector):
    return abs(directionVector.angle_to(comparingVector))


# this is the helper function to resize the velocity
def reSizeVel(passVelVector):
    passVelVectorLen = (passVelVector[0]**2
                        + passVelVector[1]**2)**0.5
    if passVelVectorLen > 400:
        passVelVector = passVelVector.normalize() * 30
        return passVelVector
    elif passVelVectorLen > 300:
        passVelVector = passVelVector.normalize() * 25
        return passVelVector
    elif passVelVectorLen > 200:
        passVelVector = passVelVector.normalize() * 15
        return passVelVector
    elif passVelVectorLen > 100:
        passVelVector = passVelVector.normalize() * 14
        return passVelVector
    elif passVelVectorLen <= 100:
        passVelVector = passVelVector.normalize() * 14
        return passVelVector



class BlueAndRedTeam(pygame.sprite.Group):
    def __init__(self):
        super(BlueAndRedTeam, self).__init__()
        self.players = []
        self.player = None

    # this method choose the closest team player near the ball
    def chooseClosestTeamPlayer(self):
        distanceDict = dict()
        for player in self.players:
            distance = calculateDistanceBetweemBallAndPlayers\
                (player.rect, ball.rect)
            distanceDict[player] = distance
        minDistance = calculateDistanceBetweemBallAndPlayers\
            (self.players[0].playerRect.center, ball.rect.center)
        minPlayer = self.players[0]
        for player, distance in distanceDict.items():
            if distance <= minDistance:
                minDistance = distance
                minPlayer = player
        return minPlayer

    # this method change the controlled player
    def changePlayer(self):
        self.player.runningSpeed = 6
        if ball.owner != self:
            self.player = self.chooseClosestTeamPlayer()
            self.player.gameState = GameState.free


    # the method pass ball to its team members
    def passBallToTeamMembers(self):
        self.player.runningSpeed = 6
        curDirection = self.player.direction
        direcVect = getDirectionVector(curDirection)
        targetPlayers = []
        angleDict = dict()
        for player in self.players:
            if player != self.player:
                targetPlayers += [player]
        for player in targetPlayers:
            comparingVector = pygame.Vector2(player.rect.x - self.player.rect.x,
                                             player.rect.y - self.player.rect.y)
            angle = calculateAngleBetweenTwoPlayers(direcVect, comparingVector)
            angleDict[player] = angle
        targetPlayer = targetPlayers[0]
        vector0 = pygame.Vector2(targetPlayer.rect.x - self.player.rect.x,
                                 targetPlayer.rect.y - self.player.rect.y)
        minAngle = calculateAngleBetweenTwoPlayers(direcVect, vector0)
        for player, angle in angleDict.items():
            if angle <= minAngle:
                minAngle = angle
                targetPlayer = player
        if minAngle < 90:
            passVelVector = pygame.Vector2\
                (targetPlayer.rect.x - self.player.rect.x,
                 targetPlayer.rect.y - self.player.rect.y)
            passVelVector = reSizeVel(passVelVector)
            self.player = targetPlayer
            ball.passBall(passVelVector)
            self.player.gameState = GameState.free
        else:
            passVelVector = direcVect * 15
            ball.passBall(passVelVector)
            self.player.gameState = GameState.free


# return coordiinate of middle fielder's x and y
def getMiddleCoordinate():
    CoordinateOfMidfielderX = getElem()[4] + (2 / 7) * getElem()[2]
    CoordinateOfMidMidfielderY = getElem()[6] + getElem()[5] + getElem()[3] / 2
    return CoordinateOfMidfielderX, CoordinateOfMidMidfielderY

# return coordiinate of defender's x and y
def getDefendersCoordinate():
    CoordinateOfDefenderX = getElem()[4] + (1 / 7) * getElem()[2]
    CoordinateOfMidMidfielderY = getElem()[6] + getElem()[5] + getElem()[3] / 2
    CoordinateOfDefenderY = CoordinateOfMidMidfielderY - (1 / 6) * getElem()[3]
    CoordinateOfDefenderX1 = CoordinateOfDefenderX
    CoordinateOfDefenderY1 = CoordinateOfMidMidfielderY + (1 / 6) * getElem()[3]
    return CoordinateOfDefenderX, CoordinateOfDefenderY,\
           CoordinateOfDefenderX1, CoordinateOfDefenderY1

# return coordiinate of striker's x and y
def getStrikersCoordinate():
    CoordinateOfStrikerX = getElem()[4] + (3 / 7) * getElem()[2]
    CoordinateOfMidMidfielderY = getElem()[6] + getElem()[5] + getElem()[3] / 2
    CoordinateOfStrikerY = CoordinateOfMidMidfielderY - (1 / 6) * getElem()[3]
    CoordinateOfStrikerX1 = CoordinateOfStrikerX
    CoordinateOfStrikerY1 = CoordinateOfMidMidfielderY + (1 / 6) * getElem()[3]
    return CoordinateOfStrikerX, CoordinateOfStrikerY,\
           CoordinateOfStrikerX1, CoordinateOfStrikerY1



# helper functioin to add player objects
def addPlayersIntoBlueTeam():
    res = [
        # two defenders
        Player(getDefendersCoordinate()[0], getDefendersCoordinate()[1]),
        Player(getDefendersCoordinate()[2], getDefendersCoordinate()[3]),
        # three midfielders
        Player(getMiddleCoordinate()[0],
               getMiddleCoordinate()[1] - (1 / 3) * getElem()[3]),
        Player(getMiddleCoordinate()[0], getMiddleCoordinate()[1]),
        Player(getMiddleCoordinate()[0],
               getMiddleCoordinate()[1] + (1 / 3) * getElem()[3]),
        # two strikers
        Player(getStrikersCoordinate()[0], getStrikersCoordinate()[1]),
        Player(getStrikersCoordinate()[2], getStrikersCoordinate()[3]),
    ]
    return res


# helper functioin to add player objects
def addPlayersIntoRedTeam():
    res = [
        # two defenders
        Computer(getElem()[7] - getDefendersCoordinate()[0], getDefendersCoordinate()[1]),
        Computer(getElem()[7] - getDefendersCoordinate()[0], getDefendersCoordinate()[3]),
        # three midfielders
        Computer(getElem()[7] - getMiddleCoordinate()[0],
                 getMiddleCoordinate()[1] - (1 / 3) * getElem()[3]),
        Computer(getElem()[7] - getMiddleCoordinate()[0], getMiddleCoordinate()[1]),
        Computer(getElem()[7] - getMiddleCoordinate()[0],
                 getMiddleCoordinate()[1] + (1 / 3) * getElem()[3]),
        # two strikers
        Computer(getElem()[7] - getStrikersCoordinate()[0], getStrikersCoordinate()[1]),
        Computer(getElem()[7] - getStrikersCoordinate()[0], getStrikersCoordinate()[3]),
    ]
    return res


# this is a group class
class BlueTeam(BlueAndRedTeam):
    def __init__(self):
        super(BlueTeam, self).__init__()
        self.players = addPlayersIntoBlueTeam()
        for player in self.players:
            self.add(player)
        self.player = self.players[-1]

    # control method for blue team
    def controlPlayer(self):
        self.player.control()
        self.player.gameState = GameState.free
        for player in self.players:
            if player != self.player:
                player.gameState = GameState.attacking
        aiPlayers = []
        for player in self.players:
            if player != self.player:
                aiPlayers += [player]
        for player in aiPlayers:
            player.teamPlayerAI(self)

    # this is the speed up method for blueTeam Player
    def speedup(self):
        for player in self.players:
            if player == self.player:
                player.runningSpeed = 12


    # this method basically draw the arrow on the player has been controlled
    def drawArrow(self, gameDisplay):
        sizeOfArrow = 15
        FIFAPlayerSize = 60
        arrowImg = pygame.image.load("assets/images/others/sort-down-fill.png")
        resizedArrowImg = pygame.transform.scale(arrowImg, (sizeOfArrow, sizeOfArrow))
        gameDisplay.blit(resizedArrowImg, (self.player.rect.centerx - sizeOfArrow / 2,
                                           self.player.rect.centery - 2 / 3 * FIFAPlayerSize))


class RedTeam(BlueAndRedTeam):
    def __init__(self):
        super(RedTeam, self).__init__()
        self.players = addPlayersIntoRedTeam()
        for player in self.players:
            self.add(player)
        self.player = self.players[-1]


    # control method for red team
    def controlAI(self):
        if ball.owner != self.player:
            for player in self.players:
                if player != self.player:
                    player.gameState = GameState.attacking
            self.player.gameState = GameState.free
            self.player = self.chooseClosestTeamPlayer()
            self.player.gameState = GameState.findBall
        elif ball.owner == self.player:
            self.player.gameState = GameState.computer
        for player in self.players:
            player.teamPlayerAI(self)



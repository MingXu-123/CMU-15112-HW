# this file is mainly for class GameControl
import pygame
from Colors import *
from Ball import boundaryElem
from Ball import ball


class GameControl(object):
    def __init__(self):
        self.isBlueTeamGoal = True
        self.isRedTeamGoal = True
        self.blueTeamScore = 0
        self.redTeamScore = 0
        self.goalZoneRectForBlue = pygame.Rect(boundaryElem()[4],
                                        (boundaryElem()[5] + boundaryElem()[6] +
                                         1 / 3 * (boundaryElem()[3])), 10, 200)
        self.goalZoneRectForRed = pygame.Rect(boundaryElem()[4] + boundaryElem()[2] - 10,
                                         (boundaryElem()[5] + boundaryElem()[6] +
                                          1 / 3 * (boundaryElem()[3])), 150, 200)
        self.font1 = pygame.font.Font('assets/fonts/Muli-Regular.ttf', 30)
        self.font2 = pygame.font.Font('assets/fonts/Muli-Bold.ttf', 30)


    # this method is to check whether team play has goal
    def teamISGoal(self):
        if ball.rect.colliderect(self.goalZoneRectForBlue):
            self.redTeamScore += 1
            return self.isBlueTeamGoal
        elif ball.rect.colliderect(self.goalZoneRectForRed):
            self.blueTeamScore += 1
            return self.isRedTeamGoal
        else:
            return False


    # cite I write generate Text according to this link's code
    # https://github.com/ilaishai/dotchaser/blob/b1e26fe62e54429
    # afd1689c1051a201fe79f5a79/venv/Lib/site-packages/pygame/tests/font_test.py


    # this is the generate score on gameDisPlay
    def generateScore(self, text, color, gameDisplay, coordinateX):
        import random
        fontLst = [self.font1, self.font2]
        font = random.choice(fontLst)
        surface = font.render(text, True, color)
        surfaceRect = surface.get_rect()
        halfHeightOfScoreTable = 30
        surfaceRect.center = (coordinateX, halfHeightOfScoreTable)
        gameDisplay.blit(surface, surfaceRect)


    # this is the draw score main function
    def drawScore(self, gameDisplay):
        text1 = 'Blue Team: '
        color1 = Colors.Blue
        text2 = str(self.blueTeamScore)
        text3 = 'Red Team: '
        color2 = Colors.Red
        text4 = str(self.redTeamScore)
        self.generateScore(text1, color1, gameDisplay, 450)
        self.generateScore(text2, color1, gameDisplay, 550)
        self.generateScore(text3, color2, gameDisplay, 660)
        self.generateScore(text4, color2, gameDisplay, 750)




# this file only contains the required background class
import pygame
from Colors import *
pygame.init()

def getGameDimension():
    displayWidth = 1100
    displayHeight = 680
    scoreTableWidth = displayWidth
    scoreTableHeight = 60
    return (displayWidth, displayHeight, scoreTableWidth, scoreTableHeight)


class Background(pygame.Surface):
    def __init__(self):
        super(Background, self).__init__((getGameDimension()[0], getGameDimension()[1]))
        # the rect is the score table of this game
        pygame.draw.rect(self, Colors().FloralWhite,
                         (0, 0, getGameDimension()[2], getGameDimension()[3]))
        backgroundImg = pygame.image.load('./assets/images/field/soccer-field.png')
        backgroundImg2 = pygame.image.load('./assets/images/background/WechatIMG174.png')
        backgroundImg3 = pygame.image.load('./assets/images/background/WechatIMG173.png')
        resizedbackgroundImg2 = pygame.transform.scale(backgroundImg2, (1100, 60))
        resizedbackgroundImg3 = pygame.transform.scale(backgroundImg3, (300, 60))
        self.blit(backgroundImg, (0, getGameDimension()[3]))
        self.blit(resizedbackgroundImg2, (0, 0))
        self.blit(resizedbackgroundImg3, (800, 0))




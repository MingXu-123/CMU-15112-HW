import pygame
import colors
from const import *
from Text import *

pygame.init()

WIDTH = WITH_SETTING_BOARD
HEIGHT = HEIGHT_SETTING_BOARD

MARGIN = WIDTH / 6
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 50
class SettingBoard(pygame.Surface):
  def __init__(self): 
    super(SettingBoard, self).__init__((WIDTH, HEIGHT))
    self.fill(colors.Blue)
    Text.showSettingText('SETTING', colors.White,self, TABLE_SCORE_HEIGHT)
    self.newGameRect = self.makeButton("NEW GAME", TABLE_SCORE_HEIGHT*1, 20 )
    self.pVp = self.makeButton("PvP", TABLE_SCORE_HEIGHT*2, 70 )
    self.computer =  self.makeButton("COMPUTER", TABLE_SCORE_HEIGHT*3, 30 )

  def renderSettingButton(self):
    self.settingButton("SETTING", 0, 700)

  def makeButton(self ,s, hight , margin=0):
    rect = pygame.Rect(MARGIN ,  hight*3 , WIDTH_OF_PAUSE_GAME - MARGIN*2, BUTTON_HEIGHT)
    titleSurf, titleRect = Text.makeTextObject(s, colors.Green)
    pygame.draw.rect(self, colors.Black, rect)
    self.blit(titleSurf, (MARGIN + margin,  hight*3 + 5 , WIDTH_OF_PAUSE_GAME - MARGIN*2, BUTTON_HEIGHT))
    return rect

  def click(self, x, y ):
    x = x - (WINDOW_WIDTH - WIDTH) / 2
    y = y - (WINDOW_HEIGHT - HEIGHT) / 2
    if( self.newGameRect.collidepoint(x,y)):
      return self.handleNewGame()
    if( self.pVp.collidepoint(x,y)):
      return self.handlepVp()
    if( self.computer.collidepoint(x,y)):
      return self.handleComputer()
  
  def handleNewGame(self):
    return 1
  def handlepVp(self):
    print(2222)  
  def handleComputer(self):
    print(3333)  

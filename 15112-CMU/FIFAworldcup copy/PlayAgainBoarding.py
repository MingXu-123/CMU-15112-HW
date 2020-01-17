import pygame
import colors
from const import *
from Text import *

pygame.init()

WIDTH = WIDTH_OF_PLAY_AGAIN_BOARDING
HEIGHT = HEIGHT_OF_PLAY_AGAIN_BOARDIG

MARGIN = WIDTH / 6
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 50

class PlayAgainBoarding(pygame.Surface):
  def __init__(self):
    super(PlayAgainBoarding, self).__init__((WIDTH, HEIGHT))
    self.fill(colors.LightGreen)
    pygame.draw.rect(self, colors.LightGreen, (0, 0, WIDTH, HEIGHT))

    Text.showTextInPlayGain('Do you want to play again?', colors.White, self, HEIGHT / 3)

    y = HEIGHT * 2 / 3
    # yes
    titleSurf, titleRect = Text.makeTextObject('YES', colors.Green)
    titleRect.center = (MARGIN + BUTTON_WIDTH / 2, y)

    self.yes_rect = pygame.Rect(MARGIN, y - BUTTON_HEIGHT / 2, BUTTON_WIDTH, BUTTON_HEIGHT)
    
    pygame.draw.rect(self, colors.White, self.yes_rect)
    self.blit(titleSurf, titleRect)

    # no
    titleSurf, titleRect = Text.makeTextObject('NO', colors.Red)
    titleRect.center = (WIDTH - MARGIN - BUTTON_WIDTH / 2, y)
    
    self.no_rect = pygame.Rect(WIDTH - MARGIN - BUTTON_WIDTH, y - BUTTON_HEIGHT / 2, BUTTON_WIDTH, BUTTON_HEIGHT)

    pygame.draw.rect(self, colors.White, self.no_rect)
    self.blit(titleSurf, titleRect)

  def click(self, x, y):
    # convert to the coordinates of this surface
    x = x - (WINDOW_WIDTH - WIDTH) / 2
    y = y - (WINDOW_HEIGHT - HEIGHT) / 2
    
    if self.yes_rect.collidepoint(x, y):
      return True
    if self.no_rect.collidepoint(x, y):
      return False

    return None
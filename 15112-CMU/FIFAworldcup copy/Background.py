import pygame
import colors
from const import *

PATH = './assets/images/field/soccer-field.png'

pygame.init()

class Background(pygame.Surface):
  def __init__(self):
    super(Background, self).__init__((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.draw.rect(self, colors.Gainsboro, (0, 0, TABLE_SCORE_WIDTH, TABLE_SCORE_HEIGHT))

    img = pygame.image.load(PATH)
    self.blit(img, (0, TABLE_SCORE_HEIGHT))
    
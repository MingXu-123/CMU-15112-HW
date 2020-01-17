import pygame
import os
import time

from const import *
from functions import *
from FBPlayer import *

class Computer(FBPlayer):
  def __init__(self, centerx, centery):
    super(Computer, self).__init__(RED_TEAM, centerx, centery)

  # def handle(self, ball):
  #   pass

  # def leadToGoal(self):
  #   # goalRect = pygame.Rect(0, TABLE_SCORE_HEIGHT + GAME_HEIGHT / 2 - 100, 50, 200)
  #   #
  #   # distances = {
  #   #   UP: caculateDistance((self.controlRect.centerx, self.controlRect.centery - SPEED_DEFAULT), goalRect.center),
  #   #   DOWN: caculateDistance((self.controlRect.centerx, self.controlRect.centery + SPEED_DEFAULT), goalRect.center),
  #   #   RIGHT: caculateDistance((self.controlRect.centerx + SPEED_DEFAULT, self.controlRect.centery), goalRect.center),
  #   #   LEFT: caculateDistance((self.controlRect.centerx - SPEED_DEFAULT, self.controlRect.centery), goalRect.center),
  #   #   UP_LEFT: caculateDistance((self.controlRect.centerx - SPEED_DEFAULT / SQRT_2, self.controlRect.centery  - SPEED_DEFAULT / SQRT_2), goalRect.center),
  #   #   UP_RIGHT: caculateDistance((self.controlRect.centerx + SPEED_DEFAULT / SQRT_2, self.controlRect.centery  - SPEED_DEFAULT / SQRT_2), goalRect.center),
  #   #   DOWN_LEFT: caculateDistance((self.controlRect.centerx - SPEED_DEFAULT / SQRT_2, self.controlRect.centery  + SPEED_DEFAULT / SQRT_2), goalRect.center),
  #   #   DOWN_RIGHT: caculateDistance((self.controlRect.centerx + SPEED_DEFAULT / SQRT_2, self.controlRect.centery  + SPEED_DEFAULT / SQRT_2), goalRect.center),
  #   # }
  #   #
  #   # direction = UP
  #   # distance = distances[UP]
  #   #
  #   # for key, value in distances.items():
  #   #   if value < distance:
  #   #     distance = value
  #   #     direction = key
  #   #
  #   # if distance < 1:
  #   #   return
  #   #
  #   # self.updateDirection(direction)
  #   # self.move(direction)
  #   pass



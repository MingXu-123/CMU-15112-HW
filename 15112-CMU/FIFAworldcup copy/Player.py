import pygame
import os
import time

from const import *
from FBPlayer import *
from Ball import BALL

DISTANCE_NEW_FRAME = 20

class Player(FBPlayer):
  def __init__(self, centerx, centery):
    super(Player, self).__init__(BLUE_TEAM, centerx, centery)

  def handle(self):
    keys = pygame.key.get_pressed()  # take pressed keys

    # update direction
    if keys[pygame.K_UP] and keys[pygame.K_LEFT]:
      self.move(UP_LEFT)
    elif keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
      self.move(UP_RIGHT)
    elif keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
      self.move(DOWN_LEFT)
    elif keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
      self.move(DOWN_RIGHT)
    elif keys[pygame.K_UP]:
      self.move(UP)
    elif keys[pygame.K_DOWN]:
      self.move(DOWN)
    elif keys[pygame.K_LEFT]:
      self.move(LEFT)
    elif keys[pygame.K_RIGHT]:
      self.move(RIGHT)

    # if BALL.owner == None:
    #   length = BALL.velocity.length()
    #   if length < 2:
    #     self.takeBall()


    
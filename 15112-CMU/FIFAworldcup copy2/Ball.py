import pygame
import os
import time

from const import *

SIZE = 12

class Ball(pygame.sprite.Sprite):
  def __init__(self):
    super(Ball, self).__init__()

    self.owner = None
    self.isRolling = False

    image = pygame.image.load('assets/images/ball/ball.png')
    self.image = pygame.transform.scale(image, (SIZE, SIZE))
    self.rect = self.image.get_rect()
    self.rect.centerx = BACKGROUND_WIDTH / 2
    self.rect.centery = TABLE_SCORE_HEIGHT + BACKGROUND_HEIGHT / 2

    # self.rect.x = BACKGROUND_WIDTH / 2
    # self.rect.y = TABLE_SCORE_HEIGHT + BACKGROUND_HEIGHT / 2

    self.velocity = pygame.Vector2(0, 0)
    self.friction = 0.97
    self.fieldSize = pygame.Rect(TOP_LEFT[0], TOP_LEFT[1], GAME_WIDTH, GAME_HEIGHT)

  def update(self, blueTeam, redTeam):
    if self.owner != None:
      self.velocity = pygame.Vector2(0, 0)
    elif self.owner == None and self.velocity == (0, 0):
      self.isRolling = False
    # else:
    elif self.owner == None and self.velocity != (0, 0):
      self.rect.x += self.velocity.x
      self.rect.y += self.velocity.y
      #friction
      self.velocity *= self.friction
      
      if abs(self.velocity.x) < 1:
        self.velocity.x = 0
      if abs(self.velocity.y) < 1:
        self.velocity.y = 0

      #bound collision response
      if self.rect.left < self.fieldSize.left:
        self.rect.left = self.fieldSize.left
        self.velocity.x = -self.velocity.x

      if self.rect.right > self.fieldSize.right:
        self.rect.right = self.fieldSize.right
        self.velocity.x = -self.velocity.x

      if self.rect.top < self.fieldSize.top:
        self.rect.top = self.fieldSize.top
        self.velocity.y = -self.velocity.y
    
      if self.rect.bottom > self.fieldSize.bottom:
        self.rect.bottom > self.fieldSize.bottom
        self.velocity.y = -self.velocity.y
      
      #collition response with football player
      # if self.velocity.length() > 10:
      #   for player in blueTeam:
      #     if self.rect.colliderect(player.controlRect) and player != blueTeam.player:
      #       self.velocity = -self.velocity
      #   for player in redTeam:
      #     if self.rect.colliderect(player.controlRect):
      #       self.velocity = -self.velocity

  def passBall(self, vec):
    self.isRolling = True
    self.owner = None

    self.velocity = vec

  def shoot(self, vec = pygame.Vector2):
    self.velocity = vec.normalize() * 20
    self.isRolling = True
    self.owner = None

  # def shoot(self, vec: pygame.Vector2):
  #   self.velocity = vec.normalize() * 20
  #   self.isRolling = True
  #   self.owner = None

  def ballAfterGoal(self):
    self.rect.centerx = BACKGROUND_WIDTH / 2
    self.rect.centery = TABLE_SCORE_HEIGHT + BACKGROUND_HEIGHT / 2
    self.velocity = pygame.Vector2(0, 0)

BALL = Ball()
import pygame, sys
import os
import time
import random

from const import *
from Player import *
from Computer import *
from Ball import BALL
from Enum import *

# for blue team
DEFENDER_X = GAP_SIZE_WIDTH + 4 / 27 * GAME_WIDTH
MIDFIELDER_X = GAP_SIZE_WIDTH + 8 / 27 * GAME_WIDTH
STRIKER_X = GAP_SIZE_WIDTH + 12 / 27 * GAME_WIDTH
MIDDLE_Y = TABLE_SCORE_HEIGHT + GAP_SIZE_HEIGHT + GAME_HEIGHT / 2

SIZE_CONTROL_ICON = 18

ANGLE_MISS = 50

class Team(pygame.sprite.Group):
  def __init__(self):
    super(Team, self).__init__()

    self.players = []

    self.index = -1
    self.player = None

  def changePlayer(self):
    self.player = self.getClosestPlayer(self.player)
    self.player.state = State.FREE
  
  def passBall(self):
    """pass ball to team member"""
    curPlayer = self.player
    desPlayer = None
    angle = 50

    directVector = convertDirectVector(self.player.direction)
    #caculate vector and calculate angle
    for player in self.players:
      if player != curPlayer:
        tempVector = pygame.Vector2(player.rect.x - curPlayer.rect.x, player.rect.y - curPlayer.rect.y)
        tempAngle = abs( directVector.angle_to( tempVector ) )
        if tempAngle > 180:
          tempAngle = 360 - tempAngle

        if tempAngle < angle :
          angle = tempAngle
          desPlayer= player

    if desPlayer != None:
      passVector = pygame.Vector2( desPlayer.rect.x - curPlayer.rect.x, desPlayer.rect.y - curPlayer.rect.y)
      self.player = desPlayer

      length = passVector.length()
      if length > 500 :
        BALL.passBall( passVector.normalize() * 17 )
      elif length > 400 :
        BALL.passBall( passVector.normalize() * 15 )
      elif length > 300 :
        BALL.passBall( passVector.normalize() * 12 )
      elif length > 200 :
        BALL.passBall( passVector.normalize() * 10 )
      elif length > 100 :
        BALL.passBall( passVector.normalize() *  8)
      else:
        BALL.passBall( passVector.normalize() * 5 )
    else:
      BALL.passBall(convertDirectVector(self.player.direction).normalize() * 8)

    # self.state = State.ATTACK
    # print(self.state)

    self.player.state = State.FREE

  def getClosestPlayer(self, exceptPlayer = None):
    players = []
    
    for player in self.players:
      if player != exceptPlayer:
        players.append(player)

    minDistance = caculateDistance(self.players[0].controlRect.center, BALL.rect.center)
    minPlayer = players[0]

    for player in players:
      distance = caculateDistance(player.rect, BALL.rect)

      if distance < minDistance:
        minDistance = distance
        minPlayer = player
    
    return minPlayer

  def attack(self):
    for player in self.players:
      player.state = State.ATTACK

    self.player.state = State.FREE

class BlueTeam(Team):
  def __init__(self):
    super(BlueTeam, self).__init__()

    self.players = [
      # 2 Defender
      Player(DEFENDER_X, MIDDLE_Y - GAME_HEIGHT * 1 / 6),
      Player(DEFENDER_X, MIDDLE_Y + GAME_HEIGHT * 1 / 6),

      # 3 Midfielder
      Player(MIDFIELDER_X, MIDDLE_Y - GAME_HEIGHT * 2 / 6),
      Player(MIDFIELDER_X, MIDDLE_Y),
      Player(MIDFIELDER_X, MIDDLE_Y + GAME_HEIGHT * 2 / 6),

      # 2 Striker
      Player(STRIKER_X, MIDDLE_Y - GAME_HEIGHT * 1 / 6),
      Player(STRIKER_X, MIDDLE_Y + GAME_HEIGHT * 1 / 6),
    ]

    for player in self.players:
      self.add(player)

    self.index = len(self.players) - 1
    self.player = self.players[self.index]

    imageControl = pygame.image.load("assets/images/others/sort-down-fill.png")
    self.imageControl = pygame.transform.scale(imageControl, (SIZE_CONTROL_ICON, SIZE_CONTROL_ICON))

  def handle(self):
    self.attack()

    self.player.handle(self)
    for player in self.players:
      if player != self.player:
        player.performAction(self)

  def draw(self, screen):
    super().draw(screen)
    screen.blit(self.imageControl, (self.player.rect.centerx - SIZE_CONTROL_ICON / 2, self.player.rect.centery - 2 / 3 * PLAYER_SIZE))

class RedTeam(Team):
  def __init__(self):
    super(RedTeam, self).__init__()
    self.players = [
      # 2 Defender
      Computer(BACKGROUND_WIDTH - DEFENDER_X, MIDDLE_Y - GAME_HEIGHT * 1 / 6),
      Computer(BACKGROUND_WIDTH - DEFENDER_X, MIDDLE_Y + GAME_HEIGHT * 1 / 6),

      # 3 Midfielder
      Computer(BACKGROUND_WIDTH - MIDFIELDER_X, MIDDLE_Y - GAME_HEIGHT * 2 / 6),
      Computer(BACKGROUND_WIDTH - MIDFIELDER_X, MIDDLE_Y),
      Computer(BACKGROUND_WIDTH - MIDFIELDER_X, MIDDLE_Y + GAME_HEIGHT * 2 / 6),

      # 2 Striker
      Computer(BACKGROUND_WIDTH - STRIKER_X, MIDDLE_Y - GAME_HEIGHT * 1 / 6),
      Computer(BACKGROUND_WIDTH - STRIKER_X, MIDDLE_Y + GAME_HEIGHT * 1 / 6),
    ]
    
    for player in self.players:
      self.add(player)

    self.index = 0
    self.player = self.players[self.index]
  
  def handle(self):
    if BALL.owner == self.player:
      self.player.state = State.COMPUTER
    elif BALL.owner != self.player:
      self.attack()
      # self.player = self.getClosestComputer()
      self.player = self.getClosestPlayer()
      self.player.state = State.FIND_BALL

    for player in self.players:
      player.performAction(self)

  def getClosestComputer(self):
    minDistance = caculateDistance(self.players[0].controlRect.center, BALL.rect.center)

    minComputer = self.players[0]

    for player in self.players:
      distance = caculateDistance(player.rect, BALL.rect)

      if distance < minDistance:
        minDistance = distance
        minComputer = player
    
    return minComputer

  # def attackComputer(self):
  #   self.attack()
  #   self.player.state = State.COMPUTER
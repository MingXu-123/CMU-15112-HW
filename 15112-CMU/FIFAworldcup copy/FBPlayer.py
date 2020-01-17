import pygame
import os
import time

from const import *
from functions import *
from Enum import *
from Ball import BALL

SIZE = PLAYER_SIZE

PATH = "assets/images/player/"

MARGIN_TOP = int(TABLE_SCORE_HEIGHT +  BACKGROUND_HEIGHT / 2 - GOAL_WIDTH / 2)

DISTANCE_NEW_FRAME = 20

INTERVAL = 10

class FBPlayer(pygame.sprite.Sprite):
  def __init__(self, team, centerx, centery):
    super(FBPlayer, self).__init__()

    self.defaultX = centerx
    self.defaultY = centery

    self.index = 1

    self.state = State.FREE

    self.sprites = {
      UP: [],
      DOWN: [],
      RIGHT: [],
      LEFT: [],
      UP_LEFT: [],
      UP_RIGHT: [],
      DOWN_LEFT: [],
      DOWN_RIGHT: [],
    }

    self.totalDistance = 0

    # load images for sprites
    loadImages(self.sprites[UP], PATH + team + '/up/')
    loadImages(self.sprites[DOWN], PATH + team + '/down/')
    loadImages(self.sprites[RIGHT], PATH + team + '/right/')
    loadImages(self.sprites[LEFT], PATH + team + '/left/')
    loadImages(self.sprites[UP_LEFT], PATH + team + '/up-left/')
    loadImages(self.sprites[UP_RIGHT], PATH + team + '/up-right/')
    loadImages(self.sprites[DOWN_LEFT], PATH + team + '/down-left/')
    loadImages(self.sprites[DOWN_RIGHT], PATH + team + '/down-right/')

    if team is BLUE_TEAM:
      self.direction = RIGHT
    else: 
      self.direction = LEFT

    self.images = self.sprites[self.direction]
    self.image = self.images[1]

    self.rect = pygame.Rect(centerx - SIZE / 2, centery - SIZE / 2, SIZE, SIZE)
    self.controlRect = getControlRect(self.rect.centerx, self.rect.centery)

    self.directVector = pygame.Vector2(0, 0)

  def update(self):
    self.controlRect = getControlRect(self.rect.centerx, self.rect.centery)

  def move(self, direction, speed = SPEED_DEFAULT):
    if BALL.owner != None:
      self.updateBallPosition()
    self.updateDirection(direction)

    # update new frame
    if self.totalDistance > DISTANCE_NEW_FRAME:
      self.image = self.images[self.index]
      self.totalDistance = 0
      self.index += 1

      if self.index >= len(self.images):
        self.index = 0

    # self.totalDistance += speed

    if direction is UP and RECT_GAME.contains(self.controlRect.move(0, -speed)):
      self.rect = self.rect.move(0, -speed)
    elif direction is DOWN and RECT_GAME.contains(self.controlRect.move(0, speed)):
      self.rect = self.rect.move(0, speed)
    elif direction is LEFT and RECT_GAME.contains(self.controlRect.move(-speed, 0)):
      self.rect = self.rect.move(-speed, 0)
    elif direction is RIGHT and RECT_GAME.contains(self.controlRect.move(speed, 0)):
      self.rect = self.rect.move(speed, 0)
    elif direction is UP_LEFT and RECT_GAME.contains(self.controlRect.move(- speed / SQRT_2, - speed / SQRT_2)):
      self.rect = self.rect.move(- speed / SQRT_2, - speed / SQRT_2)
    elif direction is UP_RIGHT and RECT_GAME.contains(self.controlRect.move(speed / SQRT_2, - speed / SQRT_2)):
      self.rect = self.rect.move(speed / SQRT_2, - speed / SQRT_2)
    elif direction is DOWN_LEFT and RECT_GAME.contains(self.controlRect.move( - speed / SQRT_2, speed / SQRT_2)):
      self.rect = self.rect.move( - speed / SQRT_2, speed / SQRT_2)
    elif direction is DOWN_RIGHT and RECT_GAME.contains(self.controlRect.move( speed / SQRT_2, speed / SQRT_2)):
      self.rect = self.rect.move( speed / SQRT_2, speed / SQRT_2)
    
    #if BALL.owner == self:
    # if BALL.owner != None:
    #   self.updateBallPosition()

  def updateDirection(self, direction):
    # if self.direction is direction:
    #   return None

    self.direction = direction
    self.images = self.sprites[self.direction]
    # self.totalDistance = 0
    # self.index = 1
    self.image = self.images[0]

  def runFindBall(self):
    if BALL.owner == self:
      # return None
      pass
    
    # if BALL.owner == None and BALL.velocity.length() > 8:
    #   return None

    distances = {
      UP: caculateDistance((self.controlRect.centerx, self.controlRect.centery - SPEED_DEFAULT), BALL.rect),
      DOWN: caculateDistance((self.controlRect.centerx, self.controlRect.centery + SPEED_DEFAULT), BALL.rect),
      RIGHT: caculateDistance((self.controlRect.centerx + SPEED_DEFAULT, self.controlRect.centery), BALL.rect),
      LEFT: caculateDistance((self.controlRect.centerx - SPEED_DEFAULT, self.controlRect.centery), BALL.rect),
      UP_LEFT: caculateDistance((self.controlRect.centerx - SPEED_DEFAULT / SQRT_2, self.controlRect.centery  - SPEED_DEFAULT / SQRT_2), BALL.rect),
      UP_RIGHT: caculateDistance((self.controlRect.centerx + SPEED_DEFAULT / SQRT_2, self.controlRect.centery  - SPEED_DEFAULT / SQRT_2), BALL.rect),
      DOWN_LEFT: caculateDistance((self.controlRect.centerx - SPEED_DEFAULT / SQRT_2, self.controlRect.centery  + SPEED_DEFAULT / SQRT_2), BALL.rect),
      DOWN_RIGHT: caculateDistance((self.controlRect.centerx + SPEED_DEFAULT / SQRT_2, self.controlRect.centery  + SPEED_DEFAULT / SQRT_2), BALL.rect),
    }

    # direction = UP
    # distance = distances[UP]

    direction = DOWN
    distance = distances[DOWN]

    for key, value in distances.items():
      if value < distance:
        distance = value
        direction = key
    # print(direction)
    # print(distance)
    
    # if distance < 1:
    #     #   return None

    self.move(direction)


    if BALL.owner != None:
      # 当球受到蓝方控制时
      # 被抢断的概率
      if random.randint(1, 10000) == 1:
        self.takeBall()
        self.state = State.COMPUTER
      else:
        pass
    # else:
    elif BALL.owner == None:
      # 如果球没有人控制 红方拿球
      self.takeBall()
      self.state = State.COMPUTER

  def takeBall(self):
    if BALL.owner == self:
      return None

    if self.controlRect.colliderect(BALL.rect):
      BALL.owner = self

  def updateBallPosition(self):
    # if BALL.owner != self:
    #   return None
    if BALL.owner == self:
      # BALL.rect.centerx = self.rect.centerx
      # BALL.rect.centery = self.rect.centery + SIZE / 3

      # if (self.direction is LEFT):
      #   BALL.rect.centerx = self.rect.centerx
      # elif (self.direction is RIGHT):
      #   BALL.rect.centerx = self.rect.centerx
      # elif (self.direction is UP):
      #   BALL.rect.centery = self.rect.centery
      # elif (self.direction is DOWN):
      #   BALL.rect.centery = self.rect.centery

      # BALL.rect.centerx = self.rect.centerx
      # BALL.rect.centery = self.rect.centery + SIZE / 3
      #
      if (self.direction is LEFT):
        BALL.rect.centerx = self.rect.centerx - SIZE / 5
      elif (self.direction is RIGHT):
        BALL.rect.centerx = self.rect.centerx + SIZE / 5
      elif (self.direction is UP):
        BALL.rect.centery = self.rect.centery + SIZE / 4
      elif (self.direction is DOWN):
        BALL.rect.centery = self.rect.centery + SIZE / 4
      else:
        BALL.rect.centerx = self.rect.centerx
        BALL.rect.centery = self.rect.centery + SIZE / 3

  def shoot(self):
    if BALL.owner == self:
      BALL.shoot(convertDirectVector(self.direction))
    # else:
    #   pass

  def performAction(self, team):
    if self.state == State.ATTACK:
      coefficient = BALL.rect.centerx / BACKGROUND_WIDTH * 2
      if coefficient < 0.8:
        coefficient = 0.8

      shouldMoveRight = self.rect.centerx - self.defaultX * coefficient + INTERVAL * coefficient < team.player.rect.centerx - team.player.defaultX * coefficient
      shouldMoveLeft = self.rect.centerx - self.defaultX * coefficient - INTERVAL * coefficient > team.player.rect.centerx - team.player.defaultX * coefficient
      shouldMoveUp = self.rect.centery - self.defaultY > INTERVAL * coefficient
      shouldMoveDown = self.rect.centery - self.defaultY < - INTERVAL * coefficient

      if shouldMoveUp and shouldMoveLeft:
        self.move(UP_LEFT)
      elif shouldMoveUp and shouldMoveRight:
        self.move(UP_RIGHT)
      elif shouldMoveDown and shouldMoveLeft:
        self.move(DOWN_LEFT)
      elif shouldMoveDown and shouldMoveRight:
        self.move(DOWN_RIGHT)
      elif shouldMoveUp:
        self.move(UP)
      elif shouldMoveDown:
        self.move(DOWN)
      elif shouldMoveRight and self.rect.centerx < BACKGROUND_WIDTH - 100:
        self.move(RIGHT)
      elif shouldMoveLeft and self.rect.centerx > 100:
        self.move(LEFT)
    elif self.state == State.FIND_BALL:
      self.runFindBall()
    elif self.state == State.COMPUTER:
      self.move(LEFT)

      if (caculateDistance(self.rect.center, pygame.Rect(0 ,MARGIN_TOP ,GAP_SIZE_WIDTH + 10, GOAL_WIDTH ).center) < 50000):
        self.shoot()
    # pass
    
      


def loadImages(list, path):
  for filename in os.listdir(path):
    if filename.endswith(".png"):
      image = pygame.image.load(path + filename)
      resizeImage = pygame.transform.scale(image, (SIZE, SIZE))
      list.append(resizeImage)

def getControlRect(centerx, centery):
  return pygame.Rect(centerx - SIZE / 4, centery, SIZE / 2, SIZE / 2)



import os
from const import *
import numpy
import random

def rename():
  folder = 'assets/sounds/hits'
  for filename in os.listdir(folder):
    infilename = os.path.join(folder,filename)
    if not os.path.isfile(infilename): continue
    oldbase = os.path.splitext(filename)
    newname = infilename.replace('.mp3', '.wav')
    output = os.rename(infilename, newname)

def caculateDistance(position1, position2):
  x = abs(position2[0] - position1[0])
  y = abs(position2[1] - position1[1])
  return (x * x + y * y)

def convertDirectVector(direction):
  if direction is LEFT:
    return pygame.Vector2(-1, 0).normalize()
  elif direction is RIGHT:
    return pygame.Vector2(1, 0).normalize()
  elif direction is UP:
    return pygame.Vector2(0, -1).normalize()
  elif direction is DOWN:
    return pygame.Vector2(0, 1).normalize()
  elif direction is UP_LEFT:
    return pygame.Vector2(-1, -1).normalize()
  elif direction is UP_RIGHT:
    return pygame.Vector2(1, -1).normalize()
  elif direction is DOWN_LEFT:
    return pygame.Vector2(-1, 1).normalize()
  elif direction is DOWN_RIGHT:
    return pygame.Vector2(1, 1).normalize()
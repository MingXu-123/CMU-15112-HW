from enum import Enum

class State(Enum):
  FIND_BALL = 1
  FREE = 2
  LEAD_TO_GOAL = 3
  ATTACK = 4
  COMPUTER = 5


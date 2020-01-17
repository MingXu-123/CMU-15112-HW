from Ball import *
from const import *
import pygame , sys
import colors
from Team import *
from Text import *
from Sounds import *

MARGIN_RIGHT = BACKGROUND_WIDTH - GAP_SIZE_WIDTH -10
MARGIN_TOP = int(TABLE_SCORE_HEIGHT +  BACKGROUND_HEIGHT / 2 - GOAL_WIDTH / 2)
DEFENDER_X = GAP_SIZE_WIDTH + 5 / 27 * GAME_WIDTH
MIDFIELDER_X = GAP_SIZE_WIDTH + 8 / 27 * GAME_WIDTH
STRIKER_X = GAP_SIZE_WIDTH + 11 / 27 * GAME_WIDTH
MIDDLE_Y = TABLE_SCORE_HEIGHT + GAP_SIZE_HEIGHT + GAME_HEIGHT / 2

sound = Sounds()
class GameInfo():
  def __init__(self):
    self.redTeamScore = 0
    self.blueTeamScore = 0
    self.blueGoal =  pygame.Rect(0 ,MARGIN_TOP ,GAP_SIZE_WIDTH + 10, GOAL_WIDTH )
    self.redGoal =  pygame.Rect(MARGIN_RIGHT,MARGIN_TOP ,GAP_SIZE_WIDTH + 10, GOAL_WIDTH)
    
  def isGoal(self):
    if self.blueGoal.colliderect( BALL.rect ):
      self.redTeamScore += 1
      sound.isRedGoal()
      return True
    if self.redGoal.colliderect( BALL.rect ):
      self.blueTeamScore += 1
      sound.isBlueGoal()
      return True
    
    return False
    
  @staticmethod
  def initGame():
    blueTeam = BlueTeam()
    redTeam = RedTeam()

    return (blueTeam, redTeam)
  
  @staticmethod
  def gameAfterGoal():
    BALL.ballAfterGoal()
    return GameInfo.initGame()

  @staticmethod
  def renderScore(red, blue, screen):
    Text.showScore('Blue Team: ', colors.Blue, screen, 100)
    Text.showScore(str(blue), colors.Blue, screen, 240)
    Text.showScore(str(red), colors.Red, screen, 310)
    Text.showScore(': Red Team', colors.Red, screen, 450)

  
import sys, pygame
from pygame.math import Vector2
import time
import datetime
import colors
from Sounds import *
from Text import *
from Background import *
from Player import *
from Ball import *
from functions import *
from const import *
from SettingBoard import * 
from GameInfo import *
from Team import *


millis = lambda: int(round(time.time() * 1000))

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % (80, 30)

pygame.init()

sounds = Sounds()
background = Background()
 
settingBoard = SettingBoard()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("FIFAworldcup")


def renderSettingButton():
  rect = pygame.Rect( 900 , 0 , WIDTH_OF_PAUSE_GAME - 2 * MARGIN, BUTTON_HEIGHT+ 10)
  titleSurf, titleRect = Text.makeTextObject("SETTING", colors.Green)
  pygame.draw.rect(screen, colors.Black, rect)
  screen.blit(titleSurf, ( 930 , 0 , WIDTH_OF_PAUSE_GAME - MARGIN * 2, BUTTON_HEIGHT))
  return rect

def renderSettingBoard(setting): 
  pygame.mouse.set_visible(True)
  while True:
    x = (WINDOW_WIDTH  - WITH_SETTING_BOARD) /2
    y = 0
    screen.blit(settingBoard, (x, y))
    for event in pygame.event.get():
      
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        (x, y) = pygame.mouse.get_pos()
        check = settingBoard.click(x, y)
        if( check == 1 ): # handle new game
          main()
        if(setting.collidepoint(x,y)):
          return
    
    pygame.display.update()
    clock.tick(FPS)

def renderTimeLeft(counter, text):
  text = str(datetime.timedelta(seconds = counter))[3:].rjust(3) if counter > 0 else 'boom!'
  counter -= 1
  return counter , text

def renderWinner(red , blue):
    myNewSurface = pygame.Surface((370, 50))
    myNewSurface.fill(colors.Black)
    screen.blit(myNewSurface, (WINDOW_HEIGHT / 2 + 30 , HEIGHT / 2 - 23 ))
    if( red > blue):
      Text.showTextWiner('Red Team Is Winner', colors.Red, screen, WINDOW_WIDTH / 2 , HEIGHT / 2)
    elif( red < blue):
      Text.showTextWiner('Blue Team Is Winner', colors.Red, screen, WINDOW_WIDTH / 2,HEIGHT / 2)
    else: 
      Text.showTextWiner('Tow Team Is Harmony', colors.Red, screen, WINDOW_WIDTH / 2 , HEIGHT / 2)
    
def main():
  counter, text = 180, '3:00'.rjust(3)

  font = pygame.font.SysFont('Consolas', 60)
  pygame.time.set_timer(pygame.USEREVENT, 1000)


  spriteBall = pygame.sprite.Group(BALL)
  gameInfo = GameInfo()
  sounds.music()
  (blueTeam, redTeam) = GameInfo.initGame()

  # setting()
  isPause = False
  startTime = millis()
  while millis() - startTime <= 5000 * 60:
    screen.blit(background, (0, 0))
    GameInfo.renderScore(gameInfo.redTeamScore, gameInfo.blueTeamScore, screen)
    setting = renderSettingButton()
    
    if isPause is False : 
      for event in pygame.event.get():
        # QUIT
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
        if event.type == pygame.USEREVENT and counter != -1 : 
          counter ,text = renderTimeLeft(counter , text)
        # Key Down
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_s:
            if BALL.owner!= blueTeam.player:
              blueTeam.changePlayer()
            else:
              blueTeam.passBall()
          elif event.key == pygame.K_d:
            blueTeam.player.shoot()
          elif event.key == pygame.K_SPACE:
            blueTeam.player.takeBall()
            pass

        # Mouse button down
        if event.type == pygame.MOUSEBUTTONDOWN:
          (x, y) = pygame.mouse.get_pos()
          if(setting.collidepoint(x,y)):
              renderSettingBoard(setting)

      redTeam.handle()
      blueTeam.handle()

      #check ball in goal ?
      if gameInfo.isGoal():
        (blueTeam, redTeam) = gameInfo.gameAfterGoal()

    #update sprite
    blueTeam.update()
    redTeam.update()
    BALL.update(blueTeam, redTeam)

    #draw to screen
    blueTeam.draw(screen)
    redTeam.draw(screen)
    spriteBall.draw(screen)
    if counter != -1:
      screen.blit(font.render(text, True, (0, 0, 0)), (600, 5))
    elif(counter == -1):
      renderWinner(gameInfo.redTeamScore,gameInfo.blueTeamScore)

    pygame.display.update()
    clock.tick(FPS)

if __name__ == '__main__':
  main()
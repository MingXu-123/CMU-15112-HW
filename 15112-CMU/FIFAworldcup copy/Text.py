from const import *

class Text:
  @staticmethod
  def makeTextObject(text, color):
    surf = FONT30B.render(text, True, color)
    return surf, surf.get_rect()

  @staticmethod
  def makeTextPauseGame(text,color):
    surf = FONT60B.render(text, True, color)
    return surf, surf.get_rect()

  @staticmethod
  def showText(text, color, screen, y):
    titleSurf, titleRect = Text.makeTextObject(text, color)
    titleRect.center = (int(GAME_WIDTH + TEXT_WIDTH / 2), int(y))

    screen.blit(titleSurf, titleRect)

  @staticmethod
  def showScore(text, color, screen, x ):
    titleSurf, titleRect = Text.makeTextObject(text, color)
    titleRect.center = (x, TABLE_SCORE_HEIGHT / 2)

    screen.blit(titleSurf, titleRect)
  
  @staticmethod
  def showTextInPlayGain(text, color, screen, y):
    titleSurf, titleRect = Text.makeTextObject(text, color)
    titleRect.center = (int(WIDTH_OF_PLAY_AGAIN_BOARDING / 2), int(y))

    screen.blit(titleSurf, titleRect)
  
  @staticmethod
  def showSettingText(text, color, screen, y):
    titleSurf, titleRect = Text.makeTextObject(text, color)
    titleRect.center = (int(WIDTH_OF_PAUSE_GAME / 2), int(y))

    screen.blit(titleSurf, titleRect)

  @staticmethod
  def showTextInPauseGame(text, color, screen, y):
    titleSurf, titleRect = Text.makeTextObject(text, color)
    titleRect.center = (int(WIDTH_OF_PAUSE_GAME / 2), int(y))

    screen.blit(titleSurf, titleRect)
  @staticmethod
  def showTextWiner(text, color, screen,x, y):
    titleSurf, titleRect = Text.makeTextObject(text, color)
    titleRect.center = (int(x), int(y))
    screen.blit(titleSurf, titleRect)




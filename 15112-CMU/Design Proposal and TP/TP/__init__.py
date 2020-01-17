# this is the __init__ file for this game and main logic of this game is in this file
from BlueAndRedTeam import *
from FIFAplayer import *
from music import *
from ControlBoard import *
import time
import datetime


# cite the structure of the framework of this game is from 15112 TA's code
# Lukas Pygame templatem, besides the images of players and
# balls in this game are downloaded from
# https://pan.baidu.com/s/1Q_b6DiPq_sH870pCdONKkg and
# the extraction code is: mz8q
# the background music is downloaded from
# http://fcsongs.com/UEFA_Champions_League_-_Main_Theme.html


class MiniFIFAOnline3(object):
    # the init function for mini FIFAonline3
    def __init__(self):
        self.blueTeam = BlueTeam()
        self.redTeam = RedTeam()
        self.music = BackGroundMusic()
        self.gameControl = GameControl()
        self.isGameOver = False
        self.fps = 200
        self.timeCounter = 180
        self.counterText = 'Time Left 3:00'
        # this font is from pygame documentation font example
        # https://github.com/search?q=pygame.font.SysFont&type=Code
        self.font = pygame.font.SysFont('Arial', 60)
        self.font1 = pygame.font.SysFont('comicsansms', 100)

    # this is the repr function
    def __repr__(self):
        return "This game is mini-FIFAonline3!!!"


    # new game method
    def newGame(self):
        self.blueTeam = BlueTeam()
        self.redTeam = RedTeam()
        ball.generateNewBall()


    # restart game method
    def restartGame(self):
        self.newGame()
        self.gameControl.blueTeamScore = 0
        self.gameControl.redTeamScore = 0
        self.timeCounter = 180


    # this is the keypress handler
    def keypressed(self, event):
        if event.key == pygame.K_s:
            if ball.owner == self.blueTeam.player:
                self.blueTeam.passBallToTeamMembers()
            elif ball.owner != self.blueTeam.player:
                self.blueTeam.changePlayer()
        elif event.key == pygame.K_d:
            if ball.owner == self.blueTeam.player:
                self.blueTeam.player.shoot()
            elif ball.owner != self.blueTeam.player:
                self.blueTeam.player.getBall()
        elif event.key == pygame.K_a:
            if ball.owner == self.blueTeam.player:
                self.blueTeam.player.crossBall()
        elif event.key == pygame.K_e:
            if ball.owner == self.blueTeam.player:
                self.blueTeam.speedup()
        elif event.key == pygame.K_r:
            self.restartGame()


    # this is the mouse press handler
    def mousepressed(self, event):
        pass


    # check whether team players have goal
    def checkWhetherIsGoal(self):
        if self.gameControl.teamISGoal():
            self.newGame()


    # this function generate game winner
    def generateWinner(self, blueTeamScore, redTeamScore, gameDisplay):
        for player in self.blueTeam:
            self.blueTeam.remove(player)
        for player in self.redTeam:
            self.redTeam.remove(player)
        ball.generateNewBall()
        if blueTeamScore > redTeamScore:
            text = "BLue Team Win !!!"
            gameDisplay.blit(self.font1.render(text,
                                              True, Colors.BlueViolet), (200, 300))
        elif blueTeamScore < redTeamScore:
            text = "Red Team Win !!!"
            gameDisplay.blit(self.font1.render(text,
                                               True, Colors.Coral), (200, 300))
        else:
            text = "It Was a Tie !!!"
            gameDisplay.blit(self.font1.render(text,
                                               True, Colors.GoldenRod), (200, 300))


    # this method update the timeCounter and counter text value each second
    def updateTimeCounterAndText(self):
        self.counterText = str("Time Left ") + \
               str(datetime.timedelta(seconds=self.timeCounter))[3:]
        self.timeCounter -= 1
        return self.timeCounter, self.counterText


    # show How much time left for this game
    def showTimeLeft(self, gameDisplay):
        gameDisplay.blit(self.font.render(self.counterText,
                                          True, Colors.Black), (50, 5))

    # this is method is to check whether to generate winner or continue to show time left
    def checkToGenerateWinner(self, gameDisplay):
        if self.timeCounter > 0:
            self.showTimeLeft(gameDisplay)
        else:
            self.generateWinner(self.gameControl.blueTeamScore,
                                self.gameControl.redTeamScore, gameDisplay)

    # this is the main loop
    def run(self):
        pygame.init()
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        self.music.loadMusic()
        gameDisplay = pygame.display.set_mode((getGameDimension()[0],
                                               getGameDimension()[1]))
        pygame.display.set_caption("MiniFIFAOnline3")
        spriteBall = pygame.sprite.Group(ball)
        clock = pygame.time.Clock()
        while not self.isGameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isGameOver = True
                # the following if statement will be called once each second
                if event.type == pygame.USEREVENT:
                    if self.timeCounter > 0:
                        self.updateTimeCounterAndText()
                if event.type == pygame.KEYDOWN:
                    self.keypressed(event)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.mousepressed(event)
            background = Background()
            gameDisplay.blit(background, (0, 0))
            self.blueTeam.controlPlayer()
            self.redTeam.controlAI()
            self.blueTeam.update()
            self.redTeam.update()
            ball.update()
            # check whether team player goal
            self.checkWhetherIsGoal()
            spriteBall.draw(gameDisplay)
            self.blueTeam.draw(gameDisplay)
            self.blueTeam.drawArrow(gameDisplay)
            self.redTeam.draw(gameDisplay)
            self.gameControl.drawScore(gameDisplay)
            self.checkToGenerateWinner(gameDisplay)
            # parameter background processing
            pygame.display.update()
            clock.tick(self.fps)


# the main function
def main():
    game = MiniFIFAOnline3()
    game.run()

if __name__ == '__main__':
    main()

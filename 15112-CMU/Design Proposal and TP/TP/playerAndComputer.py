# this file is mainly for class Player and Computer
# which means that team players is controlled by player or computer
from FIFAplayer import *


class Player(FIFAPlayer):
    def __init__(self, centerx, centery):
        blueTeam = 'blue-team'
        super(Player, self).__init__(centerx, centery, blueTeam)

    # this is the control method
    def control(self):
        # cite pygame.key.get_pressed() this code structure is from
        # https://github.com/search?q=pygame.key.get_pressed&type=Code
        if pygame.key.get_pressed()[pygame.K_UP] \
                and pygame.key.get_pressed()[pygame.K_LEFT]:
            self.move("upLeft")
        elif pygame.key.get_pressed()[pygame.K_UP] \
                and pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.move("upRight")
        elif pygame.key.get_pressed()[pygame.K_DOWN] \
                and pygame.key.get_pressed()[pygame.K_LEFT]:
            self.move("downLeft")
        elif pygame.key.get_pressed()[pygame.K_DOWN] \
                and pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.move("downRight")
        elif pygame.key.get_pressed()[pygame.K_UP]:
            self.move("up")
        elif pygame.key.get_pressed()[pygame.K_DOWN]:
            self.move("down")
        elif pygame.key.get_pressed()[pygame.K_LEFT]:
            self.move("left")
        elif pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.move("right")




class Computer(FIFAPlayer):
    def __init__(self, centerx, centery):
        redTeam = 'red-team'
        super(Computer, self).__init__(centerx, centery, redTeam)




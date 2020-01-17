#!/usr/bin/env python
#
#
#
#
#

"""
#TODO: documentation!
"""

__author__ = "$Author: DR0ID $"
__version__ = "$Revision: 94 $"
__date__ = "$Date: 2007-08-04 12:22:42 +0200 (Sa, 04 Aug 2007) $"
__license__ = ''
__copyright__ = "DR0ID (c) 2007"
__url__ = "http://www.mypage.bluewin.ch/DR0ID/index.html"
__email__ = "dr0id@bluewin.ch"


import pygame
import sys
import _FastRenderGroup as FastRenderGroup
import random
import os
join = os.path.join
orig_load = pygame.image.load

def loading(file_name):
    return orig_load(join('data', file_name))

pygame.image.load = loading

SCREEN_SIZE = (800, 900)
PLAY_INTERVALL = (200, 600)
            # [(speed, speed_deviation, num_beers_gen, intervall),point limit,  beer fill amount, picture]
##LEVEL_CONFIG = [(2,    (-1, 1),       (0,1),         (55,60),    1000, 50 ,"pic1.JPG"),\
##                (3,    (-2, 1),       (0,2),         (55,60),    2000, 50, "pic2.JPG"),\
##                (8,    (-2, 4),       (0,4),         (10,40),    3000, 50, "pic3.JPG"),\
##                (8,    (-0, 1),       (0,6),         (10,40),  100000, 50, "pic4.JPG")]
LEVEL_CONFIG = []

level_file = open(join('data','config.txt'))
line_num = 0
for line in level_file.readlines():
    entries = line.split(',')
    if entries[0][0] == '#':
        continue
    if len(entries) != 10:
        print ("Wrong number of values in config.txt, line:", line_num)
        sys.exit()
    speed = int(entries[0].strip())
    speed_dev1 = int(entries[1].strip())
    speed_dev2 = int(entries[2].strip())
    num_b_gen1 = int(entries[3].strip())
    num_b_gen2 = int(entries[4].strip())
    intervall1 = int(entries[5].strip())
    intervall2 = int(entries[6].strip())
    point_limit = int(entries[7].strip())
    fill_amount = int(entries[8].strip())
    pic_name = entries[9].strip()
    data = (speed, (speed_dev1, speed_dev2), (num_b_gen1, num_b_gen2), (intervall1, intervall2), point_limit, fill_amount, pic_name)
    LEVEL_CONFIG.append(data)
    line_num += 1





class Level(FastRenderGroup.DirtySprite):
    
    speed = 0
    speed_deviation = 0
    num_beers_generation = 0
    intervall = 0
    level_limit = 0
    fill_amount = 0
    
    
    current_level = -1
    glas = None
    points = 0
    running = True
    deckels = None
    score = None
    
    def __init__(self):
        FastRenderGroup.DirtySprite.__init__(self)
        self._missed = 0
        self.next_level()
        
    def reset(self):
        self.__class__.points = 0
        self.__class__.running = True
        self.running = True
        self.__class__.current_level = -1
        self._missed = 0
        self.next_level()
        
    def next_level(self):
        self.__class__.current_level += 1
        if self.__class__.current_level == len(LEVEL_CONFIG):
            self.__class__.current_level -= 1
        self.__class__.speed ,\
        self.__class__.speed_deviation , \
        self.__class__.num_beers_generation , \
        self.__class__.intervall, \
        self.__class__.level_limit, \
        self.__class__.fill_amount, \
        picture \
        = LEVEL_CONFIG[self.__class__.current_level]
        self.image = pygame.image.load(picture)
        self.rect = self.image.get_rect(topleft = (SCREEN_SIZE[0]-self.image.get_width(), 50))
##        print "what?:", self.rect
        self.dirty = 1
        if self.glas is not None:
            self.glas.fill()
##        for key, value in self.__class__.__dict__.items():
##            print key, "=", value
        
    def add_points(self):
        self.score.scored(100)
        if self.score.points >= self.__class__.level_limit:
            self.next_level()
            
    def missed(self):
        self._missed += 1
        if self.running:
            if len(self.deckels):
                self.deckels[-1].kill()
                self.deckels.pop(-1)
##        print len(self.deckels)
        if self._missed == 3:
            self.running = False
##            print "Game over!!!!!!!!!!!!!"
##        print "MISSED: ", self._missed
            
            
LEVEL = Level()

class Score(FastRenderGroup.DirtySprite):
    
    def __init__(self):
        FastRenderGroup.DirtySprite.__init__(self)
        self.font = pygame.font.Font("freesansbold.ttf", 50)
        self.points = 0
        self.image = self.font.render(str(0), 2, (255, 0, 0))
        self.rect = self.image.get_rect(topright=(200,self.image.get_height()/2))
        
    def scored(self, points):
        self.points += points
        self.image = self.font.render(str(self.points), 2, (255, 0,0))
        self.rect = self.image.get_rect(topright= self.rect.topright)
        self.dirty = 1
        print (self.points)

class Bier(FastRenderGroup.DirtySprite):
    
    def __init__(self):
        FastRenderGroup.DirtySprite.__init__(self)
        self.image = pygame.image.load("Bier.PNG").convert()
        self.image.set_colorkey((255, 0, 255))
        self.rect = self.image.get_rect(topleft=(0,SCREEN_SIZE[1]-225))
        self.source_rect = pygame.Rect(0, 0, self.rect.width, 0)
        
    def fill(self, amount=50):
##        print "filling"
        if self.rect.height > self.source_rect.height:
            amount = LEVEL.fill_amount
            self.source_rect.height += amount
            self.rect.top -= amount
        else:
            self.source_rect.height = self.rect.height
        self.dirty = 1


class Glas(FastRenderGroup.DirtySprite):
    
    def __init__(self):
        FastRenderGroup.DirtySprite.__init__(self)
        self.image = pygame.image.load("Glas.PNG").convert_alpha()
        self.image.set_colorkey((255, 0, 255))
        self.rect = self.image.get_rect(topleft=(0,SCREEN_SIZE[1]-self.image.get_height()-200))
        self.bier = None
        
    def fill(self):
        self.bier.fill()

class Deckel(FastRenderGroup.DirtySprite):
    
    num = 0
    
    def __init__(self):
        FastRenderGroup.DirtySprite.__init__(self)
        self.image = pygame.image.load("Deckel.PNG").convert()
        self.image.set_colorkey((255, 0, 255))
        self.rect = self.image.get_rect(topleft=(self.__class__.num*60+20,SCREEN_SIZE[1]-self.image.get_height()-50))
        self.__class__.num += 1


class Flasche(FastRenderGroup.DirtySprite):
    
    image = None
    group = None
    
    def __init__(self, speed):
        FastRenderGroup.DirtySprite.__init__(self)
        self.speed = speed + random.randint(*LEVEL.speed_deviation)
        if self.__class__.image is None:
            self.__class__.image = pygame.image.load("Flasche.PNG").convert()
            self.__class__.image.set_colorkey((255, 0, 255))
        self.image = self.__class__.image
        if self.__class__.group is None:
            self.__class__.group = pygame.sprite.Group()
        self.__class__.group.add(self)
        self.__class__.renderer.add(self)
        a, b = PLAY_INTERVALL
        w = self.image.get_width()/2
        self.rect = self.image.get_rect(topleft = (random.randint(a+w, b-w), -self.image.get_height()))
        self.dirty = 2
##        print "beer"
        
    def update(self):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_SIZE[1]:
            for group in self.groups():
                group.remove(self)
            LEVEL.missed()
        
    def kill(self):
        LEVEL.add_points()
        FastRenderGroup.DirtySprite.kill(self)
##        print LEVEL.points
        
        
class Harasse(FastRenderGroup.DirtySprite):
    
    
    def __init__(self):
        FastRenderGroup.DirtySprite.__init__(self)
        self.image = pygame.image.load("Harasse.PNG").convert()
        self.image.set_colorkey((255, 0, 255))
        img_h = self.image.get_height()
        self.rect = self.image.get_rect(topleft=(SCREEN_SIZE[0]/2, SCREEN_SIZE[1]-img_h-img_h/2))
        self.dirty = 2
        self.intervall = 40
        self.count = self.intervall
        Flasche(1)
        Deckel.num = 0
        
    def update(self):
        self.rect.centerx = pygame.mouse.get_pos()[0]
        pygame.mouse.set_visible(False)
        if self.rect.right > PLAY_INTERVALL[1]:
            self.rect.right = PLAY_INTERVALL[1]
            pygame.mouse.set_visible(True)
        if self.rect.left < PLAY_INTERVALL[0]:
            self.rect.left = PLAY_INTERVALL[0]
            pygame.mouse.set_visible(True)
            
            
        self.count += 1
        if self.count >= self.intervall:
            self.count = 0
            self.intervall = random.randint(*LEVEL.intervall)
            for num in range( random.randint(*LEVEL.num_beers_generation) ):
                Flasche(LEVEL.speed)
        # smaller collision rect
        orig = self.rect
        self.rect = pygame.Rect((orig.left, orig.top+orig.height/2), (orig.width, 3))
        collider = pygame.sprite.spritecollide(self, Flasche.group, True)
        self.rect = orig

class Text(FastRenderGroup.DirtySprite):
    
    def __init__(self, pos, msg, font, color=(255, 0, 0)):
        FastRenderGroup.DirtySprite.__init__(self)
        self.font = font
        self.points = 0
        self.image = self.font.render(str(msg), 2, color)
        self.rect = self.image.get_rect(topleft=pos)
        
    def center(self, dx=0, dy=0):
        self.rect = self.image.get_rect(center=(SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2))
        self.rect.move_ip(dx, dy)



def main():
    
    SCREEN_SIZE = (PLAY_INTERVALL[1]+LEVEL.image.get_width(), 900)
    pygame.display.init()
    pygame.font.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    bgd = pygame.Surface(screen.get_size()).convert()
    bgd.fill((255, 255, 255))
    
    running3 = True
    while running3:
        renderer = FastRenderGroup.LayeredDirty()
        
        # init stuff
        Flasche.renderer = renderer
        renderer.add(Harasse(), layer=12)
        renderer.add(LEVEL, layer = -1)
        bier = Bier()
        LEVEL.glas = Glas()
        LEVEL.glas.bier = bier
        renderer.add(bier)
        renderer.add(LEVEL.glas)
        LEVEL.deckels = []
        d = Deckel()
        LEVEL.deckels.append(d)
        renderer.add(d)
        d = Deckel()
        LEVEL.deckels.append(d)
        renderer.add(d)
        d = Deckel()
        LEVEL.deckels.append(d)
        renderer.add(d)
        
        
        LEVEL.score = Score()
        renderer.add(LEVEL.score)
        paused_text = Text((0,0), "Paused", pygame.font.Font("freesansbold.ttf", 200))
        paused_text.center()
        paused_text.visible = False
        renderer.add(paused_text, layer = 1000)
    
        
        level = 0
        clock = pygame.time.Clock()
    ##    pygame.event.set_grab(True)
        paused = False
        running = True
        running2 = True
        while running and LEVEL.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   running = False
                   running2 = False
                   running3 = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False 
                elif event.type == pygame.ACTIVEEVENT:
                    if event.gain:
                        paused = False
                        paused_text.visible = False
                    else:
                        paused = True
                        paused_text.visible = True
            clock.tick(60)
    ##        print clock.get_fps()
            # draw screen
            if not paused:
                renderer.update()
            pygame.display.update(renderer.draw(screen, bgd))
        # loop end
        pygame.mouse.set_visible(True)
        gameover_text = Text((0,0), "Game over!", pygame.font.Font("freesansbold.ttf", 100))
        gameover_text.center()
        renderer.add(gameover_text)
        
        yes_text = Text((0,0), "try again", pygame.font.Font("freesansbold.ttf", 50))
        yes_text.center(-100, 200)
        renderer.add(yes_text)
    
        no_text = Text((0,0), "exit", pygame.font.Font("freesansbold.ttf", 50))
        no_text.center(100, 200)
        renderer.add(no_text)
    
    ##    img = font.render("Game over!", 20, (255, 0, 0))
    ##    screen.blit(img, (SCREEN_SIZE[0]/2-img.get_width()/2, SCREEN_SIZE[1]/2-img.get_height()/2))
    ##    pygame.display.flip()
        while running2:
            pygame.display.update(renderer.draw(screen, bgd))
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                running2 = False
                running3 = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running2 = False 
                    running3 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if no_text.rect.collidepoint(event.pos):
                    running3 = False
                    running2 = False
                elif yes_text.rect.collidepoint(event.pos):
                    running2 = False
                    
        renderer.empty()
        Flasche.group.empty()
        LEVEL.reset()
        running = True
        running2 = True
        
    ##    pygame.quit()
                    
if __name__== '__main__':
    main()
import os
import pygame
import random

pygame.init()

PATH = "assets/sounds/"
MUSIC_BACKGROUND = PATH + "music_background/"
REDGOAL =	PATH + "redgoal/"
BLUEGOAL =	PATH + "bluegoal/"

class Sounds:
	def __init__(self):
		self.hits = []
		self.redgoal = None
		self.bluegoal = None
		self.music_background = None
		for dirs in os.listdir(PATH):
			for filesound in os.listdir(PATH + dirs):
				if filesound.endswith(".wav"):
					if(dirs == "music_background"): 
						self.music_background = MUSIC_BACKGROUND + filesound
					if(dirs == "bluegoal"): 
						self.bluegoal = BLUEGOAL + filesound
					if(dirs == "redgoal"): 
						self.redgoal = REDGOAL + filesound
	def music(self):
		pygame.mixer.music.load(self.music_background)
		pygame.mixer.music.play(-1)
		pygame.mixer.music.set_volume(0.6)

	def isRedGoal(self):
		sound = pygame.mixer.Sound(self.redgoal)
		sound.set_volume(1.0)
		sound.play()

	def isBlueGoal(self):
		sound = pygame.mixer.Sound(self.bluegoal)
		sound.set_volume(1.0)
		sound.play()

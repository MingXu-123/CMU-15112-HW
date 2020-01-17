# this file only contains class backgroundmusic
import os
import pygame


class BackGroundMusic:
    def __init__(self):
        self.musicPath = None

    # method to load music
    def loadMusic(self):
        path = "assets/sounds/music_background/"
        for filename in os.listdir(path):
            if filename.endswith(".DS_Store"):
                continue
            else:
                if filename.endswith(".mp3"):
                    self.musicPath = path + filename
        pygame.mixer.music.load(self.musicPath)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.3)


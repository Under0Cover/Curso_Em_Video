# DESAFIO 021
# TOCADOR DE MP3

import pygame
pygame.init()
pygame.mixer.music.load('legiao.mp3')
pygame.mixer.music.play()
pygame.event.wait()

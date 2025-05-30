# Instalar e ouvir arquivo mp3

import pygame

pygame.init()
pygame.mixer.music.load('exe21.mp3')
pygame.mixer.music.play()
input('Digite enter para parar a música: ')
pygame.mixer.music.stop()


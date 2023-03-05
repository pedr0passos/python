# importando o pygame
import pygame

# iniciando o pygame
pygame.init()
pygame.mixer.music.load('midia/musica.mp3')
pygame.mixer.music.play()
pygame.event.wait()

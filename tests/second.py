import pygame
import time
pygame.init()
clock = pygame.time.Clock()
# Sounds

A = pygame.mixer.Sound("A.wav")
B = pygame.mixer.Sound("B.wav")
C = pygame.mixer.Sound("C.wav")
D = pygame.mixer.Sound("D.wav")
E = pygame.mixer.Sound("E.wav")
F = pygame.mixer.Sound("F.wav")
G = pygame.mixer.Sound("G.wav")
clock.tick(60)

pygame.mixer.Sound.play(A)

pygame.mixer.music.stop()
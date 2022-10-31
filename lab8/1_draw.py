import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

circle(screen, (255, 255, 51), (200, 200), 150)
circle(screen, (0, 0, 0), (200, 200), 150, 1)
circle(screen, (255, 0, 0), (120, 150), 40)
circle(screen, (0, 0, 0), (120, 150), 40, 1)
circle(screen, (255, 0, 0), (270, 150), 30)
circle(screen, (0, 0, 0), (270, 150), 30, 1)
circle(screen, (0, 0, 0), (270, 150), 20)
circle(screen, (0, 0, 0), (120, 150), 20)
rect(screen, (0, 0, 0), (100, 260, 200, 30))
polygon(screen, (0, 0, 0), [(120, 90), (140, 80), (190, 140), (175, 150)])
polygon(screen, (0, 0, 0), [(280, 95), (260, 80), (210, 150), (220, 160)])
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

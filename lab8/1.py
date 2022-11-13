import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 0.5
screen = pygame.display.set_mode((1200, 700))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def new_ball():
    """рисует новый шарик """
    global x, y, r
    x = randint(100, 1100)
    y = randint(100, 600)
    r = randint(50, 200)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)


def click(event):
    """Отвечает за считывание клика мышкой"""
    global score
    event.x = event.pos[0]
    event.y = event.pos[1]
    if (x-event.x)**2 + (y-event.y)**2 <= r**2:
        score += 1
        print(score)


score = 0
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    X = []
    Y = []
    r = []
    Vx = []
    Vy = []
    color = []
    k = 3
    s = False
    for j in range(k):
        X.append(randint(100, 1000))
        Y.append(randint(200, 700))
        r.append(randint(10, 100))
        Vx.append(randint(-5, 5))
        Vy.append(randint(-5, 5))
        color.append(COLORS[randint(0, 5)])
        if randint(1, 10) == 1:
            s = True
    if s is True:
        X.append(randint(100, 1000))
        Y.append(randint(200, 700))
        r.append(randint(10, 100))
        Vx.append(randint(-5, 5))
        Vy.append(randint(-5, 5))
        color.append(COLORS[randint(0, 5)])



    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)

    new_ball()
    pygame.display.update()
    screen.fill(WHITE)

pygame.quit()

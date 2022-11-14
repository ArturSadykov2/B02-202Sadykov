import pygame
from pygame.draw import *
from random import randint, choice
pygame.init()

FPS = 100
screen = pygame.display.set_mode((1200, 700))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def new_ball(x, y, r, color):
    """рисует новый шарик """
    circle(screen, color, (x, y), r)


def click():
    """Отвечает за считывание клика мышкой"""
    global points
    event.x = event.pos[0]
    event.y = event.pos[1]
    for i in range(k):
        if (X[i]-event.x)**2 + (Y[i]-event.y)**2 <= R[i]**2:
            points += 1
            X[i] = randint(100, 1000)
            Y[i] = randint(200, 600)
            R[i] = randint(10, 100)
            Vx[i] = randint(-5, 5)
            Vy[i] = randint(-5, 5)
            Color[i] = COLORS[randint(0, 5)]
    if (X[k] <= event.x) and (X[k] + R[k] >= event.x) and (Y[k] <= event.y) and (Y[k] + R[k] >= event.y):
        points += 10
        X[k] = randint(100, 1000)
        Y[k] = randint(200, 600)
        R[k] = randint(50, 100)
        Vx[k] = randint(-20, 20)
        Vy[k] = randint(-20, 20)
        Color[k] = COLORS[randint(0, 5)]


def score(point):
    """Функция, прибавляющая очки за попадания.
    score - очки
    """
    g = pygame.font.SysFont("comicsansms", 35)
    value = g.render("Ваш счет:" + str(point), True, BLUE)
    screen.blit(value, [100, 110])


points = 0
pygame.display.update()
clock = pygame.time.Clock()
finished = False
X = []
Y = []
R = []
Vx = []
Vy = []
Color = []
k = 7
s = False
for j in range(k):
    X.append(randint(100, 1000))
    Y.append(randint(200, 600))
    R.append(randint(10, 100))
    Vx.append(randint(-5, 5))
    Vy.append(randint(-5, 5))
    Color.append(COLORS[randint(0, 5)])
X.append(randint(100, 1000))
Y.append(randint(200, 700))
R.append(randint(50, 100))
Vx.append(randint(-20, 20))
Vy.append(randint(-20, 20))
Color.append(COLORS[randint(0, 5)])
while not finished:
    screen.fill(WHITE)
    score(points)
    for j in range(k):
        new_ball(X[j], Y[j], R[j], Color[j])
    for j in range(k):
        if (X[j] + R[j] + Vx[j] >= 1200) or (X[j] - R[j] + Vx[j] <= 0):
            Vx[j] = -Vx[j]
        if (Y[j] + R[j] + Vy[j] >= 700) or (Y[j] - R[j] + Vy[j] <= 0):
            Vy[j] = -Vy[j]
        X[j] += Vx[j]
        Y[j] += Vy[j]
    rect(screen, Color[k], (X[k], Y[k], R[k], R[k]))
    if (X[k] + R[k] + Vx[k] >= 1200) or (X[k] + Vx[k] <= 0):
        Vy[k] = Vy[k]*choice([-1, 1])
        Vx[k] = -Vx[k]
    if (Y[k] + R[k] + Vy[k] >= 700) or (Y[k] + Vy[k] <= 0):
        Vx[k] = Vx[k]*choice([-1, 1])
        Vy[k] = -Vy[k]
    X[k] += Vx[k]
    Y[k] += Vy[k]
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click()

pygame.quit()

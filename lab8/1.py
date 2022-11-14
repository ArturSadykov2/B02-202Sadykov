import pygame
from pygame.draw import *
from random import randint, choice
pygame.init()

FPS = 100
screen = pygame.display.set_mode((1200, 700))
k = 10            # Количество шариков на экране

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


X = []
Y = []
R = []
Vx = []
Vy = []
Color = []


def new_ball(x, y, r, color):
    """Рисует новый шарик
     x - координата центра x
     y - координата центра y
     r - радиус шарика
     color - цвет
     """
    circle(screen, color, (x, y), r)


def click():
    """Отвечает за считывание клика мышкой и создание нового шарика взамен прокликанного
    X - координата объекта по горизонтали
    Y - координата объекта по вертикали
    R - размер объекта
    Vx - скорость объекта по горизонтали
    Vy - скорость объекта по вертикали
    k - количество шариков
        """
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


def new_rect(x, y, r, color):
    """Рисует новый квадрат
     x - координата левого верхнего угла квадрата x
     y - координата левого верхнего угла квадрата y
     r - сторона квадрата
     color - цвет
     """
    rect(screen, color, (x, y, r, r))


def generate_start_positions():
    """Функция генерирует массивы со стартовыми положениями, размерами и цветами для шариков и квадрата.
    k - количество шариков, одновременно присутствующих на экране.
    """
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
    return X, Y, R, Vx, Vy, Color


def circle_move():
    """Функция отвечает за движение шарика и отражение его от стенок
    X - координата центра шарика по горизонтали
    Y - координата центра шарика по вертикали
    R - радиус шарика
    Vx - скорость шарика по горизонтали
    Vy - скорость шарика по вертикали
    k - количество шариков
    """
    for h in range(k):
        if (X[h] + R[h] + Vx[h] >= 1200) or (X[h] - R[h] + Vx[h] <= 0):
            Vx[h] = -Vx[h]
        if (Y[h] + R[h] + Vy[h] >= 700) or (Y[h] - R[h] + Vy[h] <= 0):
            Vy[h] = -Vy[h]
        X[h] += Vx[h]
        Y[h] += Vy[h]
    return X, Y, Vx, Vy


def rect_move():
    """Функция отвечает за движение шарика и отражение его от стенок
        X - координата левого верхнего угла квадрата по горизонтали
        Y - координата левого верхнего угла квадрата по вертикали
        R - сторона квадрата
        Vx - скорость квадрата по горизонтали
        Vy - скорость квадрата по вертикали
        """
    if (X[k] + R[k] + Vx[k] >= 1200) or (X[k] + Vx[k] <= 0):
        Vy[k] = Vy[k]*choice([-1, 1])
        Vx[k] = -Vx[k]
    if (Y[k] + R[k] + Vy[k] >= 700) or (Y[k] + Vy[k] <= 0):
        Vx[k] = Vx[k]*choice([-1, 1])
        Vy[k] = -Vy[k]
    X[k] += Vx[k]
    Y[k] += Vy[k]
    return X, Y, Vx, Vy


points = 0
pygame.display.update()
clock = pygame.time.Clock()
finished = False

generate_start_positions()

while not finished:
    screen.fill(WHITE)
    for j in range(k):
        new_ball(X[j], Y[j], R[j], Color[j])
    new_rect(X[k], Y[k], R[k], Color[k])
    circle_move()
    rect_move()
    score(points)
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click()

pygame.quit()

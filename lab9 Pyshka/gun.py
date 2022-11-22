import math
from random import choice, randint

import pygame

k = 2
FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = (100, 100, 100)
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600


class Ball:
    def __init__(self, screen: pygame.Surface):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = gun.x
        self.y = gun.y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """

        if self.x + self.r + self.vx >= 800:
            self.vx = -self.vx
        if self.y + self.r - self.vy >= 580:
            self.vy = -0.4*self.vy
            self.vx = self.vx//1.25
        if self.y < 565:
            self.vy = self.vy - 1
        self.x += self.vx
        self.y -= self.vy

    def draw(self):
        """Функция, отрисовавающая шарик в заданных координатах x, y и с заданным радиусом r."""
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.


        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        global i, k
        s = False
        for i in range(k):
            if (self.x - target.x[i])**2 + (self.y - target.y[i])**2 <= (self.r + target.r[i])**2:
                return True
        if s is False:
            return False


class Gun:
    """Класс, отвечающий за отрисовку и функциональность пушки"""
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY
        self.x = 40
        self.y = 550

    def fire2_start(self, event):
        """Функция срабатывает при удержании левой кнопки мыши, отвечает за начальную скорость мяча"""
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            if event.pos[0] != self.x:
                if event.pos[0] > self.x:
                    self.an = math.atan((-event.pos[1]+self.y) / (event.pos[0]-self.x))
                else:
                    self.an = 3.14 - math.atan((event.pos[1] - self.y) / (event.pos[0] - self.x))
            else:
                self.an = 1.57
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        """Функция, отрисовывающая пушку в зависимости от положения мыши."""
        length = 10 + self.f2_power//3
        pygame.draw.circle(screen, BLACK, (self.x - 17, self.y + 13), 8)
        pygame.draw.circle(screen, BLACK, (self.x + 17, self.y + 13), 8)
        pygame.draw.line(self.screen, self.color, (self.x, self.y - 5),
                                                  (self.x + length*math.cos(self.an),
                                                   self.y - 5 - length*math.sin(self.an)), 9)
        pygame.draw.line(screen, BLACK, (self.x - 25, self.y), (self.x + 25, self.y), 10)

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY

    def gun_move(self, m):
        """Движение пушки"""
        if m.key == pygame.K_LEFT:
            gun.x -= 8
        elif m.key == pygame.K_RIGHT:
            gun.x += 8


class Target:
    """Класс, отрисовывающий мишень в случайной точке"""
    def __init__(self):
        self.points = 0
        self.live = 1
        self.x = [0, 0]
        self.y = [0, 0]
        self.r = [0, 0]
        self.color = [0, 0]

    def new_target(self):
        """ Инициализация новой цели. """
        global i
        self.x[i] = randint(600, 780)
        self.y[i] = randint(300, 500)
        self.r[i] = randint(10, 50)
        self.color[i] = RED

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def draw(self):
        """Функия, отрисовывающая мишень в сгенерированных координатах"""
        pygame.draw.circle(screen, self.color[i], (self.x[i], self.y[i]), self.r[i])


def score():
    """Функция, прибавляющая очки за попадания.
    points - очки
    """
    g = pygame.font.SysFont("comicsansms", 35)
    value = g.render("Ваш счет:" + str(target.points), True, BLACK)
    screen.blit(value, [100, 110])


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []


clock = pygame.time.Clock()
gun = Gun(screen)
target = Target()
finished = False
for i in range(k):
    target.new_target()

while not finished:
    screen.fill(WHITE)
    gun.draw()
    for i in range(2):
        target.draw()
    for b in balls:
        b.draw()
    score()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
        if event.type == pygame.KEYDOWN:
            gun.gun_move(event)

    for b in balls:
        b.move()
        if b.hittest() and target.live:
            target.hit()
            target.new_target()
    gun.power_up()

pygame.quit()

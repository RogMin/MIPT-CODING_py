import pygame
from pygame.draw import *


def draw_smile():
    screen = pygame.display.set_mode((400, 400))
    screen.fill((225, 225, 225))
    circle(screen, (0, 0, 0), (200, 175), 101)
    circle(screen, (255, 255, 0), (200, 175), 100)

    circle(screen, (0, 0, 0), (150, 175), 21)
    circle(screen, (255, 0, 0), (150, 175), 20)
    circle(screen, (0, 0, 0), (150, 175), 8)

    circle(screen, (0, 0, 0), (250, 155), 22)
    circle(screen, (255, 0, 0), (250, 155), 21)
    circle(screen, (0, 0, 0), (250, 155), 9)

    rect(screen, (0, 1, 0), (150, 230, 100, 20))

    polygon(screen, (0, 0, 0), [(195, 175), (235, 125), (290, 125)])
    polygon(screen, (0, 0, 0), [(190, 175), (150, 125), (100, 125)])


draw_smile()
pygame.init()
FPS = 30
pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

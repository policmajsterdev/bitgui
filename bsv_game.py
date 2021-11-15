import pygame
import sys
import random

mainClock = pygame.time.Clock()

from pygame.locals import *

pygame.init()

pygame.display.set_caption("gieras")
screen = pygame.display.set_mode((550, 800), 0, 32)

display = pygame.Surface((275, 400))

particles = []
platforms = [[[0, display.get_height() - 1], [display.get_width(), display.get_height() - 1]]]
last_point = [display.get_width() // 2, display.get_height()]
scrool = 0

line_color = (255, 153, 51)
line_placing_color = (255, 153, 51)
line_width = 1

player_pos = [display.get_width() // 2, display.get_height() // 2]


while True:

    display.fill((0,0,0))

    mx, my = pygame.mouse.get_pos()
    mx = mx // 2
    my = my // 2



    for platform in platforms:
        pygame.draw.line(display, line_color, [platform[0][0], platform[0][1] - scrool], [platform[1][0], platform[1][1] - scrool], line_width)

    pygame.draw.line(display, line_placing_color, [last_point[0], last_point[1] - scrool], [mx, my])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                last_point = [mx, my + scrool]
        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                platforms.append([last_point, [mx, my + scrool]])

    screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0))
    particles.append([player_pos, [random.randint(0, 20) / 10 - 1, -2], random.randint(4, 6)])

    for particle in particles:
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        particle[2] -= 0.1
        particle[1][1] += 0.1
        pygame.draw.circle(screen, (255, 255, 255), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
        if particle[2] <= 0:
            particles.remove(particle)

    pygame.display.update()
    mainClock.tick(30)
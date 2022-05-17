import pygame, sys
from pygame.locals import *
import random

pygame.init()

FPS = 30
FramePerSec = pygame.time.Clock()

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game")

x = 200
y = 200
w = 10
h = 10
grow_shrink = 5
move = 10

while True:
    DISPLAYSURF.fill(BLACK)
    rect = pygame.Rect(x, y, h, w)
    pygame.draw.rect(DISPLAYSURF, BLUE, rect)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    key_input = pygame.key.get_pressed()
    if key_input[pygame.K_LEFT]:
        x -= move
    if key_input[pygame.K_UP]:
        y -= move
    if key_input[pygame.K_RIGHT]:
        x += move
    if key_input[pygame.K_DOWN]:
        y += move
    if key_input[pygame.K_q]:
        x -= grow_shrink / 2
        y -= grow_shrink / 2
        h += grow_shrink
        w += grow_shrink
    if key_input[pygame.K_w]:
        x += grow_shrink / 2
        y += grow_shrink / 2
        h -= grow_shrink
        w -= grow_shrink

    pygame.display.update()
    FramePerSec.tick(FPS)

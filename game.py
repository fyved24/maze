import maze
import numpy as np
import pygame
import sys
from pygame.locals import *


if __name__ == '__main__':
    pygame.init()
    font1 = pygame.font.Font(None, 24)
    pygame.key.set_repeat()
    # pygame.mouse.set_visible(False)
    size = (10, 10)
    screen_size = (size[0] * 90, size[1] * 90)
    screen = pygame.display.set_mode(screen_size)        # 设置屏幕大小
    mouse = pygame.image.load("mouse.png").convert_alpha()
    mouse = pygame.transform.scale(mouse, (30, 30))
    block = pygame.image.load("block.png").convert_alpha()
    block = pygame.transform.scale(block, (30, 30))
    start = (5, 5)
    var = maze.Maze(size, start)
    num_rows, num_cols = var.get_shape()
    M = var.get_blocks()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
        screen.fill((169, 169, 169))  # 屏幕填充颜色
        for i in range(0, size[0] * 3):
            for j in range(0, size[1] * 3):
                screen.blit(block, (i*30, j*30))
        for i in range(1, size[0] * 3, 3):
            for j in range(0, size[1] * 3, 3):
                screen.blit(mouse, (i * 30, j * 30))
        pygame.display.update()

import maze
import numpy as np
import pygame
import sys
from pygame.locals import *
from utils.utils import *


if __name__ == '__main__':
    pygame.init()
    font1 = pygame.font.Font(None, 24)
    pygame.key.set_repeat(100)
    mouse_down = 0
    mouse_down_x = mouse_down_y = 0
    # pygame.mouse.set_visible(False)
    rows = 10  # 后续改成输入
    columns = 10
    size = (rows, columns)
    screen_size = (size[0] * 90, size[1] * 90)
    full_matrix = np.ones((columns * 3, rows * 3), dtype=np.uint8)
    screen = pygame.display.set_mode(screen_size)        # 设置屏幕大小
    mouse_icon = pygame.image.load("mouse.png").convert_alpha()  # 老鼠
    mouse_icon = pygame.transform.scale(mouse_icon, (30, 30))
    block_icon = pygame.image.load("block.png").convert_alpha()  # 墙砖
    block_icon = pygame.transform.scale(block_icon, (30, 30))
    start = (rows//2, columns//2)
    var = maze.Maze(size, start)
    locate_x = start[0] * 3 + 1
    locate_y = start[1] * 3 + 1
    pos_y = locate_x * 30
    pos_x = locate_y * 30
    M = var.get_blocks()
    blocks = var.get_blocks()  # 获取块矩阵
    for row in range(0, rows):
        for col in range(0, columns):
            print_wall(blocks[row][col], (row, col), full_matrix)
    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            key_s = pygame.key.get_pressed()
            if event.type == MOUSEBUTTONDOWN:
                mouse_down = event.button
                mouse_down_x, mouse_down_y = event.pos
                mouse_down_x = mouse_down_x // 30
                mouse_down_y = mouse_down_y // 30
                if full_matrix[mouse_down_y][mouse_down_x] == 0:
                    full_matrix[mouse_down_y][mouse_down_x] = 1
                else:
                    full_matrix[mouse_down_y][mouse_down_x] = 0
            if key_s[K_ESCAPE]:
                sys.exit()
            # 移动
            # 算出下一个点，然后判断能否移动
            if key_s[97]:   # A左
                if full_matrix[locate_y][locate_x - 1] == 1:
                    locate_x -= 1
            if key_s[97 + 3]:  # D右
                if full_matrix[locate_y][locate_x + 1] == 1:
                    locate_x += 1
            if key_s[119]:   # W上
                if full_matrix[locate_y - 1][locate_x] == 1:
                    locate_y -= 1
            if key_s[115]:    # S下
                if full_matrix[locate_y + 1][locate_x]:
                    locate_y += 1
        pos_y = locate_x * 30
        pos_x = locate_y * 30
        pos = (pos_y, pos_x)
        screen.fill((169, 169, 169))  # 屏幕填充颜色d
        # 创建迷宫矩阵
        for y in range(0, rows * 3):
            for x in range(0, columns * 3):
                if full_matrix[x][y] == 0:
                    screen.blit(block_icon, (y * 30, x * 30))
        screen.blit(mouse_icon, pos)
        pygame.display.update()

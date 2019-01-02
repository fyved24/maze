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
    # pygame.mouse.set_visible(False)
    rows = 10  # 后续改成输入
    columns = 10
    size = (rows, columns)
    screen_size = (size[0] * 90, size[1] * 90)
    screen = pygame.display.set_mode(screen_size)        # 设置屏幕大小
    mouse_icon = pygame.image.load("mouse.png").convert_alpha()
    mouse_icon = pygame.transform.scale(mouse_icon, (30, 30))
    block_icon = pygame.image.load("block.png").convert_alpha()
    block_icon = pygame.transform.scale(block_icon, (30, 30))
    start = (rows//2, columns//2)
    locate_x, locate_y = start
    next_pos_x, next_pos_y = start
    var = maze.Maze(size, start)
    pos_y = (start[0] * 3 + 1) * 30
    pos_x = (start[1] * 3 + 1) * 30
    M = var.get_blocks()
    blocks = var.get_blocks()  # 获取块矩阵
    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            key_s = pygame.key.get_pressed()
            if key_s[K_ESCAPE]:
                sys.exit()
            # 移动
            # 算出下一个点，然后判断能否移动
            ##############################################
            if key_s[97]:   # A左
                if var.get_block((locate_x, locate_y)).i_can_stand('L'):
                    next_pos_x = pos_x - 30          # 下一个位置坐标
            if key_s[97 + 3]:  # D右
                if var.get_block((locate_x, locate_y)).i_can_stand('R'):
                    next_pos_x = pos_x + 30
            if key_s[119]:   # W上
                if var.get_block((locate_x, locate_y)).i_can_stand('U'):
                    next_pos_y = pos_y - 30
            if key_s[115]:    # S下
                if var.get_block((locate_x, locate_y)).i_can_stand('D'):
                    next_pos_y = pos_y + 30
            next_x = next_pos_x // 90  # 下一个块坐标
            next_y = next_pos_y // 90
            x = (next_x * 3 + 1) * 30  #
            y = (next_y * 3 + 1) * 30
            if next_pos_x - x:  # 发生x位移
                if next_pos_x - x > 0:
                    if var.get_block((next_x, next_y)).i_can_stand('R'):
                        pos_x = next_pos_x
                    elif var.get_block((next_x, next_y)).i_can_stand('L'):
                        pos_x = next_pos_x
            if next_pos_y - y:  # 发生y位移
                if next_pos_y - y > 0:
                    if var.get_block((next_x, next_y)).i_can_stand('D'):
                        pos_x = next_pos_x
                    elif var.get_block((next_x, next_y)).i_can_stand('U'):
                        pos_x = next_pos_x
            ###############################################
        pos = (pos_x, pos_y)
        screen.fill((169, 169, 169))  # 屏幕填充颜色
        for row in range(0, rows):
            for col in range(0, columns):
                print_wall(screen, block_icon, blocks[row][col], (row, col))
        screen.blit(mouse_icon, pos)
        pygame.display.update()

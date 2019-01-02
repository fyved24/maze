import maze
import numpy as np
import pygame
import sys
import time
from pygame.locals import *
from utils.utils import *


def print_text(screen, font, x, y, text, color=(255, 255, 255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x, y))


color = 255, 255, 0


if __name__ == '__main__':
    pygame.init()
    font1 = pygame.font.Font(None, 50)
    font2 = pygame.font.Font(None, 30)
    pygame.key.set_repeat(100)
    mouse_down = 0
    mouse_down_x = mouse_down_y = 0
    # pygame.mouse.set_visible(False)
    rows = 10  # 后续改成输入
    columns = 10
    clock_start = 0
    game_over = True
    seconds = 31
    size = (rows, columns)
    screen_size = (size[0] * 90, size[1] * 90)    # 屏幕大小
    full_matrix = np.ones((columns * 3, rows * 3), dtype=np.uint8)
    screen = pygame.display.set_mode(screen_size)        # 设置屏幕大小
    mouse_icon = pygame.image.load("mouse.png").convert_alpha()  # 老鼠
    mouse_icon = pygame.transform.scale(mouse_icon, (30, 30))
    block_icon = pygame.image.load("block.png").convert_alpha()  # 墙砖
    block_icon = pygame.transform.scale(block_icon, (30, 30))
    start = (rows//2, columns//2)   # 开始点
    end = (rows - 1, columns - 1)
    locate_x = start[0] * 3 + 1
    locate_y = start[1] * 3 + 1
    pos_y = locate_x * 30
    pos_x = locate_y * 30
    # 下面是自动生成迷宫
    #############
    var = maze.Maze(size, start, end)
    answer = var.get_answer()
    while len(answer) == 0:
        var = maze.Maze(size, start, end)
        answer = var.get_answer()
    blocks = var.get_blocks()  # 获取块矩阵
    for row in range(0, rows):
        for col in range(0, columns):
            print_wall(blocks[row][col], (row, col), full_matrix)
    ##############
    mouse_flag = False
    win_flag = False
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                temp = np.array(full_matrix)
                temp.tofile("matrix.bin")
                sys.exit()
            key_s = pygame.key.get_pressed()
            if event.type == MOUSEBUTTONDOWN:       # 捕捉鼠标
                mouse_down = event.button
                mouse_down_x, mouse_down_y = event.pos
                mouse_down_x = mouse_down_x // 30
                mouse_down_y = mouse_down_y // 30
                mouse_flag = True
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
                    if locate_y == 28 and locate_y == 28:
                        win_flag = True
                    else:
                        locate_y += 1
            if key_s[K_RETURN]:
                if game_over:
                    win_flag = False
                    game_over = False
                    score = 0
                    seconds = 50
                    clock_start = time.clock()
        current = time.clock() - clock_start
        if seconds - current < 0:
            game_over = True
        pos = (pos_y, pos_x)
        # 如果游戏结束
        if game_over:
            screen.fill((169, 169, 169))  # 屏幕填充颜色
            if win_flag:
                print_text(screen, font1, 0, 80, "WIN!!!")
            elif clock_start != 0:
                print_text(screen, font2, 0, 160, str(answer[::-1][:5]))
                print_text(screen, font2, 0, 190, str(answer[::-1][5:10]))
                print_text(screen, font2, 0, 220, str(answer[::-1][10:15]))
                print_text(screen, font2, 0, 250, str(answer[::-1][15:20]))
                print_text(screen, font2, 0, 280, str(answer[::-1][20:]))

            print_text(screen, font1, 0, 0, "Press Enter to start...")
        screen.blit(mouse_icon, pos)
        if not game_over:
            # full_matrix[mouse_down_x][mouse_down_y] = not full_matrix[mouse_down_x][mouse_down_y]
            if mouse_flag:
                full_matrix[mouse_down_y][mouse_down_x] = not full_matrix[mouse_down_y][mouse_down_x]
                mouse_flag = False
            pos_y = locate_x * 30
            pos_x = locate_y * 30
            # 创建迷宫
            screen.fill((169, 169, 169))  # 屏幕填充颜色
            for y in range(0, rows * 3):
                for x in range(0, columns * 3):
                    if full_matrix[x][y] == 0:
                        screen.blit(block_icon, (y * 30, x * 30))
            if win_flag:
                game_over = True
            screen.blit(mouse_icon, pos)
            print_text(screen, font1, 0, 80, "Time :" + str(int(seconds - current)))
        pygame.display.update()

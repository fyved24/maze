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


def draw_maze(screen, block_icon, rows, cols, full_matrix):
    screen.fill((169, 169, 169))  # 屏幕填充颜色
    for y in range(0, rows * 3):
        for x in range(0, cols * 3):
            if full_matrix[x][y] == 0:
                screen.blit(block_icon, (y * 30, x * 30))


def draw_mouse(screen, mouse_icon, pos):
    screen.blit(mouse_icon, pos)


color = 255, 255, 0

if __name__ == '__main__':
    pygame.init()
    font1 = pygame.font.Font(None, 50)
    font2 = pygame.font.Font(None, 30)
    pygame.key.set_repeat(100)
    mouse_down = 0
    mouse_down_x = mouse_down_y = 0
    # pygame.mouse.set_visible(False)
    full_matrix = np.loadtxt("matrix.txt", dtype='int')
    columns, rows = full_matrix.shape    #
    answer = []
    with open("answer.txt", 'r') as f:
        for line in f.readlines():
            answer += eval(line)
    columns = columns // 3
    rows = rows // 3
    size = (rows, columns)
    start = (rows // 2, columns // 2)  # 开始点
    end = (rows - 1, columns - 1)
    switch = eval(input("是自动生成(0)还是加载(1)?"))
    # 下面是自动生成迷宫
    #############
    if switch == 0:
        rows = eval(input("输入行数"))
        columns = eval(input("输入列数"))
        full_matrix = np.ones((columns * 3, rows * 3), dtype=int)
        size = (rows, columns)
        start = (rows // 2, columns // 2)  # 开始点
        end = (rows - 1, columns - 1)
        var = maze.Maze(size, start, end)
        answer = var.get_answer()
        blocks = var.get_blocks()  # 获取块矩阵
        for row in range(0, rows):
            for col in range(0, columns):
                print_wall(blocks[row][col], (row, col), full_matrix)
    ##############
    clock_start = 0
    game_over = True
    seconds = 31
    screen_size = (size[0] * 90, size[1] * 90)  # 屏幕大小
    screen = pygame.display.set_mode(screen_size)  # 设置屏幕大小
    screen.fill((169, 169, 169))  # 屏幕填充颜色
    mouse_icon = pygame.image.load("mouse.png").convert_alpha()  # 老鼠
    mouse_icon = pygame.transform.scale(mouse_icon, (30, 30))
    block_icon = pygame.image.load("block.png").convert_alpha()  # 墙砖
    block_icon = pygame.transform.scale(block_icon, (30, 30))

    locate_x = start[0] * 3 + 1  # 位于哪一块
    locate_y = start[1] * 3 + 1
    pos_y = locate_x * 30  # 绘制块的位置
    pos_x = locate_y * 30

    mouse_flag = False
    win_flag = False
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                c = input("保存当前迷宫?(y/n)")
                if c in ["Y", "y"]:
                    np.savetxt("matrix.txt", full_matrix, fmt='%d')  # 迷宫存盘
                    file = open('answer.txt', 'w')
                    file.write(str(answer))
                    file.close()
                sys.exit()
            key_s = pygame.key.get_pressed()
            if event.type == MOUSEBUTTONDOWN:  # 捕捉鼠标
                mouse_down = event.button
                mouse_down_x, mouse_down_y = event.pos
                mouse_down_x = mouse_down_x // 30
                mouse_down_y = mouse_down_y // 30
                mouse_flag = True
            # 移动
            # 算出下一个点，然后判断能否移动
            if key_s[97]:  # A左
                if full_matrix[locate_y][locate_x - 1] == 1:
                    locate_x -= 1
            if key_s[97 + 3]:  # D右
                if full_matrix[locate_y][locate_x + 1] == 1:
                    locate_x += 1
            if key_s[119]:  # W上
                if full_matrix[locate_y - 1][locate_x] == 1:
                    locate_y -= 1
            if key_s[115]:  # S下
                if full_matrix[locate_y + 1][locate_x]:
                    if locate_y == 28 and locate_y == 28:
                        win_flag = True
                    else:
                        locate_y += 1
            if key_s[103]:
                game_over = True
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
        pos_y = locate_x * 30  # 更新老鼠位置
        pos_x = locate_y * 30
        # 如果游戏结束
        if game_over:
            # screen.fill((169, 169, 169))  # 屏幕填充颜色
            if win_flag:  # 如果赢了
                print_text(screen, font1, 0, 80, "WIN!!!")
            elif clock_start != 0:        # 不是第一次开始
                print_text(screen, font1, 0, 80, "GAME OVER!!!")
                while len(answer):
                    x, y, = answer.pop()
                    pos = ((x * 3 + 1) * 30, (y * 3 + 1) * 30)
                    draw_mouse(screen, mouse_icon, pos)
                pygame.display.update()
            draw_maze(screen, block_icon, rows, columns, full_matrix)
            print_text(screen, font1, 0, 0, "Press Enter to start...")
        screen.blit(mouse_icon, pos)
        if not game_over:
            # full_matrix[mouse_down_x][mouse_down_y] = not full_matrix[mouse_down_x][mouse_down_y]
            if mouse_flag:
                full_matrix[mouse_down_y][mouse_down_x] = not full_matrix[mouse_down_y][mouse_down_x]
                mouse_flag = False
            draw_maze(screen, block_icon, rows, columns, full_matrix)
            if win_flag:
                game_over = True
            draw_mouse(screen, mouse_icon, pos)
            print_text(screen, font1, 0, 130, "Time :" + str(int(seconds - current)))
        pygame.display.update()



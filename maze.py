import numpy as np
import random
from matplotlib import pyplot as plt
import matplotlib.cm as cm
from block import Block


class Maze:
    def __init__(self, size, start):     # start是一个元组
        self.r_num, self.c_num = size
        self.maze = np.zeros((self.r_num, self.c_num, 5), dtype=np.uint8)    # [0, 0]: 第一个数 0是墙 1是路 1, 第二个数 1是已经被访问过
        self.road = [start]  # 走过的路的栈
        self.r, self.c = start     # 行和列
        self.maze[self.r, self.c, 0] = 1     # 起点打开
        self.dfs()            # 生成迷宫
        # 打开出口
        self.maze[self.r_num - 1, self.c_num - 1, 2] = 1
        self.blocks = []        # 根据矩阵生成的迷宫
        self.create_blocks()

    def dfs(self):
        # 生成迷宫
        while len(self.road) > 0:  # 如果栈中还有元素
            self.maze[self.r, self.c, 4] = 1
            directions = []
            if self.c > 0 and self.maze[self.r, self.c - 1, 4] == 0:  # 判断左方是否可以走
                directions.append('L')
            if self.r > 0 and self.maze[self.r - 1, self.c, 4] == 0:  # 判断上方是否可以走
                directions.append('U')
            if self.c < self.c_num - 1 and self.maze[self.r, self.c + 1, 4] == 0:  # 判断右方是否可以走
                directions.append('R')
            if self.r < self.r_num - 1 and self.maze[self.r + 1, self.c, 4] == 0:  # 判断下方是否可以走
                directions.append('D')
            if len(directions):   # 如果还有方向可走
                self.road.append((self.r, self.c))
                direction = random.choice(directions)
                if direction == 'L':
                    self.maze[self.r, self.c, 0] = 1  # 设置为已经访问过
                    self.c -= 1
                    self.maze[self.r, self.c, 2] = 1
                if direction == 'U':
                    self.maze[self.r, self.c, 1] = 1  # 设置为已经访问过
                    self.r -= 1
                    self.maze[self.r, self.c, 3] = 1
                if direction == 'R':
                    self.maze[self.r, self.c, 2] = 1  # 设置为已经访问过
                    self.c += 1
                    self.maze[self.r, self.c, 0] = 1
                if direction == 'D':
                    self.maze[self.r, self.c, 3] = 1  # 设置为已经访问过
                    self.r += 1
                    self.maze[self.r, self.c, 1] = 1
            else:
                self.r, self.c = self.road.pop()     # 没有元素跳出上一个元素

    def create_blocks(self):  # 转化为块矩阵
        for row in range(0, self.r_num):
            line = []
            for col in range(0, self.c_num):
                block = Block(self.maze[row, col])
                line.append(block)
            self.blocks.append(line)

    def get_blocks(self):
        return self.blocks

    def get_block(self, locate):
        x, y = locate
        return self.blocks[x][y]

    def get_maze(self):
        return self.maze

    def get_shape(self):               # 获取尺寸大小
        return self.r_num, self.c_num

    def get_point(self, point):        # 获取一个块的状态
        x, y = point
        return self.maze[x, y]
import numpy as np
import random
from matplotlib import pyplot as plt
import matplotlib.cm as cm


class Maze:
    def __init__(self, size, start):     # start是一个元组
        self.r_num, self.c_num = size
        self.maze = np.zeros((self.r_num, self.c_num, 5), dtype=np.uint8)    # [0, 0]: 第一个数 0是墙 1是路 1, 第二个数 1是已经被访问过
        self.road = [start]  # 走过的路的栈
        self.r, self.c = start     # 行和列
        self.maze[self.r, self.c, 0] = 1     # 起点打开
        self.maze[self.r, self.c, 1] = 1     # 标记已经被访问过
        self.dfs()            # 生成迷宫
        # 打开出口
        self.maze[self.r_num - 1, self.c_num - 1, 0] = 1
        self.maze[self.r_num - 1, self.c_num - 1, 1] = 1

    def move(self):
        directions = []
        if self.c > 0 and self.maze[self.r, self.c - 1, 1] == 0:     # 判断左方是否可以走
            directions.append('L')
        if self.r > 0 and self.maze[self.r - 1, self.c, 2] == 0:     # 判断上方是否可以走
            directions.append('U')
        if self.c < self.c_num - 1 and self.maze[self.r, self.c + 1, 3] == 0:     # 判断右方是否可以走
            directions.append('R')
        if self.r < self.r_num - 1 and self.maze[self.r + 1, self.c, 4] == 0:     # 判断下方是否可以走
            directions.append('D')
        return directions

    def opposite(self, next_point):       # 判断对面的点是否可以走
        dr = next_point[0] - self.r       # row轴移动量
        dc = next_point[1] - self.c       # column轴移动量
        r = next_point[0] + dr
        c = next_point[1] + dc
        if 0 <= r < self.r_num and 0 <= c < self.c_num:    # 判断点在棋盘中
            if self.maze[r, c, 0] == 0:
                return r, c
        else:
            return r, c
        return None

    def dfs(self):
        # 生成迷宫
        while len(self.road) > 0:  # 如果栈中还有元素
            directions = self.move()
            if len(directions) > 0:   # 如果还有方向可走
                self.road.append((self.r, self.c))
                direction = random.choice(directions)
                if direction == 'L':
                    self.maze[self.r, self.c, 1] = 1  # 设置为已经访问过
                    if self.opposite((self.r, self.c - 1)):    # 如果对面的点是墙且在内部
                        self.c -= 1
                        self.maze[self.r, self.c, 0] = 1
                if direction == 'U':
                    self.maze[self.r, self.c, 2] = 1  # 设置为已经访问过
                    if self.opposite((self.r - 1, self.c)):    # 如果对面的点是墙且在内部
                        self.r -= 1
                        self.maze[self.r, self.c, 0] = 1
                if direction == 'R':
                    self.maze[self.r, self.c, 3] = 1  # 设置为已经访问过
                    if self.opposite((self.r, self.c + 1)):    # 如果对面的点是墙且在内部
                        self.c += 1
                        self.maze[self.r, self.c, 0] = 1
                if direction == 'D':
                    self.maze[self.r, self.c, 4] = 1  # 设置为已经访问过
                    if self.opposite((self.r + 1, self.c)):    # 如果对面的点是墙且在内部
                        self.r += 1
                        self.maze[self.r, self.c, 0] = 1
            else:
                self.r, self.c = self.road.pop()
            print(len(directions))
            print(directions)
            self.print_maze()

    def get_maze(self):
        return self.maze

    def get_shape(self):
        return self.r_num, self.c_num

    def get_point(self, point):
        x, y = point
        return self.maze[x, y]

    def print_maze(self):
        print(self.r, ", ", self.c)
        for i in self.maze:
            for j in i:
                if j[1] or j[2] or j[3] or j[4]:
                    print(1, end=" ")
                else:
                    print(0, end=" ")
            print()
        print()

#
#
# # maze的0， 1， 2， 3是左上右下四个方向，4是这个点是否已经被访问过
#
#
# class Maze:
#     def __init__(self, size, start):     # start是一个元组
#         self.r_num, self.c_num = size
#         self.maze = np.zeros((self.r_num, self.c_num, 5), dtype=np.uint8)
#         self.road = [start]  # 走过的路的栈
#         self.r, self.c = start     # 行和列
#         self.dfs()
#         self.maze[0, 0, 0] = 1
#         self.maze[self.r_num - 1, self.c_num - 1, 2] = 1
#
#     def get_maze(self):
#         return self.maze
#
#     def get_matrix(self):
#         matrix = np.zeros((self.r_num * 5, self.c_num * 5), dtype=int)
#         for i in range(0, self.r_num):
#             for j in range(0, self.c_num):
#                 shape = self.get_point((i, j))
#                 if shape[4] == 1:
#                     matrix[i * 5 + 1: i * 5 + 4][j * 5 + 1: j * 5 + 4] = 1
#                 if shape[0] == 1:
#                     matrix[i * 5 + 1: i * 5 + 4][j * 5] = 1
#                 if shape[1] == 1:
#                     matrix[i * 5][j * 5 + 1: j * 5 + 4] = 1
#                 if shape[2] == 1:
#                     matrix[i * 5 + 1: i * 5 + 4][j * 5 + 5] = 1
#                 if shape[3] == 1:
#                     matrix[i * 5 + 5][j * 5 + 1: j * 5 + 4] = 1
#         return matrix
#
#     def get_shape(self):
#         return self.r_num, self.c_num
#
#     def get_point(self, point):
#         x, y = point
#         return self.maze[x, y]
#
#     def move(self):
#         directions = []
#         if self.c > 0 and self.maze[self.r, self.c - 1, 4] == 0:     # 判断左方是否可以走
#             directions.append('L')
#         if self.r > 0 and self.maze[self.r - 1, self.c, 4] == 0:     # 判断上方是否可以走
#             directions.append('U')
#         if self.c < self.c_num - 1 and self.maze[self.r, self.c + 1, 4] == 0:     # 判断右方是否可以走
#             directions.append('R')
#         if self.r < self.r_num - 1 and self.maze[self.r + 1, self.c, 4] == 0:     # 判断下方是否可以走
#             directions.append('D')
#         return directions
#
#     def dfs(self):
#         # 生成迷宫
#         while len(self.road) > 0:
#             self.maze[self.r, self.c, 4] = 1
#             directions = self.move()
#             if len(directions) > 0:
#                 self.road.append((self.r, self.c))
#                 direction = random.choice(directions)
#                 if direction == 'L':
#                     self.maze[self.r, self.c, 0] = 1
#                     self.c -= 1
#                     self.maze[self.r, self.c, 2] = 1
#                 if direction == 'U':
#                     self.maze[self.r, self.c, 1] = 1
#                     self.r -= 1
#                     self.maze[self.r, self.c, 3] = 1
#                 if direction == 'R':
#                     self.maze[self.r, self.c, 2] = 1
#                     self.c += 1
#                     self.maze[self.r, self.c, 0] = 1
#                 if direction == 'D':
#                     self.maze[self.r, self.c, 3] = 1
#                     self.r += 1
#                     self.maze[self.r, self.c, 1] = 1
#             else:
#                 self.r, self.c = self.road.pop()
#
#
# def convent(maze):
#     num_rows, num_cols = maze.get_shape()
#     image = np.zeros((num_rows * 10, num_cols * 10), dtype=np.uint8)
#     for row in range(0, num_rows):
#         for col in range(0, num_cols):
#             cell_data = maze.get_maze()[row, col]
#             for i in range(10 * row + 2, 10 * row + 8):
#                 image[i, range(10 * col + 2, 10 * col + 8)] = 255
#             if cell_data[0] == 1:
#                 image[range(10 * row + 2, 10 * row + 8), 10 * col] = 255
#                 image[range(10 * row + 2, 10 * row + 8), 10 * col + 1] = 255
#             if cell_data[1] == 1:
#                 image[10 * row, range(10 * col + 2, 10 * col + 8)] = 255
#                 image[10 * row + 1, range(10 * col + 2, 10 * col + 8)] = 255
#             if cell_data[2] == 1:
#                 image[range(10 * row + 2, 10 * row + 8), 10 * col + 9] = 255
#                 image[range(10 * row + 2, 10 * row + 8), 10 * col + 8] = 255
#             if cell_data[3] == 1:
#                 image[10 * row + 9, range(10 * col + 2, 10 * col + 8)] = 255
#     return image

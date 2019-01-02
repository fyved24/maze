import maze
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm

size = 10
bg_color = (30, 30, 30)
screen_size = (900, 600)
# screen = pygame.display.set_mode(screen_size)
# pygame.display.set_caption("性感老鼠")
# screen.fill(bg_color)

if __name__ == '__main__':
    size = (10, 10)
    start = (5, 5)
    var = maze.Maze(size, start)
    num_rows, num_cols = var.get_shape()
    M = var.get_blocks()
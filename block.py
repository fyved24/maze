import numpy as np


class Block(object):
    def __init__(self, M):
        self.block = np.zeros((3, 3), dtype=int)
        self.block[1, 1] = 1
        self.block[1, 0] = M[0]
        self.block[0, 1] = M[1]
        self.block[1, 2] = M[2]
        self.block[2, 1] = M[3]

    def i_can_stand(self, direction):
        f = 0
        if direction == 'L':
            f = self.block[1, 0]
        if direction == 'U':
            f = self.block[0, 1]
        if direction == 'R':
            f = self.block[1, 2]
        if direction == 'D':
            f = self.block[2, 2]
        return f

    def get_matrix(self):
        return self.block

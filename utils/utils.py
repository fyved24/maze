from block import Block


def print_wall(block, pos, full_matrix):
    matrix = block.get_matrix()
    row, col = pos
    for i in range(0, 3):
        for j in range(0, 3):
            if matrix[i][j] == 0:
                full_matrix[(col * 3 + j)][(row * 3 + i)] = 0

from block import Block


def print_wall(screen, icon, block, pos):
    matrix = block.get_matrix()
    row, col = pos
    for i in range(0, 3):
        for j in range(0, 3):
            if matrix[i][j] == 0:
                screen.blit(icon, ((col * 3 + j) * 30, (row * 3 + i) * 30))

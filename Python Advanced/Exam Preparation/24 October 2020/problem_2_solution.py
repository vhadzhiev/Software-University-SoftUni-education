def get_mated_queens(matrix, r, c):
    mated_queens = []
    directions = ['up', 'down', 'left', 'right', 'up_left', 'down_left', 'up_right', 'down_right']
    size = len(matrix)
    for direction in directions:
        if direction == 'up':
            for next_r in range(r - 1, -1, -1):
                if matrix[next_r][c] == 'Q':
                    mated_queens.append([next_r, c])
                    break
        elif direction == 'down':
            for next_r in range(r + 1, size):
                if matrix[next_r][c] == 'Q':
                    mated_queens.append([next_r, c])
                    break
        elif direction == 'left':
            for next_c in range(c - 1, -1, -1):
                if matrix[r][next_c] == 'Q':
                    mated_queens.append([r, next_c])
                    break
        elif direction == 'right':
            for next_c in range(c + 1, size):
                if matrix[r][next_c] == 'Q':
                    mated_queens.append([r, next_c])
                    break
        elif direction == 'up_left':
            for x in range(min(r, c) + 1):
                if matrix[r - x][c - x] == 'Q':
                    mated_queens.append([r - x, c - x])
                    break
        elif direction == 'down_left':
            for x in range(min(size - r, c)):
                if matrix[r + x][c - x] == 'Q':
                    mated_queens.append([r + x, c - x])
                    break
        elif direction == 'up_right':
            for x in range(min(r, size - c)):
                if matrix[r - x][c + x] == 'Q':
                    mated_queens.append([r - x, c + x])
                    break
        elif direction == 'down_right':
            for x in range(size - max(r, c)):
                if matrix[r + x][c + x] == 'Q':
                    mated_queens.append([r + x, c + x])
                    break

    return mated_queens


size = 8
board = []
king_r = 0
king_c = 0
for row in range(size):
    row_elements = input().split()
    board.append(row_elements)
    for col in range(len(row_elements)):
        if row_elements[col] == 'K':
            king_r = row
            king_c = col

mating_queens_list = get_mated_queens(board, king_r, king_c)
if mating_queens_list:
    for x in mating_queens_list:
        print(x)
else:
    print('The king is safe!')

def is_valid(matrix, r, c):
    return 0 <= r < len(matrix) and 0 <= c < len(matrix)


def count_bombs(matrix, r, c):
    bombs = 0
    check_positions = [[r - 1, c - 1], [r - 1, c], [r - 1, c + 1],
                       [r, c - 1], [r, c + 1],
                       [r + 1, c - 1], [r + 1, c], [r + 1, c + 1]]
    for position in check_positions:
        r, c = position
        if is_valid(field, r, c) and matrix[r][c] == '*':
            bombs += 1

    return str(bombs)


size = int(input())
bombs_count = int(input())

field = []
for row in range(size):
    field.append(size * [None])

for _ in range(bombs_count):
    coordinates = input()[1:-1].split(', ')
    row, col = int(coordinates[0]), int(coordinates[1])
    field[row][col] = '*'

for r in range(size):
    for c in range(size):
        if not field[r][c] == '*':
            field[r][c] = count_bombs(field, r, c)

for row in field:
    print(' '.join(row))

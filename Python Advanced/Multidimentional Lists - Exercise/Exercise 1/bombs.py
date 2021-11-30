def is_valid(matrix, size, r, c):
    return 0 <= r < size and 0 <= c < size and matrix[r][c] > 0


size = int(input())

matrix = []
for _ in range(size):
    matrix.append([int(x) for x in input().split()])

indices = input().split()

alive_cells = 0
alive_cells_sum = 0
explosion_indices = []
for i in range(len(indices)):
    r, c = [int(x) for x in indices[i].split(',')]
    bomb = matrix[r][c]
    if not is_valid(matrix, size, r, c):
        continue
    else:
        matrix[r][c] -= bomb
        if is_valid(matrix, size, r, c - 1):
            matrix[r][c - 1] -= bomb
        if is_valid(matrix, size, r, c + 1):
            matrix[r][c + 1] -= bomb
        if is_valid(matrix, size, r - 1, c - 1):
            matrix[r - 1][c - 1] -= bomb
        if is_valid(matrix, size, r - 1, c):
            matrix[r - 1][c] -= bomb
        if is_valid(matrix, size, r - 1, c + 1):
            matrix[r - 1][c + 1] -= bomb
        if is_valid(matrix, size, r + 1, c - 1):
            matrix[r + 1][c - 1] -= bomb
        if is_valid(matrix, size, r + 1, c):
            matrix[r + 1][c] -= bomb
        if is_valid(matrix, size, r + 1, c + 1):
            matrix[r + 1][c + 1] -= bomb

for row in matrix:
    for x in row:
        if x > 0:
            alive_cells += 1
            alive_cells_sum += x

print(f'Alive cells: {alive_cells}')
print(f'Sum: {alive_cells_sum}')

for row in matrix:
    print(' '.join(str(x) for x in row))

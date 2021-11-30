rows, columns = [int(x) for x in input().split()]

matrix = []
for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

max_sum = float('-inf')
row = 0
col = 0
for r in range(rows - 2):
    for c in range(columns - 2):
        total_sum = matrix[r][c] + matrix[r][c + 1] + matrix[r][c + 2] + matrix[r + 1][c] + matrix[r + 1][c + 1] + \
                    matrix[r + 1][c + 2] + matrix[r + 2][c] + matrix[r + 2][c + 1] + matrix[r + 2][c + 2]
        if total_sum > max_sum:
            max_sum = total_sum
            row = r
            col = c

print(f"Sum = {max_sum}")
print(matrix[row][col], matrix[row][col + 1], matrix[row][col + 2])
print(matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2])
print(matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2])

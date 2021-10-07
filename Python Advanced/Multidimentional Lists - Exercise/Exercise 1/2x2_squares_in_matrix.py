rows, columns = [int(x) for x in input().split()]

matrix = []
for _ in range(rows):
    matrix.append([x for x in input().split()])

found_matrices = 0
for r in range(rows - 1):
    for c in range(columns - 1):
        if matrix[r][c] == matrix[r][c+1] == matrix[r+1][c] == matrix[r+1][c+1]:
            found_matrices += 1

print(found_matrices)

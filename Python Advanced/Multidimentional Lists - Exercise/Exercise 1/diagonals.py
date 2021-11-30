n = int(input())

matrix = []
for _ in range(n):
    matrix.append([int(x) for x in input().split(', ')])

primary_diagonal_elements = []
secondary_diagonal_elements = []
for r in range(len(matrix)):
    primary_diagonal_elements.append(matrix[r][r])
    secondary_diagonal_elements.append(matrix[r][len(matrix) - r - 1])

print(
    f'Primary diagonal: {", ".join(str(x) for x in primary_diagonal_elements)}. Sum: {sum(primary_diagonal_elements)}')
print(
    f'Secondary diagonal: {", ".join(str(x) for x in secondary_diagonal_elements)}. Sum: {sum(secondary_diagonal_elements)}')

n = int(input())

matrix = []
for _ in range(n):
    matrix.append([int(x) for x in input().split()])

sum_of_primary_diagonal_elements = 0
sum_of_secondary_diagonal_elements = 0
for r in range(len(matrix)):
    sum_of_primary_diagonal_elements += (matrix[r][r])
    sum_of_secondary_diagonal_elements += (matrix[r][len(matrix) - r - 1])

diff = abs(sum_of_primary_diagonal_elements - sum_of_secondary_diagonal_elements)
print(diff)

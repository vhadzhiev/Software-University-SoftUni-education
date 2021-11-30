rows, columns = [int(x) for x in input().split()]

matrix = []
for r in range(rows):
    row = []
    matrix.append(row)
    for c in range(columns):
        row.append(f'{chr(97 + r)}{chr(97 + r + c)}{chr(97+r)}')

for i in range(len(matrix)):
    print(' '.join(x for x in matrix[i]))

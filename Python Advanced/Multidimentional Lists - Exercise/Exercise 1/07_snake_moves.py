rows, cols = [int(x) for x in input().split()]
word = input()

matrix = []
index = 0
for r in range(rows):
    matrix.append([None] * cols)
    for c in range(cols):
        if r % 2 == 0:
            matrix[r][c] = word[index]
        else:
            matrix[r][cols - 1 - c] = word[index]
        index = (index + 1) % len(word)

for elements in matrix:
    print(''.join(elements))

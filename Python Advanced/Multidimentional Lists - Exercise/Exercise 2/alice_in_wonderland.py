def is_valid(size, r, c):
    return 0 <= r < size and 0 <= c < size


size = int(input())

matrix = []
alice_r = 0
alice_c = 0
for row in range(size):
    row_elements = input().split()
    matrix.append(row_elements)
    for col in range(size):
        symbol = row_elements[col]
        if symbol == 'A':
            alice_r = row
            alice_c = col

matrix[alice_r][alice_c] = '*'
tea_bags = 0
party = None
r = alice_r
c = alice_c
while True:
    command = input()

    if command == 'up':
        r = r - 1
    elif command == 'down':
        r = r + 1
    elif command == 'left':
        c = c - 1
    elif command == 'right':
        c = c + 1

    if not is_valid(size, r, c):
        party = False
        break
    if matrix[r][c] == 'R':
        party = False
        matrix[r][c] = '*'
        break
    elif matrix[r][c].isnumeric():
        tea_bags += int(matrix[r][c])

    matrix[r][c] = '*'
    if tea_bags >= 10:
        party = True
        break

if party:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")
for row in matrix:
    print(' '.join(row))
